""" class vertex:
    def __init__(self) -> None:
        self.color = color
        self.kolsmej = kolsmej
        self.smej = smej
     """




#=====================================================================
def reading(path): 
    """перевод из текстового файла в двумерный массив типа int"""
    global mat
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
    i = 0
    while i != len(mat):
        for j in range(len(mat[1])):
            mat[i][j] = int(mat[i][j])
        i += 1  
#=====================================================================


#=====================================================================
def dfs2(v, to):
    visited[v] = True
    colors[v] = to
    for i in range(n):
        if mat[v][i] != 0 or mat[i][v] != 0:
            if not(visited[i]):
                if to == 1:
                    dfs2(i, 2)
                else:
                    dfs2(i, 1)
            else:
                if colors[i] ==to:
                    dvydol = False
#=====================================================================


#=====================================================================
def dfs3(v):
    visited[v] = True
    z = 0
    for i in range(n):
        if mat[v][i] != 0:
            if not(visited[i]) and not(dopsep):
                if par[i] == 1:
                    if (colors[v] == 2 and t[v] == i) or (colors[v] == 1 and t[i] != v):
                        dfs3(i)
                        if dopsep:
                            if colors[v] == 2:
                                if t[v] == i:
                                    t[v] = 0
                                    par[v] = 1
                                else:
                                    if t[v] == 0:
                                        t[v] = i
                                        par[v] = 1
                            else:
                                if t[i] == v:
                                    t[i] = 0
                                    par[v] = 1
                                else:
                                    if t[i] == 0:
                                        t[i] = v
                                        par[v] = 1
                else:
                    dopsep = True
                    par[i] = 1
                    t[i] = v        
#=====================================================================


mat = []
path = input('Введите название файла: ') + '.txt'
reading(path)
n = len(mat)
par = [0] * n
d1 = [0] * n
d2 = [0] * n
t = [0] * n
colors = [0] * n
a = [0] * n
dvydol = True
visited = [False] * len(mat)
k1 = k2 = 0
firstv = []
secondv = []
for i in range(n):
    if i <= n//2:
        firstv.append(i)
    else:
        secondv.append(i)
for  i in range(n):
    if i <= n//2-1:
        colors[i] = 1
    else:
        colors[i] = 2
copcolors = colors

#=====================================================================
g = mat
for i in range(n):
    for j in range(n):
        g[i][j] = 0
#=====================================================================
dfs2(0,0)

if dvydol:
    #костыль
    for  i in range(n):
        if i <= n//2-1:
            colors[i] = 1
        else:
            colors[i] = 2
    print(colors, 'colors')
    k1, k2 = 0, 0
    for i in range(n):
        d1[i] = 0
        d2[i] = 0
        t[i] = 0
    for i in range(n):
        a[i] = 0
        if colors[i] == 1:
            k1 += 1
            d1[k1-1] = i
            print(d1, 'd1')
            for j in range(n):
                if mat[i][j] != 0:
                    g[i][j] = 1
        else:
            k2 += 1
            d2[k2-1] = i
            print(d2, 'd2')
    print(d1,'d1')
    print(d2, 'd2')
    print(copcolors, 'colors')
    print(f'Вершины первой доли: ', end='')
    for i in range(k1):
        print(i, end=' ')
        print()
    print(f'Вершины второй доли: ', end='')
    for i in range(k2):
        print(i, end=' ')
        print()
    #down
    for i in range(n):
        par[i] = 0
    m = 0
    for i in range(k1):
        c = 0
        for j in range(k2):
            if mat[d1[i]][d2[j]] != 0 and par[d2[j]] == 0 and par[d1[i]] == 0:
                par[d1[i]] = 1 
                par[d2[j]] = 1
                m += 1
                t[d2[j]] = d1[i]
                c = 1
        if c == 0:
            dopsep = False
            for z in range(n):
                visited[z] = False
            start = i
            dfs3(d1[i]) 
    print('Паросочетания: ', end='')
    for i in range(n):
        if t[i] != 0:
            print(f'{t[i]} - {i}')
    print(t)