# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def main():
    df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
    df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
    df = df.append(df2, ignore_index=True)
    print(df)
    return


if __name__ == '__main__':
    main()
    print('main - done')