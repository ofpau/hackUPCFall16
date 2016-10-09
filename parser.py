import io
import os
import csv
import pickle

data_path = "../hackupc_fall/data_export_cobercat/"

# "data_export_1-2015"
for i, file in enumerate(os.listdir(data_path)):
    if file.endswith(".csv"):
        month_year = file.split("_")[2].split(".")[0]
        data = []
        print "%d: loading %s..." % (i, month_year)

        with open(data_path + file, "rb") as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                row_data = {}
                #row_data["timestamp"] = row["timestamp"]
                row_data["lat"] = row["lat"]
                row_data["lng"] = row["lng"]
                row_data["fullCarrier"] = row["fullCarrier"]
                row_data["signal_avg"] = row["signal_avg"]
                row_data["net_type"] = row["net_type"]
                row_data["speed"] = row["speed"]
                row_data["sat"] = row["satellites"]
                row_data["act"] = row["activity"]
                data.append(row_data)
            picklefile = io.open('./data/' + month_year, 'wb')
            print "file open"
            pickle.dump(data, picklefile)
            picklefile.close()
            print "file closed"

        print "done"

#jsonfile = open("data.json", "w")
#json.dump(data, jsonfile)
#jsonfile.write("\n")
