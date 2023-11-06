import what_is_year_now
import unittest
from unittest.mock import patch
import urllib
from io import BytesIO
import json


class TestWhatIsYearNow(unittest.TestCase):
    @patch.object(urllib.request, 'urlopen')
    def test_yyyymmdd_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value = BytesIO(
            json.dumps({'currentDateTime': '2023-11-01'}).encode()
            )
        year = what_is_year_now.what_is_year_now()
        self.assertEqual(year, 2023)

    @patch.object(urllib.request, 'urlopen')
    def test_ddmmyyyy_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value = BytesIO(
            json.dumps({'currentDateTime': '01.11.2023'}).encode()
            )
        year = what_is_year_now.what_is_year_now()
        self.assertEqual(year, 2023)

    @patch.object(urllib.request, 'urlopen')
    def test_incorrect_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value = BytesIO(
            json.dumps({'currentDateTime': '01-11-2023'}).encode()
            )
        with self.assertRaises(ValueError) as e:
            what_is_year_now.what_is_year_now()
        self.assertEqual(str(e.exception), 'Invalid format')


if __name__ == '__main__':
    unittest.main()
