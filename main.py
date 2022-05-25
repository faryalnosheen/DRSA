from threading import Thread
from time import perf_counter

import pandas as pd


import numpy as np

# thread to execute upper approximation for downward union of classes
def upper_downward(u,t,cl,cl2,c):

    G = 0
    S = 0
    E = 0
    GP = 0
    L1 = False
    upd= [[0 for i in range(t)] for j in range(u)]

    for i in range(0,len(cl)):
        upd[i]= cl[i][1]

        m= upd.shape[0]:
    for j in range(0,len(cl2)):
        m=m+1
        upd[m] = cl[i][1]

    for i in range(0,len(cl2)):
        for j in range(0,len(cl))
            for k in range (1,c-1)
                if cl2[i][k] > cl[j][k]:
                    G = G + 1
                elif cl2[i][k] < cl[j][k]:
                    S = S + 1
                elif cl2[i][k] == cl[j][k]:
                    E = E + 1
                if S > 0 and G > 0:
                    GP = GP + 1
                    L1 = False
                elif G > 0 and E > 0 and S=0:
                    GP = GP + 1
                    L1 = True
                    upd[j] = Cl2[j][1]
                if E == c - 2:
                    L1 = True
                G = 0
                E = 0
                S = 0
            GP = 0

#thread to execute lower approximation for downward union of classes

def lower_downward(t,cl,cl1,cl2,c,u):

# number of rows can be get by len(cl) and number of columns by len(cl[0])

lpd = [[0 for i in range(t)] for j in range(u)]

    G=0
    S=0
    E=0
    GP=0
    L1= False
    for i in range (0,len(cl2)):
        for j in range(0,len(cl)):
            for k in range (1,c-1):
                if cl2[i][k] > cl[j][k]:
                    G=G+1
                elif cl2[i][k] < cl[j][k]:
                    S=S+1
                elif cl2[i][k] == cl[j][k]:
                    E=E+1
                if S>0 and G>0:
                    GP= GP+1
                    L1= False
                elif G>0 and E>0 and S=0:
                    GP= GP+1
                    L1= True
                    UPD[j] = Cl2[j][0]
                if E== c-2:
                    L1= True
                G=0
                E=0
                S=0
        if not L1:
            lpd[t][l+1] = cl[i][0]
        GP=0

    for i in range(0, len(cl1)):
        for j in range(0, len(cl)):
            for k in range(1, c - 1):
                if cl1[i][k] > cl[j][k]:
                    G = G + 1
                elif cl1[i][k] < cl[j][k]:
                    S = S + 1
                elif cl1[i][k] == cl[j][k]:
                    E = E + 1
                if S > 0 and G > 0:
                    GP = GP + 1
                    L1 = False
                elif G > 0 and E > 0 and S=0:
                    GP = GP + 1
                    L1 = True
                if E == c - 2:
                    L1 = True
                G = 0
                E = 0
                S = 0
        if L1:
            lpd[t][l+1] = cl1[i][0]
        GP = 0
# lower approximation for upward union of classes
def lower_upward(t,lpd,u,c,np_array):

    lpu = [[0 for i in range(t)] for j in range(u)]
    p=0
    k= False
    for i in range(0,u):
        for j in range(0,len(lpd[0])):
            if np_array[i][1] == lpd[t][j]:
                k= True
                break
        if not k:
            lpu[t][p] = np_array[i][0]
            p=p+1
# upper approximation for upward union of classes
def upper_upward(t,u,cl,cl2,cl1,c)
    upu = [[0 for i in range(t)] for j in range(u)]
    q=0
    r=0
    G=0
    S=0
    L1 = False
    GP=0
    z=0
    for i in range(0,cl):
        upu[t][q] = cl[i][0]
        q=q+1
    for j in range(0,cl2):
        upu[t][r] = cl2[j][0]
        r=r+1
    for i in range(0,len(cl1)):
        for j in range(0, len(cl)):
            for k in range(1, c - 1):
                if cl1[i][k] > cl[j][k]:
                    G = G + 1
                elif cl1[i][k] < cl[j][k]:
                    S = S + 1
                elif cl1[i][k] == cl[j][k]:
                    E = E + 1

                if G > 0 and E > 0 and S=0:
                    GP = GP + 1
                    L1 = True
                if E == c - 2:
                    L1 = True
                G = 0
                E = 0
                S = 0
        if L1:
            upu[t][z] = cl1[i][0]
        GP = 0

def main():

#mention path of your decision system from excel sheet
df= pd.read_excel("sample.xlsx")

    data = pd.DataFrame(df)
    np_array = data.to_numpy()
    d=3
    m=0
    n=0
    l=0
    a=1
    dt=[0 for i in range(3)]
    u=np_array.shape[0] # number of rows
    c=np_array.shape[1] # number of columns

    cl= [[0 for i in range(u)] for j in range(c)]

    cl1 = [[0 for i in range(u)] for j in range(c)]

    cl2 = [[0 for i in range(u)] for j in range(c)]

    for t in range(1,3):
        for i in range(0,u):
            if (np_array[i][3]) == t:
                m = m + 1
                dt[t] = m
            for j in range(1,c):
                cl[i][a]=np_array[i][j]
                a=a+1
            elif(np_array[i][3])> t:
                a=1
                n = n + 1
                dt[t] = n
                for j in range(1,c-1):
                cl1[i][a]=np_array[i][j]
                a=a+1
            elif(np_array[i][3]) < t:
                a=1
                l = l + 1
                dt[t] = l
                for j in range(1,c):
                cl2[i][a]=np_array[i][j]
                a=a+1

# Compute approximations for downward union of classes
if __name__ == '__main__':
    Thread(target=lower_downward(d,cl,cl1,cl2,c,u)).start()
    Thread(target=upper_downward(u,d,cl,cl2,c)).start()

print("lower and upper approximation for upward union of classes")

if __name__ == '__main__':
    Thread(target=lower_upward(t,lpd,u,c,np_array)).start()
    Thread(target=upper_upward(t,u,cl,cl2,cl1,c)).start()







