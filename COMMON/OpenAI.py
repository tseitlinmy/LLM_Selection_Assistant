if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), ".."))
        
import sys

from COMMON.base_classes import *
import openai
from openai import AuthenticationError, APIConnectionError

class OpenAI(BaseProvider):
    def __validate_key(api_key: str, val: OutVal) -> bool:
        """
        Validates an OpenAI API key by making a lightweight request to the API.
        """
        # Initialize the client with the provided key
        client = openai.OpenAI(api_key=api_key)
        
        try:
            # Make a simple, free API call to list available models
            client.models.list()
            val.val = "Success: The OpenAI API key is valid."
            return True
            
        except AuthenticationError:
            # This handles 401 Unauthorized errors (invalid key)
            val.val = "Error: The OpenAI API key is invalid or unauthorized."
            return False
            
        except APIConnectionError:
            # This handles network-related issues
            val.val = "Error: Could not connect to the OpenAI API. Check your internet connection."
            return False
            
        except Exception as e:
            # Catch-all for other potential API errors (e.g., rate limits, account suspended)
            val.val = f"An unexpected error occurred: {e}"
            return False
        
        return False

    def __init__(self):
        super().__init__("OpenAI", True)
        self.status = OutVal()

    def validate_api_key(self, api_key):
        return OpenAI.__validate_key(api_key, self.status)

if __name__ == "__main__":
    v = OpenAI()
    v.validate_api_key("your_api_key_here")