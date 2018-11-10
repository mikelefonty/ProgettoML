import numpy as np
from MLP import *
# 2(target) 3  3  2  3 4 2
def encode_target(x):
    if x == 1:
        return (1,)
    else:
        return (0,)

def encode_2(x):
    if x == 1:
        return (1,0)
    else:
        return (0,1)

def encode_3(x):
    if x == 1:
        return (1,0,0)
    if x == 2:
        return (0,1,0)
    else:
        return (0,0,1)

def encode_4(x):
    if x == 1:
        return (1,0,0,0)
    if x == 2:
        return (0,1,0,0)
    if x == 3:
        return (0,0,1,0)
    else:
        return (1,0,0,0)

def load_monk(filename):
    with open(filename) as f:
        res = []
        for line in f:
            example = line.split(' ')[:-1]

            for (i,l) in enumerate(example):
                if i == 0:
                    res.append(encode_target(int(l)))
                elif i == 3 or i == 6:
                     res.append(encode_2(int(l)))
                else:
                    if i == 1 or i == 2 or i == 4:
                        res.append(encode_3(int(l)))
                    else:
                        res.append(encode_4(int(l)))


        res = np.array(res).reshape(-1,7)
        X = np.zeros((res.shape[0],18))

        for (riga_x,riga) in enumerate(res):
            i =0
            colonna_x = 0
            for colonne in riga:
                if i == 0:
                    X[riga_x, colonna_x] = riga[i][0]
                    i += 1
                elif i == 3 or i == 6:
                     X[riga_x,colonna_x]= riga[i][0]
                     X[riga_x, colonna_x + 1] = riga[i][1]
                     colonna_x+=2
                     i+=1
                else:
                    if i == 1 or i == 2 or i == 4:
                        X[riga_x, colonna_x] = riga[i][0]
                        X[riga_x, colonna_x + 1] = riga[i][1]
                        X[riga_x, colonna_x + 2] = riga[i][2]
                        colonna_x += 3
                        i += 1
                    else:
                        X[riga_x, colonna_x] = riga[i][0]
                        X[riga_x, colonna_x + 1] = riga[i][1]
                        X[riga_x, colonna_x + 2] = riga[i][2]
                        X[riga_x, colonna_x + 3] = riga[i][3]
                        colonna_x += 4
                        i += 1

        X_train = np.array(X[:,1:])
        Y_train = np.array(X[:,0]).reshape(X.shape[0],-1)
        return X_train, Y_train






