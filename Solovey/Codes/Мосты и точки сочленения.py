import random
#=====================================================================
def print_matrix(matrix): # вывод матрицы смежности
    global incoherent
    print('====================Матрица_смежности:===================')
    f.write('====================Матрица_смежности:===================\n')
    for i in range(row):
        for j in range(column):
            if (sum(matrix[i]) != 0) and (incoherent == False):
                print(matrix[i][j], end = ' ')
                f.write(str(matrix[i][j])+' ')
            if (incoherent == True):
                print(matrix[i][j], end = ' ')
                f.write(str(matrix[i][j])+' ')
        if (sum(matrix[i]) != 0) and (incoherent == False) :
            f.write('\n')
            print()
        if (incoherent == True):
            f.write('\n')
            print()
#=====================================================================


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
def dfs(v, p=-1):# v - вершина; p - предок
    global timer
    used[v] = True # used[v] - запоминание посещенных вершин
    tin[v] = timer # tin[v] - время входа в вершину 
    timer += 1 # переменная времени(увеличивается при спуске)
    tup[v] = tin[v] # tup[v] - время минимального подъема
    for to in adj_list[v]: # adj_list[v] - матрица связи вершин
        if to == p:  continue # to - индекс вершин, по которым происходит обход
        if (used[to]):# если побывали в вершине
            tup[v] = min(tup[v], tin[to]) # обновление tup, так как вершина уже посещена 
        else:
            dfs(to, v)
            tup[v] = min(tup[v], tup[to])
            if tup[to] > tin[v]: # проверка на мост 
                print('Мост находится в точках:',to + 1, v + 1)
            if tup[to] >= tin[v] and p != -1: # проверка на точку сочленения 
                dots.append(v + 1)
    """ if (p == -1) and len(dots) > 0:
        dots.append(v + 1) # dots - массив точек сочленения  """
#=====================================================================


input_path = ''
while (input_path != 'e') or (input_path != 'у'):
    mat = []
    input_path = str(input('\nВставьте имя текстового документа: \n'))
    if input_path[len(input_path)-4] != '.':
        input_path = input_path + '.txt'
    reading(input_path)
    flag = False
    for i in range(len(mat[0])):
        for j in range(len(mat[0])):
            if mat[i][j] != mat[j][i]:
                flag = True
    if flag == False:
        N = len(mat[0])
        tup, tin = [0] * N, [0] * N
        adj_list = []
        used = [False] * N
        timer = 0
        dots = [] # точки сочленения
        for i in range(len(mat[0])):
            b = []
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    b.append(j)
            adj_list.append(b) 
        dfs(random.randint( 0, len(mat[0]) ))
        dots = sorted(dots)
        print('Точки сочленения:',*set(dots))
    else:
        print('Граф ориентированный!')

print()