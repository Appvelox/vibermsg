from .keyboards import Keyboard


class Message(object):
    def to_dict(self):
        pass


class TextMessage(Message):
    def __init__(self, text: str, keyboard: Keyboard = None):
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        self.text = text
        if keyboard is not None:
            if not isinstance(keyboard, Keyboard):
                raise TypeError('keyboard must be an instance of Keyboard')
        self.keyboard = keyboard

    def to_dict(self):
        result = {
            'type': 'text',
            'text': self.text
        }
        if self.keyboard:
            result['keyboard'] = self.keyboard.to_dict()
        return result
