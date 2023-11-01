# Import dependencies
from nylas import Client
from dotenv import load_dotenv
import os
from nylas.models.messages import ListMessagesQueryParams

# Load our .env file
load_dotenv()

# Initialize Nylas client
nylas = Client(
    api_key = os.environ.get("V3_API_KEY")
)

message_id = "<YOUR_MESSAGE_ID>"

# Read emails
request_id = nylas.messages.destroy(os.environ.get("GRANT_ID"), message_id, {})

if request_id != None:
	print("Email deleted succesfully")
else:
	print("The email couldn't be deleted")
