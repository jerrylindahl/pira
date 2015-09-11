from src.JabberInterface import Chat
from src.SlackChat import SlackChat

class ChatFactory:
    def getChat(self, config):
        client = config.get('Chat', 'client')
        if client == 'Slack':
            return self.getSlackChat(config)
        elif client == 'Jabber':
            return self.getJabberChat(config)

    def getJabberChat(self, config):
        chat = Chat(
            config.get('Chat', 'uri'),
            config.get('Chat', 'password'),
            config.get('Chat', 'conference'),
            config.get('Chat', 'nick'))

        chat.register_plugin('xep_0030') # Service Discovery
        chat.register_plugin('xep_0045') # Multi-User Chat
        chat.register_plugin('xep_0199') # XMPP Ping
        return chat

    def getSlackChat(self, config):
        chat = SlackChat(config)


        return chat