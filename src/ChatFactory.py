from src.JabberInterface import Chat
class ChatFactory:

    def getJabberChat(self, config):
        chat = Chat(
            config.get('Chat', 'uri'),
            config.get('Chat', 'password'),
            config.get('Chat', 'conference'),
            config.get('Chat', 'nick'))

        chat.register_plugin('xep_0030') # Service Discovery
        chat.register_plugin('xep_0045') # Multi-User Chat
        chat.register_plugin('xep_0199') # XMPP Ping
        #chat.connect()
        #chat.process(threaded=True)
        return chat