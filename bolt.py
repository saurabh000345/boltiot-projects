from boltiot import Bolt
import json
import config

class BoltDeviceUnreachableException(Exception):
    pass

class BoltDevice(Bolt):
    def __init__(self):
        self.API_KEY = config.API_KEY
        self.DEVICE_ID = config.DEVICE_ID
        super(BoltDevice, self).__init__(self.API_KEY, self.DEVICE_ID)
        response = json.loads(self.isOnline())
        if response['success']:
            print(f"Successfully established comms with device {self.DEVICE_ID}")
        else:
            print(f"There was an error connecting to device {self.DEVICE_ID}\nValue: {response['value']}")
            raise BoltDeviceUnreachableException("Failed to connect to device")
