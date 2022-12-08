import random
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
def dfs(v: int): 
    """обход в глубину"""
    visited_dfs[v] = True
    i = 0
    while i < len(mat):  
        if (mat[v][i] != 0  or mat[i][v] != 0 ) and visited_dfs[i] == False:
            dfs(i)
        i += 1
#=====================================================================



#=====================================================================
def bfs(v): 
    """обход в ширину"""
    q = []
    visited_bfs = [False] * len(mat[0])
    visited_bfs[v] = True
    d = [0] * len(mat[0])
    q.append(v)
    while q:
        v = q.pop(0)
        i = 0
        while i < len(mat[0]):
            if v >= len(mat):
                break
            if mat[v][i] != 0 and visited_bfs[i] == False:
                q.append(i)
                visited_bfs[i] = True
                d[i] = d[v] + 1
            i += 1
    return d
#=====================================================================



#=====================================================================
def find_components(v, count=1):  
    """поиск компонентов связности в глубину"""
    dfs(v)
    for i in range(len(visited_dfs)):
        if not visited_dfs[i]:
            count += 1
            dfs(i)
    return count
#=====================================================================



#=====================================================================
def number_of_absolute_sinks(): 
    """количество абсолютных стоков в орграфе обходом в ширину"""
    array = []
    subarray = []
    i = 0
    while i < len(mat):
        array.append(bfs(i))
        i += 1
    i = 0
    while i < len(mat):
        count = 0
        for j in range(len(array[0])):
            if array[i][j] != 0 and i != j and array[j][i] != 0:
                count += 1
        subarray.append(count)
        i += 1
    a = len(subarray)
    if (mat[len(mat)-1][len(mat[0])-2] == 0) and (len(mat) < len(mat[0])):
        a -= 1
    return a - subarray.count(0)   
#=====================================================================



input_path = ''
while (input_path != 'e') or (input_path != 'у'):
    mat = []
    input_path = str(input('\nВставьте имя текстового документа: \n'))
    if input_path[len(input_path)-4] != '.':
        input_path = input_path + '.txt'
    reading(input_path)
    visited_bfs = []
    visited_dfs = [False] * len(mat)
    print('Число компонентов связности равно:', find_components(random.randint(0, (len(mat[0]) - 1))//2))
    if (' ориентированный' in input_path) or ('test' in input_path):
        print('Количество абсолютных стоков в орграфе:', number_of_absolute_sinks())

    else:
        print('Граф должен быть ориентированным!!!\n')

