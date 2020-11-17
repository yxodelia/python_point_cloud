import pandas as pd
import numpy as np
import math
import argparse
from datetime import datetime
import sys
import time
import multiprocessing
from multiprocessing import Process, Pipe
from scipy import spatial

def get_data(d):
    data2_x = d['x']
    data2_y = d['y']
    data2_z = d['z']

    return { 'x': data2_x, 'y': data2_y, 'z': data2_z, "R": d['R'], "G": d['G'], "B": d['B'] }

def process(ref_data, target_data, z_thresholds, output_filename, distance_upper_bound):
    def construct_output_filename(start, end):
        return output_filename + 'from_' + str(start) + "_to_" + str(end) + '.txt'

    # Flattern all values
    ref_data_values = ref_data.values
    target_data_values = target_data.values
    
    # For each spot in target_data, find the closeset point in ref_data
    ref_data_x_y = ref_data.copy()
    target_data_x_y = target_data.copy()
    
    ref_data_x_y = ref_data_x_y.drop(columns=['z', 'R', 'G', 'B'])
    target_data_x_y = target_data_x_y.drop(columns=['z', 'R', 'G', 'B'])
    
    ref_data_x_y_values = ref_data_x_y.values
    target_data_x_y_values = target_data_x_y.values
    
    # BUT, "closeset" should be within a distance upper bound
    kdt = spatial.cKDTree(ref_data_x_y_values)
    data, index = kdt.query(target_data_x_y_values, k=1)
    
    index[data > distance_upper_bound] = -1

    target_data_x_y_values_filtered = target_data_x_y_values[index > -1]
    target_data_filtered = target_data[index > -1]
    kdt = spatial.cKDTree(ref_data_x_y_values)
    data, index = kdt.query(target_data_x_y_values_filtered, k=1)

    selected_ref_data = ref_data.iloc[index]

    # get z_diff between two sets
    z_diff = np.array(target_data_filtered) - np.array(selected_ref_data.values)
    
    # print(len(data2), len(index), len(selected_data1))
    # print(data2, selected_data1)
    
    # print(data2.z, selected_data1.z)

    # print(len(data2))
    
    def output_filtered_result(filtered_indice, start, end):
        filtered = target_data_filtered.iloc[filtered_indice[0].tolist()]
        print('filtered_data - from ' + str(start) + ' to ' + str(end) + ': ', len(filtered))
        filtered.to_csv(construct_output_filename(start, end), header=None, index=None, sep=' ', mode='a')

        return len(filtered)
    
    # Output based on domains
    point_cnt = 0
    for idx, threshold in enumerate(z_thresholds):
        if idx == 0:
            # [-threshold, threshold]
            filtered_indice = np.where(np.logical_and(z_diff[:, 2] <= threshold, z_diff[:, 2] >= -1 * threshold))
            point_cnt += output_filtered_result(filtered_indice, -1 * threshold, threshold)

            # [threshold, next_threshold]
            filtered_indice_positive = np.where(np.logical_and(z_diff[:, 2] > threshold, z_diff[:, 2] <= z_thresholds[idx + 1]))
            point_cnt += output_filtered_result(filtered_indice_positive, threshold, z_thresholds[idx + 1])

            # [-next_threshold, -threshold]
            filtered_indice_negative = np.where(np.logical_and(z_diff[:, 2] < -1 * threshold, z_diff[:, 2] >= -1 * z_thresholds[idx + 1]))
            point_cnt += output_filtered_result(filtered_indice_negative, -1 * z_thresholds[idx + 1], -1 * threshold)
        elif idx < len(z_thresholds) - 1:
            # [threshold, next_threshold]
            filtered_indice_positive = np.where(np.logical_and(z_diff[:, 2] > threshold, z_diff[:, 2] <= z_thresholds[idx + 1]))
            point_cnt += output_filtered_result(filtered_indice_positive, threshold, z_thresholds[idx + 1])

            # [-next_threshold, -threshold]
            filtered_indice_negative = np.where(np.logical_and(z_diff[:, 2] < -1 * threshold, z_diff[:, 2] >= -1 * z_thresholds[idx + 1]))
            point_cnt += output_filtered_result(filtered_indice_negative, -1 * z_thresholds[idx + 1], -1 * threshold)
        else:
            # [threshold, inf]
            filtered_indice_positive = np.where(z_diff[:, 2] > threshold)
            point_cnt += output_filtered_result(filtered_indice_positive, threshold, 'inf')

            # [-inf, threshold]
            filtered_indice_negative = np.where(z_diff[:, 2] < -1 * threshold)
            point_cnt += output_filtered_result(filtered_indice_negative, '-inf', -1 * threshold)
    
    assert point_cnt == len(target_data_filtered)

    print('总点数: ' + str(len(target_data)))
    print('符合平面阈值的点: ' + str(len(target_data_filtered)))

def main():
    # Positional Options
    parser = argparse.ArgumentParser(description='在两期点云数据中，找到两期点云中相对应的点，并选出高差大于某个阈值的点，输出成 x, y, z, R, G, B 格式的文件')
    parser.add_argument('ref_data_filename', metavar='ref_data_filename', type=str, nargs='+', help='包含用于参照的点云的文件名')
    parser.add_argument('target_data_filename', metavar='target_data_filename', type=str, nargs='+', help='包含目标点云的文件名')
    parser.add_argument('output_filename', metavar='output_filename', type=str, nargs='+', help='输出文件的文件名')

    # Optional options
    parser.add_argument('--data_columns', dest='names', type=str, default='xyzRGB', help='两个输入文件中，列的名字，需要输入一个数组。默认是 \'xyzRGB\'')
    parser.add_argument('--data_sep', dest='data_sep', type=str, default=' ', help='两个输入文件中，列与列之间的分隔符，默认是 \' \'')
    parser.add_argument('--sort_by', dest='sort_by', type=str, default='xy', help='对输入文件的点云进行排序的依据, 默认是 \'xy\', 即根据 x 和 y 的值做排序')
    parser.add_argument('--z_thresholds', dest='z_thresholds', type=str, default="1", help='两期数据比较时，筛选高差的阈值区间, 需要是一个数组，如 \'0.2, 0.5\', 默认是 1')
    parser.add_argument('--distance_upper_bound', dest='distance_upper_bound', type=float, default=0.5, help='平面距离阈值，用于过滤两期之间没有重叠的点')

    # Parse and init
    args = parser.parse_args()
    ref_data_filename = args.ref_data_filename[0]
    target_data_filename = args.target_data_filename[0]
    output_filename = args.output_filename[0]
    names = [ch for ch in args.names]
    data_sep = args.data_sep
    sort_by = [ch for ch in args.sort_by]
    z_thresholds = [float(num) for num in args.z_thresholds.split(',')]
    distance_upper_bound = args.distance_upper_bound

    # Read data
    print("Reading data...\n")
    data1 = pd.read_csv(ref_data_filename, names=names, sep=data_sep)
    data2 = pd.read_csv(target_data_filename, names=names, sep=data_sep)
    # Drop duplicates
    data1 = data1.drop_duplicates(keep=False)
    data2 = data2.drop_duplicates(keep=False)

            
    print("Processing...\n")
    original_now = datetime.now()
    process(data1, data2, z_thresholds, output_filename, distance_upper_bound)
    print("Total time: ", datetime.now() - original_now)
main()