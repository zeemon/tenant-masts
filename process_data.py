import csv
CSV_FILEPATH = 'data/Python Developer Test Dataset.csv'
NUM_RECORDS = 5


class ProcessData:

    def __init__(self, csv_filepath=CSV_FILEPATH):
        self.csv_data, self.csv_headers = self.get_csv_data(csv_filepath)

    @staticmethod
    def get_csv_data(csv_filepath):
        csv_data, csv_headers = [], []
        with open(csv_filepath) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            csv_data = [row for row in csv_reader]
            csv_headers = csv_reader.fieldnames

        return csv_data, csv_headers

    def sort_by_current_rent(self, num_records=NUM_RECORDS, reverse=False):
        sorted_list = sorted(self.csv_data, key=lambda x: x['Current Rent'], reverse=reverse)
        header_str = ''
        for h in self.csv_headers:
            header_str += h.ljust(50, ' ')

        horizontal_rule = ''.join(['_' for i in range(len(header_str))])

        all_items = ''
        for item in sorted_list[:num_records]:
            item_str = '\n'
            for i in item.values():
                item_str += i.ljust(50, ' ')
            all_items += item_str

        result_str = f"{horizontal_rule}\n{header_str}\n{horizontal_rule}" \
                     f"{all_items}" \
                     f"\n{horizontal_rule}"

        print(result_str)
        return result_str


p = ProcessData()
p.sort_by_current_rent(num_records=5)

