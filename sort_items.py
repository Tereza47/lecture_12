import csv
import os
import random

cwd_path = os.getcwd()


def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    #row = []
    path = os.path.join(cwd_path,file_name)
    with open(path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')

        for line in reader:
            row = [int(number) for number in line]

        #for line in reader:
        #    for number in line:
        #        number = int(number)
        #        row.append(number)

    return row



def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """


def selection_sort(number_array, direction):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    for index, num in enumerate(number_array):
        extreme_idx = index
        for num_idx, number in enumerate(number_array[index:]):
            if direction == 'ascending':
                if number < number_array[extreme_idx]:
                    extreme_idx = num_idx + index
            elif direction == 'descending':
                if number > number_array[extreme_idx]:
                    extreme_idx = num_idx + index
        number_array[extreme_idx], number_array[index] = number_array[index], number_array[extreme_idx]

    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """


def main():

    # Ukol: Selection Sort
    name = 'numbers_one.CSV'
    my_list = read_row(name)
    print(my_list)
    sorted_list = selection_sort(read_row(name), 'ascending')
    print(sorted_list)
    # Ukol: Selection Sort - se smerem razeni
    

    # Ukol: Bubble Sort


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

