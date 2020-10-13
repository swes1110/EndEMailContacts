import sys  # For simplicity, we'll read config file from 1st CLI param sys.argv[1]
import json
import logging
import requests


# Optional logging
logging.basicConfig(level=logging.WARNING)

config = json.load(open(sys.argv[1]))

authPayload = {"accessKeyId" : config['accessKeyId'], "accessKeySecret" : config['accessKeySecret']}

logging.info("Sending authentication request to NiC")
logging.info(authPayload)
authRequest = requests.post(
    "https://na1.nice-incontact.com/authentication/v1/token/access-key",
    json=authPayload
)

logging.info("Response:")
logging.info(authRequest.content)

logging.info("Converting response to json for parsing")
jsonifiedAuth = json.loads((authRequest.content).decode("utf-8"))

logging.info("Get current active contacts")
activeContacts = requests.get(
    "https://api-na1.niceincontact.com/incontactapi/services/v17.0/contacts/active",
    headers={'Authorization': 'Bearer ' + jsonifiedAuth['id_token']}
)

