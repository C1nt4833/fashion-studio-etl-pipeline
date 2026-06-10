import unittest
from unittest.mock import patch, MagicMock
from utils.extract import extract_data

class TestExtract(unittest.TestCase):
    @patch('utils.extract.requests.Session')
    def test_extract_success(self, mock_session_class):
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        
        mock_html = """
        <div class="collection-card">
            <div class="product-details">
                <h3 class="product-title">T-shirt Test</h3>
                <span class="price">$20.00</span>
                <p>Rating: 4.5 / 5</p>
                <p>Colors: 2 Colors</p>
                <p>Size: Size: M</p>
                <p>Gender: Gender: Men</p>
            </div>
        </div>
        <div class="collection-card">
            <div class="product-details">
                <h3 class="product-title">Pants 46</h3>
                <p class="price">Price Unavailable</p>
                <p>Rating: Not Rated</p>
            </div>
        </div>
        """
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = mock_html
        
        
        mock_session.get.return_value = mock_response

        result = extract_data(total_pages=1)
      
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
  
        self.assertEqual(result[0]['Title'], "T-shirt Test")
        self.assertEqual(result[0]['Price'], "$20.00")
        
        self.assertEqual(result[1]['Title'], "Pants 46")
        self.assertEqual(result[1]['Price'], "Price Unavailable")
        
       
        self.assertIn('Timestamp', result[0])

if __name__ == '__main__':
    unittest.main()