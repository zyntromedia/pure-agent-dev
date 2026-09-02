# app/providers/byteplus/client.py
import os

class BytePlusClient:
    def __init__(self):
        self.api_key = os.getenv("BYTEPLUS_API_KEY")
        self.endpoint = os.getenv("BYTEPLUS_ENDPOINT")

    def get_credentials(self):
        return {"api_key": self.api_key, "endpoint": self.endpoint}
