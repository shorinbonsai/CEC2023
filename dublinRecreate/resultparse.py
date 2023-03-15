import sys
import os
import csv

wordCheck = "-fitness\n"
outFile = sys.argv[1]


def getFits(dir_path: str):
    data = []
    with open(dir_path) as f:
        lines = f.readlines()
        for line in lines:
            spl = line.split(' ')
            if wordCheck in spl:
                data.append(float(spl[0]))
    return data


def main():
    results = [[] for _ in range(29)]
    with open(outFile, mode='w') as f:
        for dirpath, dirnames, files in os.walk('.'):
            for file_name in files:
                if file_name.endswith("best.lint"):
                    direc = os.path.join(dirpath, file_name)
                    if dirpath.__contains__("ps1/"):
                        results[0].append(getFits(direc))
                    elif dirpath.__contains__("ps2/"):
                        results[1].append(getFits(direc))
                    elif dirpath.__contains__("ps3/"):
                        results[2].append(getFits(direc))
                    elif dirpath.__contains__("ps4/"):
                        results[3].append(getFits(direc))
                    elif dirpath.__contains__("ps5/"):
                        results[4].append(getFits(direc))
                    elif dirpath.__contains__("ps6/"):
                        results[5].append(getFits(direc))
                    elif dirpath.__contains__("ps7/"):
                        results[6].append(getFits(direc))
                    elif dirpath.__contains__("ps8/"):
                        results[7].append(getFits(direc))
                    elif dirpath.__contains__("ps9/"):
                        results[8].append(getFits(direc))
                    elif dirpath.__contains__("ps10/"):
                        results[9].append(getFits(direc))
                    elif dirpath.__contains__("ps11/"):
                        results[10].append(getFits(direc))
                    elif dirpath.__contains__("ps12/"):
                        results[11].append(getFits(direc))
                    elif dirpath.__contains__("ps13/"):
                        results[12].append(getFits(direc))
                    elif dirpath.__contains__("ps14/"):
                        results[13].append(getFits(direc))
                    elif dirpath.__contains__("ps15/"):
                        results[14].append(getFits(direc))
                    elif dirpath.__contains__("ps16/"):
                        results[15].append(getFits(direc))
                    elif dirpath.__contains__("ps17/"):
                        results[16].append(getFits(direc))
                    elif dirpath.__contains__("ps18/"):
                        results[17].append(getFits(direc))
                    elif dirpath.__contains__("ps19/"):
                        results[18].append(getFits(direc))
                    elif dirpath.__contains__("ps20/"):
                        results[19].append(getFits(direc))
                    elif dirpath.__contains__("ps21/"):
                        results[20].append(getFits(direc))
                    elif dirpath.__contains__("ps22/"):
                        results[21].append(getFits(direc))
                    elif dirpath.__contains__("ps23/"):
                        results[22].append(getFits(direc))
                    elif dirpath.__contains__("ps24/"):
                        results[23].append(getFits(direc))
                    elif dirpath.__contains__("ps25/"):
                        results[24].append(getFits(direc))
                    elif dirpath.__contains__("ps26/"):
                        results[25].append(getFits(direc))
                    elif dirpath.__contains__("ps27/"):
                        results[26].append(getFits(direc))
                    elif dirpath.__contains__("ps28/"):
                        results[27].append(getFits(direc))
                    elif dirpath.__contains__("ps29/"):
                        results[28].append(getFits(direc))
        label = "EE"
        for x in range(29):       
            print(label + str(x + 1), file=f)
            for i in results[x]:
                for j in i:
                    print(j, file=f)
        # print(file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)
        # print("EE2", file=f)
        # for i in results[1]:
        #     for j in i:
        #         print(j, file=f)


if '__main__' == __name__:
    main()
