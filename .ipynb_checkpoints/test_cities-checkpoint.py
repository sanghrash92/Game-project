import unittest
from city_functions import get_formatted_city_country

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        """testing city and country work."""
        formatted_city = get_formatted_city_country('kathmandu', 'nepal')
        self.assertEqual(formatted_city, 'Kathmandu, Nepal')
        
    def test_city_country_population(self):
        """Does city, name and population work."""
        formatted_city = get_formatted_city_country('kathmandu', 'nepal', 100000)
        self.assertEqual(formatted_city, 'Kathmandu, Nepal, 100000')
        
if __name__ == '__main__':
    unittest.main()