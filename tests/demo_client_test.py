from demo_client.demo_client import DemoClient


# noinspection PyMissingTypeHints
class DemoClientTest:
    def test_new_object(self):
        client = DemoClient()

        assert isinstance(client, DemoClient)

    def test_get_json(self):
        json = DemoClient.get_json()

        assert all(isinstance(key, str) for key in json.keys())
