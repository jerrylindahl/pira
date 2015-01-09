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
        
        bare_mock = Mock()
        bare_mock.bare = "room"
        self.chat.muc_message({"from": bare_mock, "mucnick": "someoneelse", "body": "pirabot: Hi!"})
        
        mock.msg_rec.assert_called_with("room", "someoneelse", "pirabot: Hi!")

if __name__ == '__main__':
    unittest.main()