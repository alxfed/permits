# -*- coding: utf-8 -*-
"""https://jsonlines.readthedocs.io/en/latest/
"""
import jsonlines


def main():
    with jsonlines.open('./inspections_file.jl') as reader:
        for permit in reader:
            print('permit')
    return


if __name__ == '__main__':
    main()
    print('main - done')