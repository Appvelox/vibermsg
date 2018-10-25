class Location(object):
    def __init__(self, lat: float, lon: float):
        if not isinstance(lat, float):
            raise TypeError('lat must be an instance of float')
        if not isinstance(lon, float):
            raise TypeError('lon must be an instance of float')
        self.lat = lat
        self.lon = lon


class Sender(object):
    def __init__(self, id: str, name: str, avatar: str, country: str, language: str):
        if not isinstance(id, str):
            raise TypeError('id must be an instance of str')
        if not isinstance(name, str):
            raise TypeError('name must be an instance of str')
        if not isinstance(avatar, str):
            raise TypeError('avatar must be an instance of str')
        if not isinstance(country, str):
            raise TypeError('country must be an instance of str')
        if not isinstance(language, str):
            raise TypeError('language must be an instance of str')
        self.id = id
        self.name = name
        self.avatar = avatar
        self.country = country
        self.language = language


class IncomingMessage(object):
    pass


class IncomingTextMessage(IncomingMessage):
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        self.text = text


class Request(object):
    def __init__(self, sender: Sender, message_token: int):
        if not isinstance(sender, Sender):
            raise TypeError('sender must be an instance of Sender')
        if not isinstance(message_token, int):
            raise TypeError('message_token must be an instance of int')
        self.sender = sender
        self.message_token = message_token


class TextMessageRequest(Request):
    def __init__(self, sender: Sender, message: IncomingTextMessage, message_token: int):
        if not isinstance(message, IncomingTextMessage):
            raise TypeError('message must be an instance of IncomingTextMessage')
        self.message = message
        super(TextMessageRequest, self).__init__(sender, message_token)


class ConversationStartedRequest(Request):
    def __init__(self, sender: Sender, message_token: int):
        super(ConversationStartedRequest, self).__init__(sender, message_token)
