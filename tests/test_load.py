import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
from utils.load import load_to_csv, load_to_postgresql, load_to_google_sheets

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame([{
            'Title': 'Test Product',
            'Price': 160000.0,
            'timestamp': '2026-02-21T12:00:00'
        }])

    @patch('pandas.DataFrame.to_csv')
    def test_load_to_csv(self, mock_to_csv):
        load_to_csv(self.df, "test.csv")
        mock_to_csv.assert_called_once()

    @patch('utils.load.create_engine')
    def test_load_to_postgresql(self, mock_engine):
        mock_engine.return_value = MagicMock()
        
        db_config = {
            'user': 'postgres', 'password': 'pw', 
            'host': '127.0.0.1', 'port': '5432', 'database': 'db'
        }
        
        with patch('pandas.DataFrame.to_sql'):
            load_to_postgresql(self.df, db_config)
            
        mock_engine.assert_called_once()

    @patch('utils.load.Credentials')
    @patch('utils.load.gspread')
    def test_load_to_google_sheets(self, mock_gspread, mock_creds):
        mock_client = MagicMock()
        mock_gspread.authorize.return_value = mock_client
        mock_sh = MagicMock()
        mock_client.open.return_value = mock_sh
        mock_sh.get_worksheet.return_value = MagicMock()
        
        load_to_google_sheets(self.df, "Test Sheet", "fake_key.json")
        
        mock_gspread.authorize.assert_called_once()

if __name__ == '__main__':
    unittest.main()