import pytest

from vibermsg.models.keyboards import Button, Keyboard
from vibermsg.models.messages import TextMessage
from vibermsg.models.requests import (Sender, Location, ConversationStartedRequest, TextMessageRequest, IncomingTextMessage)


class TestKeybooards:
    def test_Button(self):
        button = Button('test', 'test')
        with pytest.raises(TypeError):
            Button(1, 'test', '', 1, 1, '', '', 1, '', '')
        with pytest.raises(TypeError):
            Button('test', 1, '', 1, 1, '', '', 1, '', '')
        with pytest.raises(TypeError):
            Button('test', 'test', 1, 1, 1, '', '', 1, '', '')
        with pytest.raises(TypeError):
            Button('test', 'test', '', '', 1, '', '', 1, '', '')
        with pytest.raises(TypeError):
            Button('test', 'test', '', 1, '', '', '', 1, '', '')
        with pytest.raises(TypeError):
            Button('test', 'test', '', 1, 1, 1, '', 1, '', '')
        with pytest.raises(TypeError):
            Button('test', 'test', '', 1, 1, '', 1, 1, '', '')
        with pytest.raises(TypeError):
            Button('test', 'test', '', 1, 1, '', '', '', '', '')
        with pytest.raises(TypeError):
            Button('test', 'test', '', 1, 1, '', '', 1, 1, '')
        with pytest.raises(TypeError):
            Button('test', 'test', '', 1, 1, '', '', 1, '', 1)
        assert button.to_dict() == {
            'Columns': 6,
            'Rows': 1,
            'BgColor': '#ffffff',
            'ActionType': 'reply',
            'ActionBody': 'test',
            'Text': 'test',
            'TextVAlign': 'middle',
            'TextHAlign': 'center',
            'TextOpacity': 100,
            'TextSize': 'regular'
        }

    def test_Keyboard(self):
        button = Button('test', 'test')
        keyboard = Keyboard([button])
        keyboard.add(button)
        with pytest.raises(TypeError):
            Keyboard(1)
        with pytest.raises(TypeError):
            Keyboard(['1'])
        with pytest.raises(TypeError):
            Keyboard(default_height=1)
        with pytest.raises(TypeError):
            Keyboard(bgcolor=1)
        with pytest.raises(TypeError):
            keyboard.add(1)
        assert keyboard.to_dict() == {
            'Type': 'keyboard',
            'DefaultHeight': False,
            'BgColor': '#dcdcdc',
            'Buttons': [
                {
                    'Columns': 6,
                    'Rows': 1,
                    'BgColor': '#ffffff',
                    'ActionType': 'reply',
                    'ActionBody': 'test',
                    'Text': 'test',
                    'TextVAlign': 'middle',
                    'TextHAlign': 'center',
                    'TextOpacity': 100,
                    'TextSize': 'regular'
                },
                {
                    'Columns': 6,
                    'Rows': 1,
                    'BgColor': '#ffffff',
                    'ActionType': 'reply',
                    'ActionBody': 'test',
                    'Text': 'test',
                    'TextVAlign': 'middle',
                    'TextHAlign': 'center',
                    'TextOpacity': 100,
                    'TextSize': 'regular'
                }
            ]
        }


class TestMessages:
    def test_TextMessage(self):
        button = Button('test', 'test')
        keyboard = Keyboard([button])
        message = TextMessage('test', keyboard)
        with pytest.raises(TypeError):
            TextMessage(1)
        with pytest.raises(TypeError):
            TextMessage('test', [])
        assert message.to_dict() == {
            'type': 'text',
            'text': 'test',
            'keyboard': {
                'Type': 'keyboard',
                'DefaultHeight': False,
                'BgColor': '#dcdcdc',
                'Buttons': [
                    {
                        'Columns': 6,
                        'Rows': 1,
                        'BgColor': '#ffffff',
                        'ActionType': 'reply',
                        'ActionBody': 'test',
                        'Text': 'test',
                        'TextVAlign': 'middle',
                        'TextHAlign': 'center',
                        'TextOpacity': 100,
                        'TextSize': 'regular'
                    }
                ]
            }
        }


class TestRequests:
    def test_Location(self):
        Location(1.2, 1.1)
        with pytest.raises(TypeError):
            Location('', 1.1)
        with pytest.raises(TypeError):
            Location(1.2, '')

    def test_Sender(self):
        Sender(**{
            "id": "01234567890A=",
            "name": "John McClane",
            "avatar": "http://avatar.example.com",
            "country": "UK",
            "language": "en",
            "api_version": 1
        })
        with pytest.raises(TypeError):
            Sender(**{
                "id": 1,
                "name": "John McClane",
                "avatar": "http://avatar.example.com",
                "country": "UK",
                "language": "en",
                "api_version": 1
            })
        with pytest.raises(TypeError):
            Sender(**{
                "id": "01234567890A=",
                "name": 1,
                "avatar": "http://avatar.example.com",
                "country": "UK",
                "language": "en",
                "api_version": 1
            })
        with pytest.raises(TypeError):
            Sender(**{
                "id": "01234567890A=",
                "name": "John McClane",
                "avatar": 1,
                "country": "UK",
                "language": "en",
                "api_version": 1
            })
        with pytest.raises(TypeError):
            Sender(**{
                "id": "01234567890A=",
                "name": "John McClane",
                "avatar": "http://avatar.example.com",
                "country": 1,
                "language": "en",
                "api_version": 1
            })
        with pytest.raises(TypeError):
            Sender(**{
                "id": "01234567890A=",
                "name": "John McClane",
                "avatar": "http://avatar.example.com",
                "country": "UK",
                "language": 1,
                "api_version": 1
            })

    def test_ConversationStartedRequest(self):
        sender = Sender(**{
            "id": "01234567890A=",
            "name": "John McClane",
            "avatar": "http://avatar.example.com",
            "country": "UK",
            "language": "en",
            "api_version": 1
        })

        ConversationStartedRequest(sender, 1)
        with pytest.raises(TypeError):
            ConversationStartedRequest(1, 1)
        with pytest.raises(TypeError):
            ConversationStartedRequest(sender, '')

    def test_IncomingTextMessage(self):
        IncomingTextMessage('test')
        with pytest.raises(TypeError):
            IncomingTextMessage(1)

    def test_TextMessageRequest(self):
        message = IncomingTextMessage('')
        sender = Sender(**{
            "id": "01234567890A=",
            "name": "John McClane",
            "avatar": "http://avatar.example.com",
            "country": "UK",
            "language": "en",
            "api_version": 1
        })
        TextMessageRequest(sender, message, 1)
        with pytest.raises(TypeError):
            TextMessageRequest(sender, 1, 1)
