import configparser
from azure.storage.blob import BlobServiceClient

# Read config.ini file
config = configparser.ConfigParser()
config.read("config.ini")

# Get credentials from the .ini file
account_name = config["azure_storage"]["account_name"]
account_key = config["azure_storage"]["account_key"]

# Create BlobServiceClient
blob_service_client = BlobServiceClient(
    f"https://{account_name}.blob.core.windows.net", 
    credential=account_key
)

# List containers
print("Containers in storage account:")
for container in blob_service_client.list_containers():
    print(container["name"])
