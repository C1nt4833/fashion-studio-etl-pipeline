import unittest
import pandas as pd
import numpy as np
from utils.transform import transform_data

class TestTransform(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            {
                "Title": "T-shirt 2", 
                "Price": "$100.00", 
                "Rating": "3.9 / 5", 
                "Colors": "3 Colors", 
                "Size": "Size: M", 
                "Gender": "Gender: Men"
            },
            {
                "Title": "Unknown Product",
                "Price": "Price Unavailable", 
                "Rating": "Invalid Rating / 5", 
                "Colors": "0 Colors", 
                "Size": "Size: S", 
                "Gender": "Gender: Unisex"
            }
        ]

    def test_transform_cleaning(self):
        df = transform_data(self.raw_data)
    
        self.assertNotIn("Unknown Product", df['Title'].values)
       
        self.assertEqual(df.iloc[0]['Price'], 1600000.0)
        
        self.assertEqual(df.iloc[0]['Size'], "M")
        self.assertEqual(df.iloc[0]['Gender'], "Men")
        
        self.assertIsInstance(df.iloc[0]['Rating'], float)
        
        self.assertTrue(isinstance(df.iloc[0]['Colors'], (int, float, np.integer)), 
                        f"Expected int/float/np.integer, got {type(df.iloc[0]['Colors'])}")

if __name__ == '__main__':
    unittest.main()