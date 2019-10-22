# -*- coding: utf-8 -*-
"""...
"""
import recordlinkage
from recordlinkage.datasets import load_febrl4


def main():
    dfA, dfB = load_febrl4()
    indexer = recordlinkage.Index()
    indexer.full()
    pairs = indexer.index(dfA, dfB)
    return


if __name__ == '__main__':
    main()
    print('main - done')