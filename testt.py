import csv
def get_length(file_path):
    with open("data.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        #print(reader_list)
        return len(reader_list)
print(get_length("data.csv"))