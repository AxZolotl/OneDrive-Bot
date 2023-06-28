from configparser import ConfigParser

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section("graph_api")

# Set the Values.
config.set("graph_api", "client_id", "e141a6f5-0ddd-4824-9ff0-440ee57cde89")
config.set("graph_api", "client_secret", "_1W8Q~404NRMmpb-dh7PQFA3ru1ZD1mvDTHRKaRz")
config.set("graph_api", "redirect_uri", "https://localhost:8000/getToken")

# Write the file.
with open(file="configs/config.ini", mode="w+", encoding="utf-8") as f:
    config.write(f)