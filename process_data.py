import csv
import pprint
CSV_FILEPATH = 'data/Python Developer Test Dataset.csv'


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
            print(self.printable_sorted_rent_result(sorted_list=sorted_list, display_records=display_records))

        return sorted_list

    def filter_by_lease_years(self, num_years):
        filtered_list = [i for i in self.data if i['Lease Years'] == str(num_years)]

        # if self.verbose:
        #   Output the list to the console, including all data fields
        #   Output the total rent for all items in this list to the console

        return filtered_list

    def get_mast_counts(self):
        mast_counts = {}
        for i in self.data:
            if i['Tenant Name'] in mast_counts:
                mast_counts[i['Tenant Name']] += 1
            else:
                mast_counts[i['Tenant Name']] = 1

        if self.verbose:
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(mast_counts)

        return mast_counts

    def printable_sorted_rent_result(self, sorted_list, display_records):
        header_str = ''
        for h in self.headers:
            header_str += h.ljust(50, ' ')

        horizontal_rule = ''.join(['_' for i in range(len(header_str))])

        all_items = ''
        for item in sorted_list[:display_records]:
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

