__all__ = ['constants', 'companies', 'contacts', 'associations']

from .constants import *
from . import companies, contacts, associations


def main():
    print('main in hubspot.__init__.py: ok')
    return


if __name__ == '__main__':
    main()
