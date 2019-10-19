# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import numpy as np


def main():
    output_file = '/media/alxfed/toca/presentation/hierarchy_index.csv'
    data = pd.Series(np.random.randn(9),
                     index = [['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                              [1, 2, 3, 1, 3, 1, 2, 2, 3]])
    frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                         index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                         columns = [['Ohio', 'Ohio', 'Colorado'],
                                    ['Green', 'Red', 'Green']])
    print(frame)
    frame.to_csv(output_file)
    return


if __name__ == '__main__':
    main()
    print('main - done')