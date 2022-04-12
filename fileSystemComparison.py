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


def single_level_dir():
    path = './singleRoot'
    os.mkdir(path)
    for elem in range(1, 101):
        file_name = 'file' + str(elem) + '.txt'
        fp = open(os.path.join(path, file_name), 'x')
        fp.close()


def hierarchical_level_dir():
    path = './hierarchicalRoot'
    os.mkdir(path)
    for elem in range(1, 11):
        dir_name = 'files' + str(elem) + '-' + str(elem+9)
        os.makedirs(os.path.join(path, dir_name))
    for elem in range(1, 101):
        file_name = 'file' + str(elem) + '.txt'
        fp = open(os.path.join(path, file_name), 'x')
        fp.close()

    # move files to the appropriate directory after generating the directories


def comp_size_diff():
    print()
    #     Starting from your new root directories (singleRoot and hierarchicalRoot), write a program that starts at the
    #     root, and then descends the file tree (if it can) from the root.
    #         For both singleLevel and hierarchical, save the size of all the files and the names that you find into a data
    #         structure (if python, I suggest a list or dict). Write each filename and its size to a text file in the
    #         associated root. Name it singleLevelFiles.txt and hierarchicalFiles.txt, respectively.
    #             hierarchicalFiles.txt should contain the size of each directory as part of its contents (single level
    #             doesn't need this, because single level doesn't use other directories)
    #     Print the number of files in each txt file (singleLevelFiles and hierarchicalFiles) to the screen
    #     Print the average size of each file to the screen
    #         Due to my oversight when writing this assignment, I will accept average file sizes that contain directories;
    #         OR you can report the average directory size separately from average file size. Either will do.


def comp_traversal_time_diff():
    print()
    #     Import or include a time library that allows you to track how long it takes to get all of the data about files in
    #     singleLevelFiles, and how long it takes to get all of the data about files and directories in hierarchicalFiles.
    #     Whatever library you import should be capable of doing this in milliseconds. Print the total traversal time to the
    #     screen after you've printed the number of files and average size (do not print the time it takes to traverse
    #     individual directories).


def main():
    single_level_dir()
    hierarchical_level_dir()
    # In summary, you will have code to generate your singleLevel directory. You will generate 100 files within that
    # directory. You will calculate the number of files in the singleLevel directory. You will calculate the average
    # size of the files in the singleLevel directory. You will calculate the execution time to descend from root and
    # gather all file names/sizes. Print each value in that order. Repeat the same exercise for hierarchical, including
    # the subdirectory names and sizes.

if __name__ == "__main__":
    main()
