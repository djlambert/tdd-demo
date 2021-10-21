from typing import Any, Dict, Text

import requests


class DemoClient:

    def get_json(self) -> Dict[Text, Any]:
        response = requests.get('https://httpbin.org/json')

        return response.json()
