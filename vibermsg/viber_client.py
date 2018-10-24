import requests
import json


class ViberClient(object):
    _viber_bot_api_url = 'https://chatapi.viber.com/pa'

    def __init__(self, token: str):
        if not isinstance(token, str):
            raise TypeError('token must be an instance of str')
        self.token = token

    def set_webhook(self, url: str, send_name: bool = False, send_photo: bool = False, event_types: list = None):
        if not isinstance(url, str):
            raise TypeError('url must be an instance of str')
        if not isinstance(send_name, bool):
            raise TypeError('send_name must be an instance of bool')
        if not isinstance(send_photo, bool):
            raise TypeError('send_photo must be an instance of bool')
        payload = {'url': url, 'send_name': send_name, 'send_photo': send_photo}
        if event_types is not None:
            if not isinstance(event_types, list):
                raise TypeError('event_types must be an instance of list')
            payload['event_types'] = event_types
        self.post_request('set_webhook', json.dumps(payload))

    def post_request(self, endpoint: str, data: str):
        if not isinstance(endpoint, str):
            raise TypeError('endpoint must be an instance of str')
        if not isinstance(data, str):
            raise TypeError('data must be an instance of str')
        headers = requests.utils.default_headers()
        headers['X-Viber-Auth-Token'] = self.token
        response = requests.post(f'{self._viber_bot_api_url}/{endpoint}', data=data, headers=headers)
        response.raise_for_status()
        return json.loads(response.text)
