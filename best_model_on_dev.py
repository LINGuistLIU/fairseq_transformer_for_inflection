'''
This script picks out the models with the first five highest accuracies on the dev set,
and deletes all other models.
'''

import os
import sys

def file2dict(fname):
    id2gold = {}
    id2pred = {}
    with open(fname) as f:
        for line in f:
            if 'T-' in line:
                id, gold = line.strip().split('\t')
                id = int(id.strip().split('\-')[1])
                id2gold[id] = gold.strip()
            if 'H-' in line:
                id, score, pred = line.strip().split('\t')
                id = int(id.strip().split('\-')[1])
                id2pred[id] = pred.strip()
    return id2gold, id2pred

def first5accurate(pred_dir):
    file_acc_list = []
    for item in os.listdir(pred_dir):
        if 'dev-' in item:
            fname = pred_dir + item
            id2gold, id2pred = file2dict(fname)
            correct = 0
            guess = 0
            for k, v in id2gold:
                guess += 1
                if v == id2pred[k]:
                    correct += 1
            file_acc_list.append(item, round(correct/guess, 6))
    final_list = []
    for i in range(0, 5):
        candidate = (0, 0)
        for j in range(len(file_acc_list)):
            if file_acc_list[j][1] > candidate[1]:
                candidate = file_acc_list[j]
        file_acc_list.remove(candidate)
        final_list.append(candidate)
    return final_list

def deletefiles(final_list):
    modelset = set([item[0][:-4] for item in final_list])
    predset = set([item[0] for item in final_list])
    for item in os.listdir(model_dir):
        if item not in modelset:
            os.remove(model_dir+item)
    for item in os.listdir(pred_dir):
        if item not in predset:
            os.remove(pred_dir+item)

if __name__ == '__main__':
    lang = sys.argv[1]

    model_dir = 'checkpoints/' + lang + '-models/'
    pred_dir = 'checkpoints/' + lang + '-predictions/'

    final_list = first5accurate(pred_dir)
    deletefiles(final_list)

