'''
This script presuppose the Sigmorphon 2020 shared task 0 data is stored in the directory task0-data/

e.g.
$ python fairseqFormat.py eng

It will turn all English train, dev, (test if there is test data) into the format Fairseq requires,
and store the reformatted data in the current directory.
'''
import sys
import os

def reformat(fname, finputname, foutputname):
    with open(fname) as f, \
        open(finputname, 'w') as finput, \
        open(foutputname, 'w') as foutput:
        for line in f:
            lemma, form, msd = line.strip().split('\t')
            input = [letter for letter in lemma] + [tag for tag in msd.split(';')]
            output = [letter for letter in form]
            finput.write(' '.join(input) + '\n')
            foutput.write(' '.join(output) + '\n')

if __name__ == '__main__':
    lang = sys.argv[1]  # language code of 3 letters for Sigmorphon 2020 shared task0


    train = 'task0-data/' + lang + '.trn'
    trainin = 'train.' + lang + '.input'
    trainout = 'train.' + lang + '.output'

    if os.path.exists(train):
        reformat(train, trainin, trainout)

    dev = 'task0-data/' + lang + '.dev'
    devin = 'dev.' + lang + '.input'
    devout = 'dev.' + lang + '.output'
    if os.path.exists(dev):
        reformat(dev, devin, devout)

    test = 'task0-data/' + lang + '.test'
    testin = 'test.' + lang + '.input'
    testout = 'test.' + lang + '.output'
    if os.path.exists(test):
        reformat(test, testin, testout)



