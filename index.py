import os
from SI import helpers

helpers.assert_dir('/home/leandro/PycharmProjects/untitled/SI/docs/')
helpers.assert_dir('/home/leandro/PycharmProjects/untitled/SI/data')

helpers.index('/home/leandro/PycharmProjects/untitled/SI/docs', '/home/leandro/PycharmProjects/untitled/SI/data')
print('Index done.')
