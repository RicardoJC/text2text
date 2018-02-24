# Simple program to change text's encoding
__author__ = "RicardoJC"
__version__ = "0.1"
__maintainer__ = "RicardoJC"
__email__ = "ricardoj.epc@gmail.com"
__status__ = "Debug"

from os import listdir, getcwd, mkdir
from os.path import isfile
import os
from exceptions import OSError
import codecs

'''
Variables
'''
FILE_EXTENSION = '.txt'
ENCODING_ORIGIN_FILES = 'macroman'
ENCODING_DESTINATION_FILES = 'utf-8'
DIRECTORY_NAME = 'files'

files = []

def main():
    for f in listdir(getcwd()):
        if f.endswith(FILE_EXTENSION):
            files.append(f)
    try:
        mkdir(DIRECTORY_NAME)
        for f in files:
            with codecs.open(f,'r',encoding=ENCODING_ORIGIN_FILES) as o:
                with codecs.open(DIRECTORY_NAME + '/' +f,'a+',encoding=ENCODING_DESTINATION_FILES) as d:
                    d.write(o.read())
    except OSError:
        print 'Error'


if __name__ == '__main__':
    main()
