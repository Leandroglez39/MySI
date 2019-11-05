import os
from SI import helpers

def index(path):
    helpers.assert_dir(path)
    helpers.assert_dir('./data')

    helpers.index(path, './data')
    print('Index done.')
