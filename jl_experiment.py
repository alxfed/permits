# -*- coding: utf-8 -*-
"""https://jsonlines.readthedocs.io/en/latest/
"""
import jsonlines


def main():
    with jsonlines.open('./perm_and_insp_file.jl') as reader:
        for line in reader:
            address = line['full_address']
            ranaddr = line['range_address']
            permits = line['perm_table']
            inspect = line['insp_table']
            print(line)
    return


if __name__ == '__main__':
    main()
    print('main - done')