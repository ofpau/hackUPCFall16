import io
import os
import csv
import pickle

data_path = "../hackupc_fall/data_export_cobercat/"

# "data_export_1-2015"
data = {}
i = 0
for file in os.listdir(data_path):
    if file.endswith(".csv"):
        month_year = file.split("_")[2].split(".")[0]
        data[month_year] = []

        print "loading %s..." % month_year

        with open(data_path + file, "rb") as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                row_data = {}
                row_data["timestamp"] = row["timestamp"]
                row_data["lat"] = row["lat"]
                row_data["lng"] = row["lng"]
                row_data["fullCarrier"] = row["fullCarrier"]
                row_data["net_type"] = row["net_type"]
                data[month_year].append(row_data)
        print "done"

picklefile = io.open('./data', 'wb')
print "file open"
pickle.dump(data, picklefile)
picklefile.close()
print "file closed"
#jsonfile = open("data.json", "w")
#json.dump(data, jsonfile)
#jsonfile.write("\n")
