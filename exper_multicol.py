# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd


def work_on_rows(row, ref, sta):
    d = row['A']
    e = ref['B'][2]
    f = sta['C'][0]
    c = {'a': 2}
    return pd.Series([d, e, f])


def main():
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=list('ABC'))
    reference = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=list('ABC'))
    state = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=list('ABC'))

    out = pd.DataFrame()

    out[['D', 'E', 'F']] = df.apply(work_on_rows, axis=1, ref=reference, sta=state)
    print(out)
    return


if __name__ == '__main__':
    main()
    print('main - done')