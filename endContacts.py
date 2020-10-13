import sys  # For simplicity, we'll read config file from 1st CLI param sys.argv[1]
import json
import logging
import requests


# Optional logging
logging.basicConfig(level=logging.INFO)

# Load configuration file
config = json.load(open(sys.argv[1]))

# Put key/secret into JSON object
authPayload = {"accessKeyId" : config['accessKeyId'], "accessKeySecret" : config['accessKeySecret']}

# Get authentication token from NiC
logging.info("Sending authentication request to NiC")
logging.info(authPayload)
authRequest = requests.post(
    "https://na1.nice-incontact.com/authentication/v1/token/access-key",
    json=authPayload
)

logging.info("Response:")
logging.info(authRequest.content)

# Convert auth response to json for parsing
logging.info("Converting response to json for parsing")
authRequest = json.loads((authRequest.content).decode("utf-8"))

# Use auth token to get list of active contacts
logging.info("Get current active contacts")
activeContacts = requests.get(
    "https://api-na1.niceincontact.com/incontactapi/services/v17.0/contacts/active",
    headers={'Authorization': 'Bearer ' + authRequest['id_token']}
)

# Convert response to json
logging.info("Coverting contact list to JSON")
activeContacts = json.loads((activeContacts.content).decode("utf-8"))
logging.info("The following contacts were retrieved")
logging.info(activeContacts)

for contact in activeContacts:
    if contact["campaignId"] == '2577248':
        print("found e-mail contact:")
        print(contact["contactId"])
    if contact["campaignId"] == '2576991':
        print("found chat contact:")
        print(contact["contactId"])