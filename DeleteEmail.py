from dotenv import load_dotenv
load_dotenv()

from nylas import APIClient
import os
import sys

nylas = APIClient(
	os.environ.get('CLIENT_ID'),
	os.environ.get('CLIENT_SECRET'),
	os.environ.get('ACCESS_TOKEN')
)

messageId = "<MESSAGE_ID>"
labelsDict = {}
labels = nylas.labels.all()
for label in labels:
	labelsDict[label["name"]] = label["id"] 

try:
	message = nylas.messages.get(messageId)
	message.add_label(labelsDict["trash"])
	message.save()
	print(f"Your message was succesfully deleted")
except:
	print(f"An {sys.exc_info()[0]} error ocurred. \nMessage was not found.")
