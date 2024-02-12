import os
import csv
import sys
import shutil


def create_directory(folder1, folder2):
    """create 2 folders to put your files inside"""
    try:
        os.mkdir(folder1)
        os.mkdir(folder2)
        return folder1, folder2
    except FileExistsError:
        print('dir already exist')

def create_files(file_csv):
    """return 2 files in format: txt, csv or xlsx"""
    with open (file_csv, 'w') as wr:
        field_name = ['first_name', 'last_name']
        writer = csv.DictWriter(wr, fieldnames=field_name)
    return writer


def open_files(file:str):
    """open the 2 files created"""
    pass

def compare_files(file:str):
    """compare the 2 files content """
    pass


def move_file(file:str):
    """move the content from file1 to file2"""
    pass


if __name__ == "__main__":
    path = input('enter your path: ')
    dir1 = os.path.join(path, 'dir1')
    dir2 = os.path.join(path, 'dir2')
    file_csv = 'file.csv'
    print(create_directory(dir1, dir2))
    print(create_files(file_csv))