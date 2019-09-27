# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    total = 22
    per_page = 15
    current_page = 1
    last_page = 3
    message_list = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,3, 3, 3, 3, 3, 3, 3, 3, 3,3, 3, 3, 3, 4]
    if total > 0:
        # deal with a message_list
        for page in range(2, last_page + 1):
            print(page)
    return


if __name__ == '__main__':
    main()
    print('main - done')