import os
from google.cloud import translate_v2 as translates


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./wrenchtech-198715-054f1f5b9ea5.json"


class TranslateAddress:
    def __init__(self):
        self.client = translates.Client()

    def send_request(self):
        # result = self.client.translate(["Улица Победы", "Киев", "Голосеевский район", "12 в"], target_language="uk")
        result = self.client.translate(None, target_language="uk")
        print(result)


TranslateAddress().send_request()
