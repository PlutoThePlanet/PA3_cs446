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


def traverse_hierarchical():
    hierarchical = []

    for root, dirs, files in os.walk('./hierarchicalRoot'):
        for name in dirs:
            print(os.path.join(root, name))
        print('\n')
        for name in files:
            print(os.path.join(root, name))
    return hierarchical
        # note: hierarchicalFiles.txt should contain the size of each directory as part of its contents


def comp_traversal_time(root):
    start = 0
    stop = 0
    data_list = []
    if root == './hierarchicalRoot':
        start = perf_counter()
        data_list = traverse_hierarchical()
        stop = perf_counter()
    if root == './singleRoot':
        start = perf_counter()
        data_list = traverse_single()
        stop = perf_counter()
                                                                                                                                        # print all data to file
    total_time = stop - start
    return total_time * 1000 # milliseconds


def main():
    single_root = './hierarchicalRoot'
    hierarchical_root = './singleRoot'

    single_level_dir()
    comp_traversal_time(single_root)
    fp_single = open(os.path.join('./singleRoot', 'singleLevelFiles.txt'), 'w')
    fp_single.close()

    # save the size of all the files and the names that you find into a list
    # write each filename and its size to a text file in the associated root
    # print the number of files in each txt file (singleLevelFiles and hierarchicalFiles) to the screen
    # print the average size of each file to the screen
    # Due to my oversight when writing this assignment, I will accept average file sizes that contain directories;
    # OR you can report the average directory size separately from average file size. Either will do.

    hierarchical_level_dir()
    traverse_hierarchical()
    comp_traversal_time(hierarchical_root)
    fp_hierarchical = open(os.path.join('./hierarchicalRoot', 'hierarchicalFiles.txt'), 'w')
    fp_hierarchical.close()

    # calculate the number of files in the singleLevel directory
    # calculate the average size of the files in the singleLevel directory
    # calculate the execution time to descend from root and gather all file names/sizes
    # print each value

    # Repeat the same exercise for hierarchical, including the subdirectory names and sizes

if __name__ == "__main__":
    main()
