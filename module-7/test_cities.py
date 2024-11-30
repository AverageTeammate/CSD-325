# import the function from city_functions.py
import unittest
from city_functions import city_country  # Import the function to test

class TestCityCountryFunction(unittest.TestCase):
    
    def test_city_country(self):
        """Test the city_country function."""
        
        # Test with population and language
        result = city_country('Santiago', 'Chile', 5000000, 'Spanish')
        self.assertEqual(result, 'Santiago, Chile - population 5000000, Spanish')  

        # Test with population and language
        result = city_country('Paris', 'France', 2148000, 'French')
        self.assertEqual(result, 'Paris, France - population 2148000, French') 

        # Test with language but no population
        result = city_country('Tokyo', 'Japan', language='Japanese')
        self.assertEqual(result, 'Tokyo, Japan, Japanese')  

        # Test with neither population nor language
        result = city_country('New York', 'USA')
        self.assertEqual(result, 'New York, USA') 

if __name__ == '__main__':
    unittest.main()
