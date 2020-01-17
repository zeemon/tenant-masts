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

    def test_get_mast_counts(self):
        mast_counts = self.p.get_mast_counts()
        self.assertEqual(mast_counts['Everything Everywhere Ltd&Hutchison 3G UK Ltd'], 8)

    def test_filter_by_lease_start(self):
        filtered_data = self.p.filter_by_lease_start_date(start_date_from="01/06/1999", start_date_to="31/08/2007")
        self.assertTrue(len(filtered_data),5)


if __name__ == '__main__':
    unittest.main()
