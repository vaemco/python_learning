class Dataset:
    def __init__(self, data):
        self.data = data

    def get_info(self):
        print(f"Das Dataset hat {len(self.data)} Einträge.")

my_data = Dataset([10, 20, 30])
my_data.get_info()
