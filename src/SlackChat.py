import time
import datetime
from slackclient import SlackClient


class SlackChat:
    def __init__(self, config):
        self.config = config
        self.interrupt = False
        self.token = config.get('Slack', 'token')

        self.sc = SlackClient(self.token)
        self.hasRemindedToday = False
        self.callBack = None

    def run(self):
        self.sc.rtm_connect()

        while not self.interrupt:
            message = self.sc.rtm_read()
            print(message)
            if len(message) != 0:
                if 'type' in message[0] and 'user' in message[0]:
                    if message[0]['type'] == "message":
                        self.callBack.msg_rec(message[0]['channel'], message[0]['user'], message[0]['text'])

            d = datetime.datetime.now()
            if str(d.isoweekday()) == self.config.get('Reminder', 'day'):
                if str(d.hour) == self.config.get('Reminder', 'hour') and not self.hasRemindedToday:
                    self.send_message(
                        self.config.get('Reminder', 'channel'),
                        '',
                        '',
                        mhtml=self.config.get('Reminder', 'message'))

                    self.hasRemindedToday = True
            else:
                self.hasRemindedToday = False

            time.sleep(1)

    def send_message(self, mto, mbody, mtype, mhtml=""):
        self.sc.rtm_send_message(mto, mhtml)

    def disconnect(self):
        self.interrupt = True

