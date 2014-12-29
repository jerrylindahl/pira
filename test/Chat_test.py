import unittest
from unittest.mock import Mock

from src.JabberInterface import Chat


class ChatTest(unittest.TestCase):
    def setUp(self):
        self.chat = Chat('test@test.com', 'password', 'room@server', 'pirabot')

    def test_init(self):
        self.assertEqual(self.chat.room, 'room@server')

    def test_message_recieve(self):
        mock = Mock()
        self.chat.callBack = mock

        self.chat.muc_message({"mucnick": "someoneelse", "body": "pirabot: Hi!"})

        mock.msg_rec.assert_called_with("someoneelse", "pirabot: Hi!")

if __name__ == '__main__':
    unittest.main()