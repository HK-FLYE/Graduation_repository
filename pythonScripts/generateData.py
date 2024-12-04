import numpy as np
import os

if __name__ == '__main__':

    num_count = 1000
    column1 = np.random.rand(num_count) * 3 + 25
    column2 = np.random.rand(num_count) * 5 + 20

    fileName = "C:\\Users\\HKFLYE\\Desktop\\data.tsv"

    with open(fileName, 'w') as file:
        file.write('first\tsecond\n')

        for data1, data2 in zip(column1, column2):
            file.write(f"{data1}\t{data2}\n")

    print(f"保存完成")
