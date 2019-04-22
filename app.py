import csv
import sys
import multiprocessing
from datetime import datetime as dt
import io
import time
import numpy as np
import random


def worker(data_for_worker):
    print('worker started sleeping for', data_for_worker)
    time.sleep(random.randint(1, int(data_for_worker[0])))
    return data_for_worker


def hendler(data=None):
    if data is None:
        data = []
        for x in range(500):
            data.append(str(random.randint(1, 60)))
    count = 0
    dates = []
    docs = 10
    overall = dt.now()
    print('time started ============================>', overall)
    for i in range(0, len(data), docs):  #
        now = dt.now()
        pool = multiprocessing.Pool(processes=4)
        pool_outputs = pool.map(worker, data[i:i + docs])
        pool.close()
        pool.join()
        dates.append(dt.now() - now)
        mean = np.mean(dates)
        print(count, 'predict end time by mean iteration time:', overall + (len(data) / docs) * mean)
        count += 1
        # we can store pool_outputs
        # path = 'DELETE.csv'
        # for ii in pool_outputs:
        #     with io.open(path, 'a', encoding='utf-8') as myfile:
        #         wr = csv.writer(myfile, delimiter=';')
        #         wr.writerow(ii)
    return



if __name__ == '__main__':
    c = 0
    data = []
    # with io.open('.csv', 'rt') as csvfile:
    #     readCSV = csv.reader(csvfile, delimiter=',')
    #     for i in readCSV:
    #         data.append(i[1])
    hendler()
