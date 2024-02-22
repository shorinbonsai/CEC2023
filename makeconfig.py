import csv
import os
import sys

# Profiles
# p1 = "0.0312029 0.35282 0.25448 0.28346 0.00649138 0.0150983 0.00109488 0.0324265 0.0229266 "
# p2 = "0.759203 0.0305105 0.00241891 0.00600742 0.00676785 0.034367 0.0105658 0.117565 0.0325949 "
# p3 = "0.00726438 0.0260516 0.340635 0.00152519 0.0195147 0.374055 0.0077196 0.203695 0.0195395 "
# p4 = "0.368196 0.0190693 0.0319179 0.366953 0.0191151 0.11071 0.0127143 0.0466466 0.0246774 "
# p5 = "0.0179573 0.049097 0.000154922 0.764618 0.0277425 0.0173987 0.0660979 0.0047374 0.0521967 "
# p6 = "0.00323446 0.398225 0.0128502 0.0426209 0.0335682 0.0115188 0.00701098 0.0539209 0.43705 "
# p7 = "0.357175 0.201562 0.00447789 0.00787014 0.00262596 0.00879636 0.355586 0.0510066 0.0108997 "
# p8 = "0.423771 0.034258 0.00211753 0.0319399 0.00206064 0.00660799 0.048702 0.00368962 0.446854 "

# Duration
# p1 = "0.0312029 0.35282 0.25448 0.28346 0.00649138 0.0150983 0.00109488 0.0324265 0.0229266 "
# p2 = "0.0438092 0.0188496 0.0281214 0.0499315 0.000273141 0.432242 0.00508051 0.0169589 0.404733 "
# p3 = "0.0179573 0.049097 0.000154922 0.764618 0.0277425 0.0173987 0.0660979 0.0047374 0.0521967 "
# p4 = "0.0333572 0.414917 0.0112833 0.000532368 0.0323085 0.412991 0.0212584 0.0373119 0.0360396 "
# p5 = "0.0128646 0.389581 0.019287 0.00339553 0.00379972 0.00009036 0.148332 0.409602 0.0130482 "
# p6 = "0.0341497 0.0191908 0.00442833 0.209495 0.0585888 0.332769 0.323254 0.00469258 0.013431 "
# p7 = "0.0531136 0.789422 0.0394036 0.0260864 0.0114258 0.0202999 0.0150275 0.0163537 0.0288679 "
# p8 = "0.00323446 0.398225 0.0128502 0.0426209 0.0335682 0.0115188 0.00701098 0.0539209 0.43705 "

# test densities
p1 = "0.252285 0.0244388 0.0803629 0.013385 0.269923 0.00555957 0.237857 0.0551791 0.0610102 "
p2 = "0.751169 0.0264949 0.01653 0.0662802 0.0072829 0.0489093 0.0294204 0.029531 0.0243822 "
p3 = "0.0133053 0.01672 0.0194695 0.0459996 0.00918666 0.0368842 0.773507 0.00455052 0.0803774 "
p4 = "0.000186181 0.184902 0.0270336 0.713587 0.017313 0.0152535 0.000959354 0.00244221 0.0383236 "
p5 = "0.00932626 0.019643 0.0274797 0.00551086 0.0105448 0.0383528 0.00195196 0.822713 0.0644776 "
p6 = "0.015828 0.0213853 0.045346 0.0292304 0.777718 0.0379161 0.0159045 0.0301709 0.0265007 "
p7 = "0.0322815 0.0456118 0.774662 0.00717739 0.0352475 0.0519677 0.0385945 0.000976337 0.0134808 "
p8 = "0.00392737 0.00816609 0.00495686 0.306572 0.0111134 0.00928871 0.0179041 0.258563 0.379509 "
p9 = "0.000226298 0.745308 0.0112869 0.00578633 0.00837676 0.0680324 0.00989125 0.1205 0.0305925 "
p10 = "0.00271179 0.00912587 0.00107073 0.0627651 0.00713813 0.854546 0.0484254 0.00275076 0.0114662 "
p11 = "0.0116187 0.245324 0.203332 0.00886967 0.00068059 0.339068 0.0164031 0.038454 0.136249 "
p12 = "0.00331919 0.006526 0.00292917 0.00851741 0.00547914 0.052572 0.0203249 0.034358 0.865974 "
# p13 = "0.0199224 0.00318979 0.324294 0.188128 0.399131 0.0012421 0.0262276 0.0268533 0.0110109"
# p14 = "0.0179573 0.049097 0.000154922 0.764618 0.0277425 0.0173987 0.0660979 0.0047374 0.0521967"
# p15 = "0.0333572 0.414917 0.0112833 0.000532368 0.0323085 0.412991 0.0212584 0.0373119 0.0360396"
# p16 = "0.0128646 0.389581 0.019287 0.00339553 0.00379972 0.00009036 0.148332 0.409602 0.0130482"
# p17 = "0.00929419 0.0210842 0.00983161 0.00199297 0.808423 0.0531949 0.0000337 0.0519473 0.0441978"
# p18 = "0.0341497 0.0191908 0.00442833 0.209495 0.0585888 0.332769 0.323254 0.00469258 0.0134319"
# p19 = "0.0531136 0.789422 0.0394036 0.0260864 0.0114258 0.0202999 0.0150275 0.0163537 0.0288679"
# p20 = "0.00377077 0.0456627 0.406635 0.0768452 0.0225842 0.00605926 0.395203 0.0267984 0.0164408"
# p21 = "0.00323446 0.398225 0.0128502 0.0426209 0.0335682 0.0115188 0.00701098 0.0539209 0.43705"
# p22 = "0.0258769 0.0140246 0.00316205 0.221979 0.00559183 0.0160208 0.020291 0.362284 0.330769"
# p23 = "0.00532201 0.0228535 0.0371849 0.0191664 0.0110278 0.0134098 0.0435344 0.00453251 0.842969"
# p24 = "0.0176338 0.376509 0.0125054 0.0156455 0.363675 0.00940393 0.175719 0.00993326 0.0189757"
# p25 = "0.357175 0.201562 0.00447789 0.00787014 0.00262596 0.00879636 0.355586 0.0510066 0.0108997"
# p26 = "0.00271179 0.00912587 0.00107073 0.0627651 0.00713813 0.854546 0.0484254 0.00275076 0.0114662"
# p27 = "0.00382178 0.0156427 0.0220541 0.00213684 0.028481 0.0267235 0.418316 0.0396135 0.44321"
# p28 = "0.0265174 0.0455925 0.0144216 0.0108894 0.0179354 0.0102103 0.00867097 0.796621 0.0691414"
# p29 = "0.423771 0.034258 0.00211753 0.0319399 0.00206064 0.00660799 0.048702 0.00368962 0.446854"
pp0 = "0 "
pp1 = "1 "
pr1 = "./Profiles/Profile1.dat 1 "
pr2 = "./Profiles/Profile2.dat 2 "
pr3 = "./Profiles/Profile3.dat 3 "
pr4 = "./Profiles/Profile4.dat 4 "
pr5 = "./Profiles/Profile5.dat 5 "
pr6 = "./Profiles/Profile6.dat 6 "
pr7 = "./Profiles/Profile7.dat 7 "
pr8 = "./Profiles/Profile8.dat 8 "
pr9 = "./Profiles/Profile9.dat 9 "

# prog1 = "./recreate ./dublinRecreate/"
# prog2 = "./PMedgeOpex ./PMedgeOp/"
# prog1 = "./PMpcgTest2ex ./PMpcgTest2/"
# prog1 = "./prof1s30alpha ./PM1pcg/"
# prog2 = "./prof1s40alpha ./PM1pcg/"
# prog3 = "./prof3s30alpha ./PM3pcg/"
# prog4 = "./prof3s40alpha ./PM3pcg/"
# prog5 = "./prof5s30alpha ./PM5pcg/"
# prog6 = "./prof5s40alpha ./PM5pcg/"

# prog1 = "./ED1s30alpha ./ED1pcg/"
# prog2 = "./ED1s40alpha ./ED1pcg/"
# prog3 = "./ED3s30alpha ./ED3pcg/"
# prog4 = "./ED3s40alpha ./ED3pcg/"
# prog5 = "./ED5s30alpha ./ED5pcg/"
# prog6 = "./ED5s40alpha ./ED5pcg/"

d1 = "ps1/ "
d2 = "ps2/ "
d3 = "ps3/ "
d4 = "ps4/ "
d5 = "ps5/ "
d6 = "ps6/ "
d7 = "ps7/ "
d8 = "ps8/ "
d9 = "ps9/ "
d10 = "ps10/ "
d11 = "ps11/ "
d12 = "ps12/ "
d13 = "ps13/ "
d14 = "ps14/ "
d15 = "ps15/ "
d16 = "ps16/ "
d17 = "ps17/ "
d18 = "ps18/ "
d19 = "ps19/ "
d20 = "ps20/ "
d21 = "ps21/ "
d22 = "ps22/ "
d23 = "ps23/ "
d24 = "ps24/ "
d25 = "ps25/ "
d26 = "ps26/ "
d27 = "ps27/ "
d28 = "ps28/ "
d29 = "ps29/ "

dirs = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15,
        d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29]

root1 = "/home/js17sy/projects/def-houghten/js17sy/PM1r/"
root3 = "/home/js17sy/projects/def-houghten/js17sy/PM3r/"
root5 = "/home/js17sy/projects/def-houghten/js17sy/PM5r/"

mid30 = "30alph/"
mid40 = "40alph/"

# densities = [p1, p2, p3, p4, p5, p6, p7, p8]
densities = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
print(len(densities))
# profiles = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9]
profiles = [pr1, pr7]

prog1 = "./new128ED ./128EDgraph1/"
prog2 = "./new128ED ./128EDgraph2/"
prog3 = "./new128ED ./128EDgraph3/"
prog4 = "./new128PM ./128PM1graph1/"
prog5 = "./new128PM ./128PM1graph2/"
prog6 = "./new128PM ./128PM1graph3/"
prog7 = "./new128PM ./128PM7graph1/"
prog8 = "./new128PM ./128PM7graph2/"
prog9 = "./new128PM ./128PM7graph3/"
prog10 = "./new256ED ./256EDgraph1/"
prog11 = "./new256ED ./256EDgraph2/"
prog12 = "./new256ED ./256EDgraph3/"
prog13 = "./new256PM ./256PM1graph1/"
prog14 = "./new256PM ./256PM1graph2/"
prog15 = "./new256PM ./256PM1graph3/"
prog16 = "./new256PM ./256PM7graph1/"
prog17 = "./new256PM ./256PM7graph2/"
prog18 = "./new256PM ./256PM7graph3/"
prog19 = "./newDUBPM ./DUBPMgraph1/"
prog20 = "./newDUBPM ./DUBPMgraph2/"
prog21 = "./newDUBPM ./DUBPMgraph3/"
progsPM = [prog4, prog5, prog6, prog7, prog8, prog9, prog13, prog14, prog15, prog16, prog17, prog18]
progsED = [prog1, prog2, prog3, prog10, prog11, prog12]
progsDUB = [prog19, prog20, prog21]

#files
EDFiles = ["128ED_BestNet1.dat", "128ED_BestNet2.dat", "128ED_BestNet3.dat", "256ED_BestNet3.dat", "256ED_BestNet8.dat", "256ED_BestNet9.dat"]
PMFiles = ["128PM1_BestNet3.dat", "128PM1_BestNet5.dat", "128PM1_BestNet6.dat","128PM7_BestNet1.dat", "128PM7_BestNet6.dat","128PM7_BestNet9.dat", \
           "256PM1_BestNet1.dat","256PM1_BestNet2.dat", "256PM1_BestNet3.dat", "256PM7_BestNet1.dat", "256PM7_BestNet6.dat", "256PM7_BestNet9.dat"]
DUBFiles = ["DUBPM_BestNet1.dat", "DUBPM_BestNet6.dat", "DUBPM_BestNet8.dat"]

with open('bmcED.dat', 'w') as f:
    count = 0
    for i in range(len(progsED)):
        for x in range(len(densities)):
            cmd = progsED[i] + dirs[x] + pp1 + densities[x] + EDFiles[i]
            print(cmd, file=f)

with open('bmcPM.dat', 'w') as f:
    count = 0
    PM = 0
    for i in range(len(progsPM)):
        if count == 3:
            count = 0
            if PM == 0:
                PM = 1
            else:
                PM = 0
        for x in range(len(densities)):

            cmd = progsPM[i] + dirs[x] + profiles[PM] + densities[x] + PMFiles[i]
            print(cmd, file=f)
        count += 1

with open('bmcDUB.dat', 'w') as f:
    for i in range(len(progsDUB)):
        for x in range(len(densities)):
            cmd = progsDUB[i] + dirs[x] + pp0 + densities[x] + DUBFiles[i]
            print(cmd, file=f)

#     for x in range(len(densities)):
#         cmd = prog2 + mid40 + dirs[x] + profiles[0] + densities[x]
#         print(cmd, file=f)

    # for x in range(len(densities)):
    #     cmd = prog1 + mid30 + dirs[x] + profiles[0] + densities[x]
    #     print(cmd, file=f)

#     for x in range(len(densities)):
#         cmd = prog4 + mid40 + dirs[x] + profiles[0] + densities[x]
#         print(cmd, file=f)

    # for x in range(len(densities)):
    #     cmd = prog1 + mid30 + dirs[x] + profiles[0] + densities[x]
    #     print(cmd, file=f)

#     for x in range(len(densities)):
#         cmd = prog6 + mid40 + dirs[x] + profiles[0] + densities[x]
#         print(cmd, file=f)


# with open('table2.dat', 'w') as f:
#     for x in range(len(densities)):
#         for y in range(len(profiles)):
#             cmd = prog2 + dirs[x] + profiles[y] + densities[x]
#             # print(cmd)
#             print(cmd, file=f)

#     for x in range(len(densities)):
#         for y in range(len(profiles)):
#             cmd = prog2 + mid40 + dirs[x] + profiles[y] + densities[x]
#             #print(cmd)
#             print(cmd, file=f)

#     for x in range(len(densities)):
#         for y in range(len(profiles)):
#             cmd = prog3 + mid30 + dirs[x] + profiles[y] + densities[x]
#             #print(cmd)
#             print(cmd, file=f)

    # for x in range(len(densities)):
    #     for y in range(len(profiles)):
    #         cmd = prog4 + mid40 + dirs[x] + profiles[y] + densities[x]
    #         #print(cmd)
    #         print(cmd, file=f)

    # for x in range(len(densities)):
    #     for y in range(len(profiles)):
    #         cmd = prog5 + mid30 + dirs[x] + profiles[y] + densities[x]
    #         #print(cmd)
    #         print(cmd, file=f)

    # for x in range(len(densities)):
    #     for y in range(len(profiles)):
    #         cmd = prog6 + mid40 + dirs[x] + profiles[y] + densities[x]
    #         #print(cmd)
    #         print(cmd, file=f)
