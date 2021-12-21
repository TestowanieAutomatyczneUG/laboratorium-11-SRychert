import unittest
from unittest.mock import mock_open, patch, Mock, create_autospec
from App import App


class TestApp(unittest.TestCase):
    def setUp(self):
        self.temp = App()

    def test_read(self):
        fake_open = mock_open(read_data="important\ndata\nhere")
        with fake_open('/fake/file/path.txt', 'r') as f:
            self.assertEqual(self.temp.read_all_lines(f), "important\ndata\nhere")

    def test_count_lines(self):
        file_content_mock = """Data
        Yes this is a data
        A data in a file
        Data
        And another data"""
        fake_file_path = '/fake/file/path.txt'

        with patch('App.open'.format(__name__),
                   new=mock_open(read_data=file_content_mock)) as mocked_file:
            actual = self.temp.count_lines(fake_file_path)
            mocked_file.assert_called_once_with(fake_file_path, 'r')

            expected = len(file_content_mock.split('\n'))
            self.assertEqual(expected, actual)

    def test_add_phrase(self):
        fake_file_path = "/fake/file/path.txt"
        content = "Message to write on file to be written"
        with patch('App.open', mock_open()) as mocked_file:
            self.temp.add_phrase(fake_file_path, content)

            # assert if opened file on write mode 'a'
            mocked_file.assert_called_once_with(fake_file_path, 'a')

            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file
            mocked_file().write.assert_called_once_with("\n"+content)

    def test_delete(self):
        y = create_autospec(self.temp)
        fake_file_path = "/fake/file/path.txt"
        y.delete(fake_file_path)
        y.delete.assert_called_once_with(fake_file_path)

    def tearDown(self) -> None:
        self.temp = None
