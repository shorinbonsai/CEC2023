import sys
import os
import csv
import copy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

wordCheck = "-fitness\n"
outFile = sys.argv[1]


def getFits(dir_path: str):
    data = []
    graphbest = []
    graph = []
    bestfit = 9999999
    counter = 0
    order = 0
    with open(dir_path) as f:
        lines = f.readlines()
        for line in lines:
            if line.__contains__(wordCheck):
                if len(graph) > 1:
                    if fit < bestfit:
                        graphbest = graph
                        graph = []
                spl = line.split(' ')
                fit = float(spl[0])
                data.append(fit)
                count = 1
                
            elif count < 4:
                count += 1
            elif count == 4:
                spl = line.split(' ')
                order = int(spl[0])
                count += 1
            elif count == 5:
                graph.append(line)

                
    return data, graphbest

def getRef(dir_ref: str):
    with open(dir_ref) as f:
        lines = f.readlines()
        count = 0
        result = []
        for line in lines:
            count += 1
            if count < 3:
                pass
            else:
                spl = line.strip()
                result.append(spl)
        return result
            

def compare(duby , testy ):
    dub = copy.deepcopy(duby)
    test = copy.deepcopy(testy)
    onlyDub = []
    both = []
    onlyTest = []
    for i,j in enumerate(dub):
        dub[i] = j.split(' ')
    for i,j in enumerate(test):
        test[i] = j.split(' ')
    for i,_ in enumerate(dub):
        for num in dub[i]:
            if num == ' ':
                print("wtf")
            if num in test[i]:
                both.append(int(num))
            else:
                onlyDub.append(int(num))
        for num in test[i]:
            if num == ' ':
                print("huh?")
            if num not in dub[i]:
                onlyTest.append(int(num))
    dubCount = len(onlyDub)/2
    bothCount = len(both)/2
    testCount = len(onlyTest)/2
                
    return onlyDub, both, onlyTest


def main():
    results = [[] for _ in range(29)]
    graphs = [[] for _ in range(29)]
    dub = getRef("dublin_graph.dat")
    with open(outFile, mode='w') as f:
        for dirpath, dirnames, files in os.walk('.'):
            for file_name in files:
                if file_name.endswith("best.lint"):
                    direc = os.path.join(dirpath, file_name)
                    if dirpath.__contains__("ps1/"):
                        results[0], graphs[0] = getFits(direc)
                    elif dirpath.__contains__("ps2/"):
                        results[1], graphs[1] = getFits(direc)
                    elif dirpath.__contains__("ps3/"):
                        results[2], graphs[2] = getFits(direc)
                    elif dirpath.__contains__("ps4/"):
                        results[3], graphs[3] = getFits(direc)
                    elif dirpath.__contains__("ps5/"):
                        results[4], graphs[4] = getFits(direc)
                    elif dirpath.__contains__("ps6/"):
                        results[5], graphs[5] = getFits(direc)
                    elif dirpath.__contains__("ps7/"):
                        results[6], graphs[6] = getFits(direc)
                    elif dirpath.__contains__("ps8/"):
                        results[7], graphs[7] = getFits(direc)
                    elif dirpath.__contains__("ps9/"):
                        results[8], graphs[8] = getFits(direc)
                    elif dirpath.__contains__("ps10/"):
                        results[9], graphs[9] = getFits(direc)
                    elif dirpath.__contains__("ps11/"):
                        results[10], graphs[10] = getFits(direc)
                    elif dirpath.__contains__("ps12/"):
                        results[11], graphs[11] = getFits(direc)
                    elif dirpath.__contains__("ps13/"):
                        results[12], graphs[12] = getFits(direc)
                    elif dirpath.__contains__("ps14/"):
                        results[13], graphs[13] = getFits(direc)
                    elif dirpath.__contains__("ps15/"):
                        results[14], graphs[14] = getFits(direc)
                    elif dirpath.__contains__("ps16/"):
                        results[15], graphs[15] = getFits(direc)
                    elif dirpath.__contains__("ps17/"):
                        results[16], graphs[16] = getFits(direc)
                    elif dirpath.__contains__("ps18/"):
                        results[17], graphs[17] = getFits(direc)
                    elif dirpath.__contains__("ps19/"):
                        results[18], graphs[18] = getFits(direc)
                    elif dirpath.__contains__("ps20/"):
                        results[19], graphs[19] = getFits(direc)
                    elif dirpath.__contains__("ps21/"):
                        results[20], graphs[20] = getFits(direc)
                    elif dirpath.__contains__("ps22/"):
                        results[21], graphs[21] = getFits(direc)
                    elif dirpath.__contains__("ps23/"):
                        results[22], graphs[22] = getFits(direc)
                    elif dirpath.__contains__("ps24/"):
                        results[23], graphs[23] = getFits(direc)
                    elif dirpath.__contains__("ps25/"):
                        results[24], graphs[24] = getFits(direc)
                    elif dirpath.__contains__("ps26/"):
                        results[25], graphs[25] = getFits(direc)
                    elif dirpath.__contains__("ps27/"):
                        results[26], graphs[26] = getFits(direc)
                    elif dirpath.__contains__("ps28/"):
                        results[27], graphs[27] = getFits(direc)
                    elif dirpath.__contains__("ps29/"):
                        results[28], graphs[28] = getFits(direc)
        label = "EE"
        with open("graphs" + outFile, mode='w') as g:
            for x in range(29):       
                print(label + str(x + 1), file=f)
                print(label + str(x + 1), file=g)
                graphs[x].pop()
                for i, j in enumerate(graphs[x]):
                    graphs[x][i] = j.strip()
                    print(graphs[x][i], file=g)
            # print(*graphs[x] + "\n", file=f)
                best = results[x].index(min(results[x]))
                print("graph: " + str(best + 1) + " value: " + str(results[x][best]), file=f)
        print("cat")
        with open("analysis"+ outFile, mode='w') as h:
            for x in range(29):
                print(label + str(x+1), file=h)
                donly, both, tonly = compare(dub, graphs[x])
                print("Dublin only: " + str(len(donly)/2), file=h)
                print("Both graphs: " + str(len(both)/2), file=h)
                print("Evolved graph only: " + str(len(tonly)/2), file=h)
                print("cat")
        ax = sns.boxplot(data=results)
        plt.show()




if '__main__' == __name__:
    main()
