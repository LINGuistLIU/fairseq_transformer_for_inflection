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
            id2pred[id] = pred.replace(' ', '')
    inputlines = [line.strip() for line in finput]
    for i, line in enumerate(inputlines):
        lemma, _, msd = line.strip().split('\t')
        fw.write('\t'.join([lemma, id2pred[i], msd]) + '\n')



