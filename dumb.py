import pandas as pd
import numpy as np
import math
import argparse
from datetime import datetime
import sys
import time
import multiprocessing
from multiprocessing import Process, Pipe

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_data(d):
    data2_x = d['x']
    data2_y = d['y']
    data2_z = d['z']

    return { 'x': data2_x, 'y': data2_y, 'z': data2_z, "R": d['R'], "G": d['G'], "B": d['B'] }

def print_progress(progress, time_elapsed):
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write("[%-100s] %.2f%%" % ('=' * int(progress), progress))
    sys.stdout.write(" Time elapsed: ")
    sys.stdout.write(str(time_elapsed))
    sys.stdout.flush()

def process(data1, data2, z_threshold, i, output_filename, names, original_now, conn):
    # Prepare for main loop
    data1_unique_x = data1.x.unique()
    data2_unique_x = data2.x.unique()
    data2_unique_y = data2.y.unique()

    # Main loop in sub progress
    result = []

    cnt = 0
    # The first two outer loops are used to iterate thru referenced point set
    for x1 in data1_unique_x:
        data1_x_columns = data1.loc[data1["x"] == x1]
        
        for index, data1_x_col in data1_x_columns.iterrows():
            data1_x = data1_x_col['x']
            data1_y = data1_x_col['y']
            data1_z = data1_x_col['z']

            # Filter out target points
            temp = data2.loc[abs(data2["x"] - x1) < 0.05]
            temp = temp.loc[abs(temp["y"] - data1_y) < 0.05]
            
            for index, d in temp.iterrows():
                data2_x = d['x']
                data2_y = d['y']
                data2_z = d['z']
                
                # Check conditions on filtered points
                if distance(data1_x, data1_y, data2_x, data2_y) < 0.05 and data1_z - data2_z > z_threshold:
                    result.append({ 'x': data2_x, 'y': data2_y, 'z': data2_z, 'R': d['R'], 'G': d['G'], 'B': d['B'] })
            cnt += 1
        
            if cnt % 1000 == 0:
                now = datetime.now()
                print('\nProcess of Thread ' + str(i), 'Total: ' + str(data1.shape[0]), 'Processed: ' + str(cnt), 'Time Elapsed: ' + str(now - original_now))


    print("\nOutputing for Thread " + str(i) + "...\n")
    output = open(output_filename + str(i), "w+")

    for r in result:
        output.write(''.join('{0' + '[' + names[i] + ']} ' for i in range(len(r))).format(r) + '\n')
    output.close()
    conn.send(True)

def main():
    # Config input first - Parse options
    completed = 0

    # Positional Options
    parser = argparse.ArgumentParser(description='在两期点云数据中，找到两期点云中相对应的点，并选出高差大于某个阈值的点，输出成 x, y, z, R, G, B 格式的文件')
    parser.add_argument('ref_data_filename', metavar='ref_data_filename', type=str, nargs='+', help='包含用于参照的点云的文件名')
    parser.add_argument('target_data_filename', metavar='target_data_filename', type=str, nargs='+', help='包含目标点云的文件名')
    parser.add_argument('output_filename', metavar='output_filename', type=str, nargs='+', help='输出文件的文件名')

    # Optional options
    parser.add_argument('--data_columns', dest='names', type=str, default='xyzRGB', help='两个输入文件中，列的名字，需要输入一个数组。默认是 \'xyzRGB\'')
    parser.add_argument('--data_sep', dest='data_sep', type=str, default=' ', help='两个输入文件中，列与列之间的分隔符，默认是 \' \'')
    parser.add_argument('--sort_by', dest='sort_by', type=str, default='xy', help='对输入文件的点云进行排序的依据, 默认是 \'xy\', 即根据 x 和 y 的值做排序')
    parser.add_argument('--z_threshold', dest='z_threshold', type=int, default=1, help='两期数据比较时，筛选高差的阈值, 默认是 1')
    parser.add_argument('--thread_cnt', dest='cpu_count', type=int, default=multiprocessing.cpu_count(), help='使用多少个进程来做运算, 默认会使用机子允许的最大数量')

    # Parse and init
    args = parser.parse_args()
    ref_data_filename = args.ref_data_filename[0]
    target_data_filename = args.target_data_filename[0]
    output_filename = args.output_filename[0]
    names = [ch for ch in args.names]
    data_sep = args.data_sep
    sort_by = [ch for ch in args.sort_by]
    z_threshold = args.z_threshold
    cpu_count = args.cpu_count

    print("Using " + str(cpu_count) + "threads for this task")

    # Get cpu count
    cpu_count = multiprocessing.cpu_count()

    # Read data
    print("Reading data...\n")
    data1 = pd.read_csv(ref_data_filename, names=names, sep=data_sep)
    data2 = pd.read_csv(target_data_filename, names=names, sep=data_sep)
    # Always make a copy
    data2_cp = data2.copy()

    # Drop duplicates and sort
    print("Sorting...\n")
    data1 = data1.drop_duplicates(keep=False)
    sorted_data1 = data1.sort_values(sort_by)
    data2_cp = data2_cp.drop_duplicates(keep=False)
    sorted_data2_cp = data2_cp.sort_values(sort_by)

    splitted_data1 = np.array_split(sorted_data1, cpu_count)

    original_now = datetime.now()
            
    print("Processing...\n")
    processes = []
    parent_conn_list = []
    for i in range(cpu_count):
        parent_conn, child_conn = Pipe()
        p = Process(target=process, args=(splitted_data1[i], sorted_data2_cp, z_threshold, i, output_filename, names, original_now, child_conn,))
        p.start()
        parent_conn_list.append(parent_conn)

        processes.append(p)


    while completed < cpu_count:
        for i in range(cpu_count):
            try:
                parent_conn = parent_conn_list[i]
                res = parent_conn.recv()
            except:
                res = False

            if res:
                processes[i].terminate()
                completed += 1
        
        time.sleep(1)
        
    # Stitch result from different threads and store it to `output_filename`
    frames = []

    for i in range(cpu_count):
        data = pd.read_csv(output_filename + str(i), names=names, sep=data_sep)
        frames.append(data)

    result = pd.concat(frames)
    result.to_csv(output_filename, header=None, index=None, sep=data_sep, mode='a')
    # if cnt > 1000:
    #     break

main()