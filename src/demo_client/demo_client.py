from typing import Any, Dict, Text

import requests


class DemoClient:
    @staticmethod
    def get_json() -> Dict[Text, Any]:
        response = requests.get('https://httpbin.org/json')

        return response.json()

    def get_text(self) -> Text:
        response = requests.get('https://httpbin.org/json')

        return response.text
