from pprint import pprint
from configparser import ConfigParser
from msgraph_client import MicrosoftGraphClient
from msgraph.generated.models.o_data_errors.o_data_error import ODataError
import pandas as pd
import os

scopes = [
    "Files.ReadWrite.All",
    "User.Read"
]

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read("configs/config.ini")

# Get the specified credentials.
client_id = config.get("graph_api", "client_id")
client_secret = config.get("graph_api", "client_secret")
tenant_id = config.get("graph_api", "tenant_id")
redirect_uri = config.get("graph_api", "redirect_uri")

print("ODSL Generator Bot\nAuthenticating account...\n")

# Initialize the Client.
graph_client = MicrosoftGraphClient(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scopes,
    tenant_id=tenant_id,
    credentials="configs/ms_graph_state.jsonc"
)

# Login to the Client.
status = graph_client.login()

if status:
    print("Authentication Successful!")
else:
    print("Authentication Failed!")
    exit()

# Grab the User Services and greet user.
graph_client.user().greet_user()

choice = -1

while choice != 0:
    print('Please choose one of the following options:')
    print('0. Exit')
    print('1. Create Shareable Link')
    print("\nChoice:")
    try:
        choice = int(input())
    except ValueError:
        choice = -1

    try:
        if choice == 0:
            print('Goodbye...')
        elif choice == 1:
            # Grab the Drive Items Services.
            drive_items_services = graph_client.drive_item()
            
            if os.path.isfile('C:/Users/User/OneDrive/Documents/OneDrive-Bot/msgraph/subslist.xlsx'):
                print('\nsubslist.xlsx file found.')
                print("Generating shareable links...")
            else:
                print("\nNo subslist.xlsx file found. Please create one and try again.")
                exit()
            
            subs_excel_file = pd.read_excel("C:/Users/User/OneDrive/Documents/OneDrive-Bot/msgraph/subslist.xlsx")
            subs_name = subs_excel_file['Name'].values
            
            for sub_name in subs_name:
                search_response = drive_items_services.search_folder(sub_name)
                
                folder_name = search_response['value'][0]['name']
                if folder_name == sub_name:
                    item_id = search_response['value'][0]['id']
                    
                    create_response = drive_items_services.create_sl(
                        item_id=item_id,
                        request_body={
                            "type": "view",
                            "scope": "anonymous"
                        }
                    )
                    
                    print(create_response['link']['webUrl'])
        else:
            print('Invalid choice!\n')
    except ODataError as odata_error:
        print('Error:')
        if odata_error.error:
            print(odata_error.error.code, odata_error.error.message)
            

