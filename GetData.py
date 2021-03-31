import csv
import numpy as np

"import pandas as pd"


def get_data():
    sample_data = np.array([0, 0, 0])
    with open('GBPEURdata.csv', 'r') as file:
        csv_reader = csv.reader(file)
        print(csv_reader)
        line_count = 0
        for line in csv_reader:
            if line_count == 0:
                line_count = line_count + 1
                print(line)
            else:
                print(line)
                concat_data = np.array([line[0], line[1], line[5]])
                sample_data = np.vstack((sample_data, concat_data))
    print(sample_data)
    return sample_data


def get_daily_data():
    sample_data = np.array([0, 0, 0])
    with open('dailyData.csv', 'r') as file:
        csv_reader = csv.reader(file)
        #print(csv_reader)
        line_count = 0
        for line in csv_reader:
            if line_count == 0:
                line_count = line_count + 1
               # print(line)
            else:
                #print(line)
                concat_data = np.array([line[0], line[1], line[5]])
                sample_data = np.vstack((sample_data, concat_data))
    (sample_data)
    return sample_data


get_daily_data()
get_data()
