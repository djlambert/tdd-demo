from demo_client.demo_client import DemoClient


# noinspection PyMissingTypeHints
class DemoClientTest:
    def test_new_object(self):
        client = DemoClient()

        assert isinstance(client, DemoClient)
