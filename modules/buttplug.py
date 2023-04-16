import logging
import sys
import asyncio

from buttplug import Client, WebsocketConnector, ProtocolSpec

# =========================== Buttplug Module =============================
# Just a simple class to handle the buttplug connection
# In the future, this will be expanded to handle multiple devices 
# and provide a description of the device to the ai so it 
# can control them individually
# =========================================================================


class ButtPlugModule():

    def __init__(self, value=0):
        self.vibrator = value  # 0 = off, can range from 0 to 100
        self.client = Client("Tavern AI Client", ProtocolSpec.v3)
        self.connector = WebsocketConnector(
            "ws://127.0.0.1:12345", logger=self.client.logger)

    def connect(self):
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.client.connect(self.connector))
            print("Connected to server")
        except Exception as e:
            logging.error(f"Could not connect to server, exiting: {e}")
        return

    # set the vibration level of the buttplug

    def set(self, value):
        print("Vibrator set to: " + str(value))
        self.vibrator = value
        if len(self.client.devices) != 0: 
            device = self.client.devices[0]
            loop = asyncio.new_event_loop()
            if value == 0:
                loop.run_until_complete(device.stop())
            else:
                loop.run_until_complete(device.vibrate(value))
                

    def get(self):
        return self.vibrator
    
# dummy class for when buttplug is not installed on the system. useful for testing
class ButtPlugDummyModule():
    def __init__(self, value=0):
        self.vibrator = value  # 0 = off, can range from 0 to 100
      

    def connect(self):
        pass
    # set the vibration level of the buttplug

    def set(self, value):
        self.vibrator = value
        print("Vibrator set to: " + str(value))
       
    def get(self):
        return self.vibrator
    
