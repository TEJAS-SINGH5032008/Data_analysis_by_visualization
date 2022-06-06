import csv
import pandas as pd
import ploty.express as px

with open('data.csv,new line = "')as f:
    reader = csv.reader(f)
    file_data = list(reader)

    file_dat.pop(0)
    new_data  =[]
    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(float(n_num))

        n = len(new_data)
        total = 0
        for x in new_data:
            total += x
            mean = total/n_num
            print('mean/average is'+str(mean))
