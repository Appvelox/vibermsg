import pytest
import requests_mock

from vibermsg import ViberClient
from vibermsg.models.messages import TextMessage


@requests_mock.Mocker(kw='mock')
class TestMessengerClient:
    _viber_bot_api_url = 'https://chatapi.viber.com/pa/'

    def test_init(self, **kwargs):
        kwargs['mock'].register_uri('POST', self._viber_bot_api_url + 'get_account_info',
                                    json={'status': 0, 'status_message': '',
                                          'name': 'name', 'icon': 'icon'})
        with pytest.raises(TypeError):
            ViberClient(123)
        c = ViberClient('asda')
        assert c.name == 'name'
        assert c.icon == 'icon'

    def test_set_webhook(self, **kwargs):
        kwargs['mock'].register_uri('POST', self._viber_bot_api_url + 'get_account_info',
                                    json={'status': 0, 'status_message': '',
                                          'name': 'name', 'icon': 'icon'})
        c = ViberClient('asda')
        kwargs['mock'].register_uri('POST', self._viber_bot_api_url + 'set_webhook',
                                    json={'status': 0, 'event_types': ['qqq']})
        assert c.set_webhook('asd') == ['qqq']
        with pytest.raises(TypeError):
            c.set_webhook(1)
        with pytest.raises(TypeError):
            c.set_webhook('asd', send_name=1)
        with pytest.raises(TypeError):
            c.set_webhook('asd', send_photo=1)
        with pytest.raises(TypeError):
            c.set_webhook('asd', event_types=1)

    def test_conversation_started(self, **kwargs):
        kwargs['mock'].register_uri('POST', self._viber_bot_api_url + 'get_account_info',
                                    json={'status': 0, 'status_message': '',
                                          'name': 'name', 'icon': 'icon'})
        c = ViberClient('asda')
        msg = {
            "event": "conversation_started",
            "timestamp": 1457764197627,
            "message_token": 4912661846655238145,
            "type": "open",
            "context": "context information",
            "user": {
                "id": "01234567890A=",
                "name": "John McClane",
                "avatar": "http://avatar.example.com",
                "country": "UK",
                "language": "en",
                "api_version": 1
            },
            "subscribed": False
        }
        with pytest.raises(AttributeError):
            c.process_json(msg)

        @c.register_conversation_started()
        def f(request):
            pass

        c.process_json(msg)

    def test_text_message(self, **kwargs):
        kwargs['mock'].register_uri('POST', self._viber_bot_api_url + 'get_account_info',
                                    json={'status': 0, 'status_message': '',
                                          'name': 'name', 'icon': 'icon'})
        c = ViberClient('asda')
        msg = {
            "event": "message",
            "timestamp": 1457764197627,
            "message_token": 4912661846655238145,
            "sender": {
                "id": "01234567890A=",
                "name": "John McClane",
                "avatar": "http://avatar.example.com",
                "country": "UK",
                "language": "en",
                "api_version": 1
            },
            "message": {
                "type": "text",
                "text": "a message to the service",
                "media": "http://example.com",
                "location": {
                    "lat": 50.76891,
                    "lon": 6.11499
                },
                "tracking_data": "tracking data"
            }
        }
        with pytest.raises(AttributeError):
            c.process_json(msg)

        @c.register_text_message_processor()
        def f(request):
            pass

        c.process_json(msg)
        with pytest.raises(TypeError):
            c.process_json(1)
        with pytest.raises(KeyError):
            c.process_json({})
        with pytest.raises(TypeError):
            c.process_json({'event': 1})
        with pytest.raises(TypeError):
            c.process_json({'event': 1})
        with pytest.raises(Exception):
            msg['message']['type'] = 'aaa'
            c.process_json(msg)

    def test_send_message(self, **kwargs):
        kwargs['mock'].register_uri('POST', self._viber_bot_api_url + 'get_account_info',
                                    json={'status': 0, 'status_message': '',
                                          'name': 'name', 'icon': 'icon'})
        c = ViberClient('asda')
        kwargs['mock'].register_uri('POST', self._viber_bot_api_url + 'send_message',
                                    json={'status': 0})
        message = TextMessage('test')
        c.send_message('111', message)
        with pytest.raises(TypeError):
            c.send_message(1, message)
        with pytest.raises(TypeError):
            c.send_message('111', 1)

    def test_rost_request(self, **kwargs):
        kwargs['mock'].register_uri('POST', self._viber_bot_api_url + 'get_account_info',
                                    json={'status': 0, 'status_message': '',
                                          'name': 'name', 'icon': 'icon'})
        c = ViberClient('asda')
        with pytest.raises(TypeError):
            c.post_request(1, '')
        with pytest.raises(TypeError):
            c.post_request('', 1)
