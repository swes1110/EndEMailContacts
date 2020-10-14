# EndEmailContacts

EndEmailContacts is a simple python script to end all contacts matching a certain "campaignId" in Nice InContact. I developed specifically for e-mail contacts but this would work for any active contacts simply by updating the campaignId in the configuration file.

## Dependencies

Python 3.x

##### The following modules are required

* Requests
```
pip install requests
```

*Listed versions are validated with this application, other's may work but have not been tested*

## Configuration

### NiC Configuration

You will need to generate an accessKey and an accessSecret to utilize the NiC API. For assistance with this please reach out to your NiC support team.

### Configuration File

Rename the configuration file from ParametersSample.json to Parameters.json and fill in the following values
```
"accessKeyId": "{YOUR_ACCESS_KEY_ID}",
"accessKeySecret": "{YOUR_ACCESS_KEY_SECRET}"
"campaignId": "{DESIRED_CAMPAIGNID_TO_END}"
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
GNU General Public License v3.0
