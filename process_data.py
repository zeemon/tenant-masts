import csv
from datetime import datetime
import pprint
CSV_FILEPATH = 'data/Python Developer Test Dataset.csv'
pp = pprint.PrettyPrinter(indent=4)

class ProcessData:

    def __init__(self, csv_filepath=CSV_FILEPATH, verbose=False):
        self.verbose = verbose
        self.data, self.headers = self.get_csv_data(csv_filepath)

    @staticmethod
    def get_csv_data(csv_filepath):
        data, headers = [], []
        with open(csv_filepath) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
            headers = csv_reader.fieldnames

        return data, headers

    def sort_by_current_rent(self, display_records=None, reverse=False):
        sorted_list = sorted(self.data, key=lambda x: x['Current Rent'], reverse=reverse)

        if self.verbose:
            print("Top 5 results sorted by Current Rent \n")
            print(self.printable_result(display_list=sorted_list, display_records=display_records))

        return sorted_list

    def filter_by_lease_years(self, num_years):
        filtered_list = [i for i in self.data if i['Lease Years'] == str(num_years)]

        if self.verbose:
            print(f"\n\nList filtered by lease years: {num_years} years")
            print(self.printable_result(display_list=filtered_list))
            print(f"\n\nRents of records filtered by {num_years} years of lease")
            print('\n'.join([i['Current Rent'] for i in filtered_list]))

        return filtered_list

    def get_mast_counts(self):
        mast_counts = {}
        for i in self.data:
            if i['Tenant Name'] in mast_counts:
                mast_counts[i['Tenant Name']] += 1
            else:
                mast_counts[i['Tenant Name']] = 1

        if self.verbose:
            print("\nDictionary containing tenant name and a count of masts for each tenant")
            pp.pprint(mast_counts)

        return mast_counts

    def filter_by_lease_start_date(self, start_date_from, start_date_to):
        start_date_from_obj = start_date_to_obj = None
        if start_date_from:
            start_date_from_obj = datetime.strptime(start_date_from, '%d/%m/%Y')
        if start_date_to:
            start_date_to_obj = datetime.strptime(start_date_to, '%d/%m/%Y')

        filtered_data = []
        for record in self.data:
            lease_from = datetime.strptime(record['Lease Start Date'], '%d %b %Y')
            if start_date_from_obj <= lease_from <= start_date_to_obj:
                filtered_data.append(record)

        if self.verbose:
            print("\n\nList the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007")
            print(self.printable_result(display_list=filtered_data))

        return filtered_data

    def printable_result(self, display_list, display_records=None):
        header_str = ''
        for h in self.headers:
            header_str += h.ljust(50, ' ')

        horizontal_rule = ''.join(['_' for i in range(len(header_str))])

        all_items = ''
        for item in display_list[:display_records]:
            item_str = '\n'
            for i in item.values():
                item_str += i.ljust(50, ' ')
            all_items += item_str

        result_str = f"{horizontal_rule}\n{header_str}\n{horizontal_rule}" \
                     f"{all_items}" \
                     f"\n{horizontal_rule}"
        return result_str


if __name__ == '__main__':
    p = ProcessData(verbose=True)
    p.sort_by_current_rent(display_records=5)
    p.filter_by_lease_years(num_years=25)
    p.get_mast_counts()
    p.filter_by_lease_start_date(start_date_from="01/06/1999", start_date_to="31/08/2007")

