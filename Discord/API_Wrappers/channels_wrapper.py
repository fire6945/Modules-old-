import requests

class Channel:

    def __init__(self):
        self.payload = {}
        self.headers = {}
        self.json = {}
        self.Authentication = None
        self.base_url = "https://discord.com/api/v8/channels/"

    def initialize_data(payload=None, headers=None, json=None, Authenication=None):
        self.payload = payload
        self.headers = headers
        self.json = json
        self.Authentication = Authentication
    
    def send_message(self, channel_id, message, msg_type):
        pass
