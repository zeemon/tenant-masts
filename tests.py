import unittest
from process_data import ProcessData


class TestSum(unittest.TestCase):

    def setUp(self):
        self.p = ProcessData()

    def test_sort_by_current_rent(self):
        sorted_data = self.p.sort_by_current_rent()
        rent_values = [i['Current Rent'] for i in sorted_data]
        self.assertEqual(rent_values, sorted(rent_values))

    def test_filter_by_lease_years(self):
        num_years = 25
        filtered_data = self.p.filter_by_lease_years(num_years=num_years)
        lease_years = [i['Lease Years'] for i in filtered_data]
        self.assertEqual(set(lease_years), {str(num_years)})


if __name__ == '__main__':
    unittest.main()
