#=====================================================================
def reading(path): 
    """перевод из текстового файла в двумерный массив типа int"""
    global mat
    global matset 
    data = ''
    f = open(path, 'r')
    trash = f.readline()
    trash = f.readline()
    while len(trash) != 58 :
        trash = f.readline()
    while len(trash) != 57:
        array = []
        trash = f.readline()
        if len(trash) == 57:
            break
        mat.append(trash.replace(' \n', '').split())
        matset.append(trash.replace(' \n', '').split())
    i = 0
    while i != len(mat):
        for j in range(len(mat[1])):
            mat[i][j] = int(mat[i][j])
            matset[i][j] = int(mat[i][j])
        i += 1  
#=====================================================================


#=====================================================================
def bfs1(v):
    global visited
    global found
    global t
    global printt
    global par
    q = [0] * len(mat[0])
    for i in range(len(mat[0])):
        q[i] = 0
        minproh[i] = 9999
    k = 0
    head = -1
    k += 1
    q[k-1] = v
    visited[v] = True
    while head < k:
        head += 1
        v = q[head]
        printt.append(v)
        for i in range(len(matset[0])):
            if matset[v][i] != 0 and not(visited[i]):
                par[i] = v + 1
                if matset[v][i] < minproh[v]:
                    minproh[i] = matset[v][i]
                else:
                    minproh[i] = minproh[v]
                if i  == t:
                    head = k + 10
                    found = True
                k += 1
                q[k-1] = i
                visited[i] = True
#=====================================================================


#=====================================================================
def dfs2(v, c): #проверка на двудольность
    global dvydol
    visited[v] = True
    colors[v] = c 
    for i in range(n):
        if mat[v][i] != 0 or mat[i][v] != 0:
            if not(visited[i]):
                if c == 1:
                    dfs2(i, 2)
                else:
                    dfs2(i, 1)
            else:
                if colors[i] ==c:
                    dvydol = False
#=====================================================================
printt = []
mat = []
matset = []
path = input('Введите название файла: ') + '.txt'
reading(path)
masv = [0] * len(mat[0])
minproh = [0] * len(mat[0])
par = [0] * len(mat[0])
visited = [False] * len(mat[0])

found = True
t = 0 
s = 0
potok = 0

""" for i in range(len(matset[0])):
    for j in range(len(matset[0])):
        matset[i][j] = 0 """

#=====================================================================
#Сток и исток
for i in range(len(mat[0])):
    stok = True
    istok = True
    for j in range(len(mat[0])):
        if mat[i][j] != 0:
            stok = False
        if mat[j][i] != 0:
            istok = False
    if stok:
        t = i
    if istok:
        s = i    
print('Исток и сток:')  
print(s+1, t+1)     
#=====================================================================


#=====================================================================
#поиск
found = True
while found:
    found = False
    for i in range(len(mat[0])):
        visited[i] = False
        par[i] = 0  
    bfs1(s)
    if found:
        i = t
        d = minproh[t]
        while par[i] != 0:
            matset[i][par[i]-1] = matset[i][par[i]-1] + d
            matset[par[i]-1][i] = matset[par[i]-1][i] - d  
            i = par[i]-1
#=====================================================================


#=====================================================================
#поток
potok = 0
for i in range(len(mat[0])):
    if matset[t][i] != 0:
        potok += matset[t][i]
print('Поток: ')
print(potok)
#=====================================================================


