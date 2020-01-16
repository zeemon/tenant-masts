import unittest
from process_data import ProcessData


class TestSum(unittest.TestCase):

    def setUp(self):
        self.p = ProcessData()

    def test_sort_by_current_rent(self):
        sorted_data = self.p.sort_by_current_rent()
        rent_values = [i['Current Rent'] for i in sorted_data]
        self.assertEqual(rent_values, sorted(rent_values))


if __name__ == '__main__':
    unittest.main()
