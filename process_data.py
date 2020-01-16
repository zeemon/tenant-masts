import csv
CSV_FILEPATH = 'data/Python Developer Test Dataset.csv'
DISPLAY_RECORDS = 5


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

    def sort_by_current_rent(self, display_records=DISPLAY_RECORDS, reverse=False):
        sorted_list = sorted(self.data, key=lambda x: x['Current Rent'], reverse=reverse)

        if self.verbose:
            print(self.printable_sorted_rent_result(sorted_list=sorted_list, display_records=display_records))

        return sorted_list

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
