import pytest

from vibermsg.models.keyboards import Button, Keyboard
from vibermsg.models.messages import TextMessage
from vibermsg.models.requests import (TextMessageRequest, IncomingTextMessage, Sender, ConversationStartedRequest, Location)


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
        pass