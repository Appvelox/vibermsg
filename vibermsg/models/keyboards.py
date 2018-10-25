class Button(object):
    def __init__(self, text: str, action_body: str, bg_сolor: str = '#ffffff', rows: int = 1, columns: int = 6,
                 action_type: str = 'reply', text_size: str = 'regular', textopacity: int = 100,
                 textvalign: str = 'middle', texthalign='center'):
        if not isinstance(action_body, str):
            raise TypeError('action_body must be an instance of str')
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        if not isinstance(columns, int):
            raise TypeError('columns must be an instance of int')
        if not isinstance(rows, int):
            raise TypeError('rows must be an instance of int')
        if not isinstance(bg_сolor, str):
            raise TypeError('bgColor must be an instance of str')
        if not isinstance(action_type, str):
            raise TypeError('action_type must be an instance of str')
        if not isinstance(textopacity, int):
            raise TypeError('textopacity must be an instance of int')
        if not isinstance(text_size, str):
            raise TypeError('text_size must be an instance of str')
        if not isinstance(textvalign, str):
            raise TypeError('textvalign must be an instance of str')
        if not isinstance(texthalign, str):
            raise TypeError('texthalign must be an instance of str')
        self.columns = columns
        self.rows = rows
        self.bg_color = bg_сolor
        self.action_type = action_type
        self.action_body = action_body
        self.text = text
        self.textvalign = textvalign
        self.texthalign = texthalign
        self.textopacity = textopacity
        self.text_size = text_size

    def to_dict(self):
        return {
            'Columns': self.columns,
            'Rows': self.rows,
            'BgColor': self.bg_color,
            'ActionType': self.action_type,
            'ActionBody': self.action_body,
            'Text': self.text,
            'TextVAlign': self.textvalign,
            'TextHAlign': self.texthalign,
            'TextOpacity': self.textopacity,
            'TextSize': self.text_size
        }


class Keyboard(object):
    def __init__(self, buttons: list = None, default_height: bool = False, bgcolor: str = '#dcdcdc'):
        self.buttons = []
        if buttons is not None:
            if not isinstance(buttons, list):
                raise TypeError('buttons must be an instance of list')
            for button in buttons:
                if not isinstance(button, Button):
                    raise TypeError('buttons items must be an instance of Button')
            self.buttons = buttons
        if not isinstance(default_height, bool):
            raise TypeError('default_height must be an instance of bool')
        if not isinstance(bgcolor, str):
            raise TypeError('bgcolor must be an instance of str')
        self.default_height = default_height
        self.bgcolor = bgcolor

    def add(self, button: Button):
        if not isinstance(button, Button):
            raise TypeError('event_types must be an instance of Button')

    def to_dict(self):
        return {
            'Type': 'keyboard',
            'DefaultHeight': self.default_height,
            'BgColor': self.bgcolor,
            'Buttons': [button.to_dict() for button in self.buttons]
        }
