import signal
import time

import configparser

from src.ChatFactory import ChatFactory
from src.ChatRouter import ChatRouter


class Main():
    def __init__(self):
        self.chat = None
        self.config = None

        self.sig_int = False

    def receive_signal(self, signum, _):
        if signum == signal.SIGINT:
            self.shutdown()
        else:
            print('Unknown signal', signum)
            signal.getsignal()

    def main(self):
        signal.signal(signal.SIGINT, self.receive_signal)

        self.config = self.get_config('pira.cfg')

        self.init_chat()
        chat_router = ChatRouter(self.chat, self.config)
        chat_router.run()

        self.main_loop()
        self.shutdown()

    def main_loop(self):
        while not self.sig_int:
            time.sleep(1)
        exit(0)

    def shutdown(self):
        print('Shutting down.')
        self.chat.disconnect()
        self.sig_int = True

    def init_chat(self):
        cf = ChatFactory()
        self.chat = cf.getJabberChat(self.config)

    def get_config(self, file):
        config = configparser.RawConfigParser()
        config.read(file)
        return config


if __name__ == "__main__":
    main = Main()
    main.main()