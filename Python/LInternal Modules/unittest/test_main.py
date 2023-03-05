import unittest
from unittest.mock import patch, MagicMock
import requests.exceptions
from requests import Timeout, HTTPError
from main import len_todo, get_todo


class TestTodo(unittest.TestCase):
    @patch("main.get_todo")
    def test_len_todo(self, mock_get_todo: MagicMock):
        mock_get_todo.return_value = "one"
        self.assertEqual(len_todo(), 3)

    @patch("main.requests")
    def test_get_todo(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"title": "Hello World"}

        mock_requests.get.return_value = mock_response
        self.assertEqual(get_todo(), "Hello World")

    @patch("main.requests")
    def test_get_todo_timeout(self, mock_requests: MagicMock):

        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effect = Timeout(
            "Seems that the server is down.")

        self.assertEqual(get_todo(), "No todos")

    @patch("main.requests")
    def test_get_todo_raise_for_status(self, mock_requests: MagicMock):

        mock_requests.exceptions = requests.exceptions

        mock_response = MagicMock(status_code=403)
        mock_response.raise_for_status.side_effect = HTTPError(
            "Something goes wrong")

        mock_requests.get.return_value = mock_response
        self.assertEqual(get_todo(), "HTTPError was raise")


if __name__ == "__main__":
    unittest.main()
