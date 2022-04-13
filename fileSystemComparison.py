# fileSystemComparison.py
# Paige Mortensen
# CS 446 PA3 - compare and contrast single level file directories with hierarchical file directories

# QUESTIONS
# discuss any similarities/dissimilarities in the printed output between singleLevelFiles.txt and hierarchicalFiles.txt
# explain the reason these differences or similarities exist

# We have a simple file system that only supports a single-level architecture. Files can have arbitrarily long names and
# the root directory can have an arbitrary number of files. How could we implement something similar to a hierarchical
# file system? (hint, think about approximating a path)


import os
import sys
import shutil
from time import perf_counter
# import pandas


def single_level_dir():
    path = './singleRoot'
    try:
        os.mkdir(path)
        for elem in range(1, 101):
            file_name = 'file' + str(elem) + '.txt'
            fp = open(os.path.join(path, file_name), 'x')
            fp.close()
    except OSError:
        print('your files already exist')
        sys.exit(1)

def hierarchical_level_dir():
    i = 1
    path = './hierarchicalRoot'
    try:
        os.mkdir(path)
        for elem in range(1, 11):                                       # create dirs
            dir_name = 'files' + str(i) + '-' + str(i + 9)
            i += 10
            os.makedirs(os.path.join(path, dir_name))
        for elem in range(1, 101):                                      # create files
            file_name = 'file' + str(elem) + '.txt'
            fp = open(os.path.join(path, file_name), 'x')
            fp.close()
    except OSError:
        print('your files already exist')
        sys.exit(1)
    for elem in range(1, 101):                                          # loop through dirs and move files
        filename = 'file' + str(elem) + '.txt'
        if elem <= 10:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files1-10')
        elif elem <= 20:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files11-20')
        elif elem <= 30:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files21-30')
        elif elem <= 40:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files31-40')
        elif elem <= 50:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files41-50')
        elif elem <= 60:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files51-60')
        elif elem <= 70:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files61-70')
        elif elem <= 80:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files71-80')
        elif elem <= 90:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files81-90')
        elif elem <= 100:
            shutil.move(os.path.join(path, filename), './hierarchicalRoot/files91-100')


def traverse_single():
    single = []
    for root, dirs, files in os.walk('./singleRoot'):
        for name in files:
            single += [[os.path.join(root, name), os.path.getsize(os.path.join(root, name))]]
    return single


def traverse_hierarchical():                                                                                                        # hierarchical traverse
    hierarchical = []
    dirs = []

    # sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))
    # dirs = os.listdir('./hierarchicalRoot')
    # print(dirs)

    return hierarchical
        # note: hierarchicalFiles.txt should contain the size of each directory as part of its contents


def comp_traversal_time(root):
    if root == './hierarchicalRoot':
        start = perf_counter()
        data_list_hierarchical = traverse_hierarchical()
        stop = perf_counter()
        total_time = ((stop - start) * 1000)                # calc total time (milliseconds)
                                                                                                                        # set up data to be returned to main
        return total_time
    if root == './singleRoot':
        start = perf_counter()
        data_list_single = traverse_single()
        stop = perf_counter()
        total_time = ((stop - start) * 1000)                # calc total time (milliseconds)                                                                                                               # set up data to be returned to main
        return total_time, data_list_single


def main():
    single_root = './singleRoot'
    single_level_dir()                                      # generate files
    data_list_single = comp_traversal_time(single_root)     # gather files and time it
    run_time_single = data_list_single[0]
    data_single = data_list_single[1]
    file_bytes_single = 0

    fp_single = open(os.path.join('./singleRoot', 'singleLevelFiles.txt'), 'a')
    for i in range (0, len(data_single)):
        fp_single.write(str(data_single[i][0]) + ':\t' + str(data_single[i][1]) + 'bytes\n')
        file_bytes_single += data_single[i][1]
    fp_single.close()
    print('Single level file system')
    print('Number of files: ' + str(len(data_single)))
    print('Average file size: ' + str(file_bytes_single / len(data_single)))
    print('Traversal time: ' + str(float("{0:.4f}".format(run_time_single))))

    # save the size of all the files and the names that you find into a list
    # write each filename and its size to a text file in the associated root
    # print the number of files in each txt file (singleLevelFiles and hierarchicalFiles) to the screen
    # print the average size of each file to the screen
    # Due to my oversight when writing this assignment, I will accept average file sizes that contain directories;
    # OR you can report the average directory size separately from average file size. Either will do.

    # hierarchical_root = './hierarchicalRoot'
    # hierarchical_level_dir()
    # traverse_hierarchical()
    # comp_traversal_time(hierarchical_root)
    # fp_hierarchical = open(os.path.join('./hierarchicalRoot', 'hierarchicalFiles.txt'), 'a')
    # fp_hierarchical.close()

    # calculate the number of files in the singleLevel directory
    # calculate the average size of the files in the singleLevel directory
    # calculate the execution time to descend from root and gather all file names/sizes
    # print each value

    # Repeat the same exercise for hierarchical, including the subdirectory names and sizes

if __name__ == "__main__":
    main()
