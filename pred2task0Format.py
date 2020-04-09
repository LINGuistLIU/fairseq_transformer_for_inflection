'''
This script transforms the best predictions from the best model back to the task0 data format.

$ python pred2task0Format.py 3LETTER-LANGUAGE-CODE
'''
import sys
import os

def goldid2input(fname):
    inputlist = []
    with open(fname) as f:
        for line in f:
            lines = line.strip().split('\t')
            if len(lines) == 3 or len(lines) == 2:
                lemma = lines[0]
                msd = lines[-1]
            else:
                print('Please make sure each line in your file is a tab separated 3-column entry.')
            inputlist.append((lemma, msd))
    return inputlist

def id2pred(fname):
    id2pred_dict = {}
    with open(fname) as f:
        for line in f:
            if line[:2] == 'H-':
                id, score, pred = line.strip().split('\t')
                id = int(id.split('-')[1])
                id2pred_dict[id] = pred.replace(' ', '').replace('_', ' ')
    return id2pred_dict

def outputReformatted(inputlist, id2pred_dict, foutname):
    with open(foutname, 'w') as fw:
        id = 0
        for lemma, msd in inputlist:
            fw.write('\t'.join([lemma, id2pred_dict[id], msd]) + '\n')
            id += 1

def outputAll(pred_dir, output_dir, fgoldname):
    inputlist = goldid2input(fgoldname)
    for file in os.listdir(pred_dir):
        if type in file:
            fpredname = pred_dir + file
            id2pred_dict = id2pred(fpredname)
            foutname = output_dir+file
            outputReformatted(inputlist, id2pred_dict, foutname)

if __name__ == '__main__':
    lang = sys.argv[1]
    type = sys.argv[2]  # dev or test

    output_dir = 'predictions/'+lang+'/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pred_dir = 'checkpoints/' + lang + '-predictions/'
    fgoldname = 'task0-data/'+lang+'.'+type

    outputAll(pred_dir, output_dir, fgoldname)



