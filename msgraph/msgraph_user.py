from msgraph_session import GraphSession


class User():

    """
    ## Overview:
    ----
    You can use Microsoft Graph to build compelling app experiences
    based on users, their relationships with other users and groups,
    and their mail, calendar, and files.
    """

    def __init__(self, session: object) -> None:
        """Initializes the `Users` object.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft Graph Client.
        """

        # Set the session.
        self.graph_session: GraphSession = session

        # Set the endpoint.
        self.endpoint = "me"

    def greet_user(self) -> dict:
        """Retrieve the signed in user.

        ### Returns
        ----
        dict :
            If successful, this method returns a 200 OK response code
            and user object in the response body.
        """

        content = self.graph_session.make_request(
            method="get",
            endpoint=self.endpoint
        )

        print("Hello, ", content['displayName'])
        print("Email: ", content['mail'], "\n")