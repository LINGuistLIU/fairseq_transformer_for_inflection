'''
This script transforms the best predictions from the best model back to the task0 data format.

$ python pred2task0Format.py 3LETTER-LANGUAGE-CODE
'''
import sys
import os

lang = sys.argv[1]
type = sys.argv[2] # dev or test

outputdir = 'predictions/'
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

with open('checkpoints/'+lang+'-predictions/'+type+'-checkpoint_best.pt.txt') as fpred, \
    open('task0-data/'+lang+'.'+type) as finput, \
    open(outputdir+lang+'.'+type+'.output', 'w') as fw:
    id2pred = {}
    for line in fpred:
        if line[:2] == 'H-':
            id, score, pred = line.strip().split('\t')
            id = int(id.split('-')[1])
            id2pred[id] = pred.replace(' ', '').replace('_', ' ')
    inputlines = [line.strip() for line in finput]
    for i, line in enumerate(inputlines):
        lines = line.strip().split('\t')
        if len(lines) == 3 or len(lines) == 2:
            lemma = lines[0]
            msd = lines[-1]
        else:
            print('Please make sure each line in your file is a tab separated 3-column entry.')
        fw.write('\t'.join([lemma, id2pred[i], msd]) + '\n')



