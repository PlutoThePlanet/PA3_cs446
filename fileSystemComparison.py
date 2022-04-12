# fileSystemComparison.py
# Paige Mortensen
# CS 446 PA3 - compare and contrast single level file directories with hierarchical file directories

# QUESTIONS
# discuss any similarities/dissimilarities in the printed output between singleLevelFiles.txt and hierarchicalFiles.txt
# explain the reason these differences or similarities exist

# We have a simple file system that only supports a single-level architecture. Files can have arbitrarily long names and
# the root directory can have an arbitrary number of files. How could we implement something similar to a hierarchical
# file system? (hint, think about approximating a path)

# You may import the glob, numpy, sys, pandas, and/or os libraries
import os
import sys
import shutil


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
    for elem in range(1, 101):                                      # loop through dirs and move files
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
        fp = open(os.path.join('./singleRoot', 'singleLevelFiles.txt'), 'w')
        # print(sum(os.path.getsize(os.path.join(root, name)) for name in files), end=" ")
        # print("bytes in", len(files), "non-directory files")
        fp.close()

    # save the size of all the files and the names that you find into a list
    # write each filename and its size to a text file in the associated root
    # print the number of files in each txt file (singleLevelFiles and hierarchicalFiles) to the screen
    # print the average size of each file to the screen
        # Due to my oversight when writing this assignment, I will accept average file sizes that contain directories;
        # OR you can report the average directory size separately from average file size. Either will do.


def traverse_hierarchical():
    hierarchical = []
    for root, dirs, files in os.walk('./hierarchicalRoot'):
        fp = open(os.path.join('./hierarchicalRoot', 'hierarchicalFiles.txt'), 'w')
        # note: hierarchicalFiles.txt should contain the size of each directory as part of its contents
        fp.close()


def comp_traversal_time(root): # pass in root to traverse
    time = 0
    if root == './hierarchicalRoot':
        # start
        traverse_hierarchical()
        # stop
        # time = stop - start
    elif root == './singleRoot':
        # start
        traverse_single()
        # stop
        # time = stop - start
    return time

    #     Import or include a time library that allows you to track how long it takes to get all of the data about files in
    #     singleLevelFiles, and how long it takes to get all of the data about files and directories in hierarchicalFiles.
    #     Whatever library you import should be capable of doing this in milliseconds. Print the total traversal time to the
    #     screen after you've printed the number of files and average size (do not print the time it takes to traverse
    #     individual directories).


def main():
    single_root = './hierarchicalRoot'
    hierarchical_root = './singleRoot'

    single_level_dir()
    # hierarchical_level_dir()
    # comp_traversal_time(single_root)
    # comp_traversal_time(hierarchical_root)

    # calculate the number of files in the singleLevel directory
    # calculate the average size of the files in the singleLevel directory
    # calculate the execution time to descend from root and gather all file names/sizes
    # print each value

    # Repeat the same exercise for hierarchical, including the subdirectory names and sizes

if __name__ == "__main__":
    main()
