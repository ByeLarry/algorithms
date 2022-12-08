from random import randint

  
#--------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------

        
#1
#--------------------------------------------------------------------------------
def matrix_filling_input(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Невзвешенный')
    print('2)Ориентрированный ')
    print('3)Псевдограф(имеются петли)')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(0,1))
            if array[-1]==1:
                verge_array.append(1)
        matrix.append(array)
    f.write('====================Свойства графа:======================\n')
    f.write('1)Невзвешенный\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Псевдограф(имеются петли)\n')
#--------------------------------------------------------------------------------

    
#2
#--------------------------------------------------------------------------------
def matrix_filling_input_2(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Взвешенный')
    print('2)Ориентрированный ')
    print('3)Псевдограф(имеются петли)')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Взвешенный\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Псевдограф(имеются петли)\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(0,MaxValue))
            if array[-1] != 0:
                verge_array.append(1)
        matrix.append(array)
#--------------------------------------------------------------------------------
        

#3
#--------------------------------------------------------------------------------
def matrix_filling_input_3(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Невзвешенный')
    print('2)Неориентрированный ')
    print('3)Псевдограф(имеются петли)')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Невзвешенный\n')
    f.write('2)Неориентрированный\n')
    f.write('3)Псевдограф(имеются петли)\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(0,1))
            if array[-1] == 1:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if matrix[i][j]==1: #для неориентированных графов
                matrix[j][i] = 1
#--------------------------------------------------------------------------------

                
#4
#--------------------------------------------------------------------------------
def matrix_filling_input_4(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Взвешенный')
    print('2)Неориентрированный ')
    print('3)Псевдограф(имеются петли)')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Взвешенный\n')
    f.write('2)Неориентрированный\n')
    f.write('3)Псевдограф(имеются петли)\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(0,MaxValue))
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if matrix[i][j]!=0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
#--------------------------------------------------------------------------------


#5
#--------------------------------------------------------------------------------                
def matrix_filling_input_5(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Полный ')
    print('2)Неориентрированный')
    print('3)Мультиграф(не имеется петель)')
    print('4)Невзвешенный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Полный\n')
    f.write('2)Неориентрированный\n')
    f.write('3)Мультиграф(не имеется петель)\n')
    f.write('4)Невзвешенный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(1)
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if matrix[i][j]!=0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
            if (matrix[i][j]!=0) and (i==j): #для мультиграфа
                matrix[i][j] = 0
#--------------------------------------------------------------------------------  


#6
#--------------------------------------------------------------------------------                
def matrix_filling_input_6(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Полный ')
    print('2)Неориентрированный')
    print('3)Мультиграф(не имеется петель)')
    print('4)Взвешенный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Полный\n')
    f.write('2)Неориентрированный\n')
    f.write('3)Мультиграф(не имеется петель)\n')
    f.write('4)Взвешенный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(1,MaxValue))
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if matrix[i][j]!=0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
            if (matrix[i][j]!=0) and (i==j): #для мультиграфа
                matrix[i][j] = 0
#--------------------------------------------------------------------------------  


#7
#--------------------------------------------------------------------------------                
def matrix_filling_input_7(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Полный ')
    print('2)Ориентрированный')
    print('3)Мультиграф(не имеется петель)')
    print('4)Невзвешенный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Полный\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Мультиграф(не имеется петель)\n')
    f.write('4)Невзвешенный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(1)
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if (matrix[i][j]!=0) and (i==j): #для мультиграфа
                matrix[i][j] = 0
#--------------------------------------------------------------------------------  


#8
#--------------------------------------------------------------------------------                
def matrix_filling_input_8(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Полный ')
    print('2)Ориентрированный')
    print('3)Мультиграф(не имеется петель)')
    print('4)Взвешенный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Полный\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Мультиграф(не имеется петель)\n')
    f.write('4)Взвешенный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(1, MaxValue))
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if (matrix[i][j]!=0) and (i==j): #для мультиграфа
                matrix[i][j] = 0    
#--------------------------------------------------------------------------------  


#9
#--------------------------------------------------------------------------------                
def matrix_filling_input_9(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Полный ')
    print('2)Неориентрированный')
    print('3)Псевдограф(имеются петли)')
    print('4)Невзвешенный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Полный\n')
    f.write('2)Неориентрированный\n')
    f.write('3)Псевдограф(имеются петли)\n')
    f.write('4)Невзвешенный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(1)
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if matrix[i][j]!=0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
            if (matrix[i][j]==0) and (i==j):
                matrix[i][j] = randint(1, MaxValue)
#--------------------------------------------------------------------------------  


#10
#--------------------------------------------------------------------------------                
def matrix_filling_input_10(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Полный ')
    print('2)Неориентрированный')
    print('3)Псевдограф(имеются петли)')
    print('4)Взвешенный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Полный\n')
    f.write('2)Неориентрированный\n')
    f.write('3)Псевдограф(имеются петли)\n')
    f.write('4)Взвешенный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(1,MaxValue))
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if matrix[i][j]!=0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
            if (matrix[i][j]==0) and (i==j):
                matrix[i][j] = randint(1, MaxValue)   
#--------------------------------------------------------------------------------  


#11
#--------------------------------------------------------------------------------                
def matrix_filling_input_11(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Полный ')
    print('2)Ориентрированный')
    print('3)Псевдограф(имеются петли)')
    print('4)Невзвешенный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Полный\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Псевдограф(имеются петли)\n')
    f.write('4)Невзвешенный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(1)
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if matrix[i][j]!=0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
            if (matrix[i][j]==0) and (i==j):
                matrix[i][j] = randint(1, MaxValue)   
#--------------------------------------------------------------------------------  


#12
#--------------------------------------------------------------------------------                
def matrix_filling_input_12(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Полный ')
    print('2)Ориентрированный')
    print('3)Псевдограф(имеются петли)')
    print('4)Взвешенный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Полный\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Псевдограф(имеются петли)\n')
    f.write('4)Взвешенный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(1, MaxValue))
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
           if (matrix[i][j]==0) and (i==j):
                matrix[i][j] = randint(1, MaxValue)   
#--------------------------------------------------------------------------------  


#13
#--------------------------------------------------------------------------------
def matrix_filling_input_13(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Невзвешенный')
    print('2)Ориентрированный ')
    print('3)Мультиграф(не имеется петель)')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Невзвешенный\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Мультиграф(не имеется петель)\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(0,1))
            if array[-1]==1:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
           if (matrix[i][j]!=0) and (i==j): #для мультиграфа
                matrix[i][j] = 0
#--------------------------------------------------------------------------------
    

#14
#--------------------------------------------------------------------------------

def matrix_filling_input_14(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Взвешенный')
    print('2)Ориентрированный ')
    print('3)Мультиграф(не имеется петель)')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Взвешенный\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Мультиграф(не имеется петель)\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(0,MaxValue))
            if array[-1] != 0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
           if (matrix[i][j]!=0) and (i==j): #для мультиграфа
                matrix[i][j] = 0 
#--------------------------------------------------------------------------------
        
#15
#--------------------------------------------------------------------------------
def matrix_filling_input_15(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Невзвешенный')
    print('2)Неориентрированный ')
    print('3)Мультиграф(не имеется петель)')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Невзвешенный\n')
    f.write('2)Неориентрированный\n')
    f.write('3)Мультиграф(не имеется петель)\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(0,1))
            if array[-1] == 1:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column):
            if matrix[i][j]==1: #для неориентированных графов
                matrix[j][i] = 1
            if (matrix[i][j]!=0) and (i==j): #для мультиграфа
                matrix[i][j] = 0               
#--------------------------------------------------------------------------------
                

#16
#--------------------------------------------------------------------------------
def matrix_filling_input_16(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Взвешенный')
    print('2)Неориентрированный ')
    print('3)Мультиграф(не имеется петель)')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Взвешенный\n')
    f.write('2)Неориентрированный\n')
    f.write('3)Мультиграф(не имеется петель)\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(randint(0,MaxValue))
            if array[-1]!=0:
                verge_array.append(1)
        matrix.append(array)
    for i in range(row):
        for j in range(column): 
            if matrix[i][j]!=0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
            if (matrix[i][j]!=0) and (i==j): #для мультиграфа
                matrix[i][j] = 0 
#--------------------------------------------------------------------------------


#17
#--------------------------------------------------------------------------------
def matrix_filling_input_17(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Дерево')
    print('2)Ориентрированный ')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Дерево\n')
    f.write('2)Ориентрированный\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(0)
        matrix.append(array)
    matrix[0][1] = 1
    verge_array.append(1)
    i = 1
    j = 1
    while (i < len(matrix[0])-2) and (j <= len(matrix[0])-3):
        matrix[i][j+1] = 1
        matrix[i][j+2] = 1
        verge_array.append(1)
        verge_array.append(1)
        j += 2
        i += 1
    verge_array.append(1)
    if len(matrix[0])%2 == 1:
           matrix[i][j+1] = 1
           verge_array.append(1)
#--------------------------------------------------------------------------------


#18
#--------------------------------------------------------------------------------
def matrix_filling_input_18(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Дерево')
    print('2)Ориентрированный ')
    print('3)Взвешенное')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Дерево\n')
    f.write('2)Ориентрированный\n')
    f.write('3)Взвешенное\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(0)
        matrix.append(array)
    matrix[0][1] = randint(1,MaxValue)
    verge_array.append(randint(1,MaxValue))
    i = 1
    j = 1
    while (i < len(matrix[0])-2) and (j <= len(matrix[0])-3):
        matrix[i][j+1] = randint(1,MaxValue)
        matrix[i][j+2] = randint(1,MaxValue)
        verge_array.append(1)
        verge_array.append(1)
        j += 2
        i += 1
    verge_array.append(1)
    if len(matrix[0])%2 == 1:
           matrix[i][j+1] = 1
           verge_array.append(1)
#--------------------------------------------------------------------------------


#19
#--------------------------------------------------------------------------------
def matrix_filling_input_19(matrix): # заполнение матрицы смежности
    global incoherent
    incoherent = True
    print('====================Свойства графа:======================')
    print('1)Несвязный')
    print('2)Невзвешенный')
    print('3)Ориентрированный ')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Несвязный\n')
    f.write('2)Невзвешенный\n')
    f.write('3)Ориентрированный\n')
    for i in range(row-1):
        array = []
        for j in range(column-1):
            array.append(randint(0,1))
            if array[-1]==1:
                verge_array.append(1)
        array.append(0)
        verge_array.append(1)
        matrix.append(array)
    array1 = []
    for i in range(row):
        array1.append(0)
    matrix.append(array1)
#--------------------------------------------------------------------------------


#20
#--------------------------------------------------------------------------------
def matrix_filling_input_20(matrix): # заполнение матрицы смежности
    global incoherent
    incoherent = True
    print('====================Свойства графа:======================')
    print('1)Несвязный')
    print('2)Взвешенный')
    print('3)Ориентрированный ')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Несвязный\n')
    f.write('2)Взвешенный\n')
    f.write('3)Ориентрированный\n')
    for i in range(row-1):
        array = []
        for j in range(column-1):
            array.append(randint(0,MaxValue))
            if array[-1]==1:
                verge_array.append(1)
        array.append(0)
        verge_array.append(1)
        matrix.append(array)
    array1 = []
    for i in range(row):
        array1.append(0)
    matrix.append(array1)
#--------------------------------------------------------------------------------


#21
#--------------------------------------------------------------------------------
def matrix_filling_input_21(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Дерево')
    print('2)Неориентированное')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Дерево\n')
    f.write('2)Неориентированное\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(0)
        matrix.append(array)
    matrix[0][1] = 1
    verge_array.append(1)
    i = 1
    j = 1
    while (i < len(matrix[0])-2) and (j <= len(matrix[0])-3):
        matrix[i][j+1] = 1
        matrix[i][j+2] = 1
        verge_array.append(1)
        verge_array.append(1)
        j += 2
        i += 1
    verge_array.append(1)
    if len(matrix[0])%2 == 1:
           matrix[i][j+1] = 1
           verge_array.append(1)
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 1: #для неориентированных графов
                matrix[j][i] = 1
#--------------------------------------------------------------------------------


#22
#--------------------------------------------------------------------------------
def matrix_filling_input_22(matrix): # заполнение матрицы смежности
    print('====================Свойства графа:======================')
    print('1)Дерево')
    print('2)Взвешенное')
    print('3)Неориентированное')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Дерево\n')
    f.write('2)Взвешенное\n')
    f.write('3)Неориентированное\n')
    for i in range(row):
        array = []
        for j in range(column):
            array.append(0)
        matrix.append(array)
    matrix[0][1] = randint(1,MaxValue)
    verge_array.append(randint(1,MaxValue))
    i = 1
    j = 1
    while (i < len(matrix[0])-2) and (j <= len(matrix[0])-3):
        matrix[i][j+1] = randint(1,MaxValue)
        matrix[i][j+2] = randint(1,MaxValue)
        verge_array.append(1)
        verge_array.append(1)
        j += 2
        i += 1
    verge_array.append(1)
    if len(matrix[0])%2 == 1:
           matrix[i][j+1] = 1
           verge_array.append(1)
    for i in range(row):
        for j in range(column):
            if matrix[i][j] != 0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
#--------------------------------------------------------------------------------


#23
#--------------------------------------------------------------------------------
def matrix_filling_input_23(matrix): # заполнение матрицы смежности
    global incoherent
    incoherent = True
    print('====================Свойства графа:======================')
    print('1)Несвязный')
    print('2)Взвешенный')
    print('3)Неориентированный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Несвязный\n')
    f.write('2)Взвешенный\n')
    f.write('3)Неориентированный\n')
    for i in range(row-1):
        array = []
        for j in range(column-1):
            array.append(randint(0,MaxValue))
            if array[-1]==1:
                verge_array.append(1)
        array.append(0)
        verge_array.append(1)
        matrix.append(array)
    array1 = []
    for i in range(row):
        array1.append(0)
    matrix.append(array1)
    for i in range(row-1):
        for j in range(column-1):
            if matrix[i][j] != 0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
#--------------------------------------------------------------------------------



#24
#--------------------------------------------------------------------------------
def matrix_filling_input_24(matrix): # заполнение матрицы смежности
    global incoherent
    incoherent = True
    print('====================Свойства графа:======================')
    print('1)Несвязный')
    print('2)Невзвешенный')
    print('3)Неориентированный')
    f.write('====================Свойства графа:======================\n')
    f.write('1)Несвязный\n')
    f.write('2)Невзвешенный\n')
    f.write('3)Неориентированный\n')
    for i in range(row-1):
        array = []
        for j in range(column-1):
            array.append(randint(0,1))
            if array[-1]==1:
                verge_array.append(1)
        array.append(0)
        verge_array.append(1)
        matrix.append(array)
    array1 = []
    for i in range(row):
        array1.append(0)
    matrix.append(array1)
    for i in range(row-1):
        for j in range(column-1):
            if matrix[i][j] != 0: #для неориентированных графов
                matrix[j][i] = matrix[i][j]
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
def print_list(matrix): # вывод списка смежности
    global incoherent
    print('====================Список_смежности:===================')
    f.write('====================Список_смежности:===================\n')
    for i in range(row):
        if sum(matrix[i]) !=0:
            print('[{}]'.format(i+1), end = '')
            f.write('['+str(i+1)+']')
        for j in range(column):
            if matrix[i][j]!=0:
                print('{} '.format(verge_array[j]), end='')
                f.write(str(verge_array[j])+' ')
        if sum(matrix[i]) !=0:
            f.write('\n')
            print()
    if (sum(matrix[len(matrix[0])-1]) == 0) and (incoherent == True):
        print('[{}]'.format(i+1))
        f.write('['+str(i+1)+']'+'\n')
    print('========================================================')
    f.write('========================================================\n')
    incoherent = False
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
def sample(path):
    global graph_verge 
    global verge_array   
    global mat
    global f
    global incoherent


    graph_verge = 1
    verge_array = []    
    mat = []
    f = open(path,'w', encoding="UTF-8")


    if (path[0] == '1') and (path[1] == ')'):
        matrix_filling_input(mat)#1
    elif (path[0] == '2')and (path[1] == ')') :
        matrix_filling_input_2(mat)#2
    elif path[0] == '3':
        matrix_filling_input_3(mat)#3
    elif path[0] == '4':
        matrix_filling_input_4(mat)#4
    elif path[0] == '5':
        matrix_filling_input_5(mat)#5
    elif path[0] == '6':
        matrix_filling_input_6(mat)#6
    elif path[0] == '7':
        matrix_filling_input_7(mat)#7
    elif path[0] == '8':
        matrix_filling_input_8(mat)#8
    elif path[0] == '9':
        matrix_filling_input_9(mat)#9
    elif (path[0] == '1') and (path[1] == '0'):
        matrix_filling_input_10(mat)#10
    elif (path[0] == '1') and (path[1] == '1'):
        matrix_filling_input_11(mat)#11
    elif (path[0] == '1') and (path[1] == '2'):
        matrix_filling_input_12(mat)#12
    elif (path[0] == '1') and (path[1] == '3'):
        matrix_filling_input_13(mat)#13
    elif (path[0] == '1') and (path[1] == '4'):
        matrix_filling_input_14(mat)#14
    elif (path[0] == '1') and (path[1] == '5'):
        matrix_filling_input_15(mat)#15
    elif (path[0] == '1') and (path[1] == '6'):
        matrix_filling_input_16(mat)#16
    elif (path[0] == '1') and (path[1] == '7'):
        matrix_filling_input_17(mat)#17
    elif (path[0] == '1') and (path[1] == '8'):
        matrix_filling_input_18(mat)#18
    elif (path[0] == '1') and (path[1] == '9'):
        matrix_filling_input_19(mat)#19
    elif (path[0] == '2') and (path[1] == '0'):
        matrix_filling_input_20(mat)#20
    elif (path[0] == '2') and (path[1] == '1'):
        matrix_filling_input_21(mat)#21
    elif (path[0] == '2') and (path[1] == '2'):
        matrix_filling_input_22(mat)#22
    elif (path[0] == '2') and (path[1] == '3'):
        matrix_filling_input_23(mat)#23
    elif (path[0] == '2') and (path[1] == '4'):
        matrix_filling_input_24(mat)#24
    print_matrix(mat)
    for i in range(1,len(verge_array)):
        verge_array[i] = verge_array[i] + graph_verge
        graph_verge += 1
    print_list(mat)
    f.close()
#--------------------------------------------------------------------------------

        
#--------------------------------------------------------------------------------
#Можно изменить
MinNM = 6 #При значении ниже 6 могут быть проблемы
MaxNM = 15
MaxValue = 4 #Максимальное значение для ребер взвешенного графа
#--------------------------------------------------------------------------------
incoherent = False #логическая переменная для несвязных графов
Inp = ''
while (Inp != 'e'): 
    RandomNM = input('Введите "R" если хотите случайное N:\n')
    if (RandomNM == 'r') or (RandomNM == 'R'):
        row = randint(MinNM, MaxNM) # кол-во ребер(m)
        column = row  # кол-во вершин(n)
    else:   
        row = int(input('Ввод N: ')) # кол-во ребер(m)
        column = row # кол-во вершин(n)


    if (row <= MaxNM) and (column <= MaxNM) and (row >= MinNM) and (column >= MinNM):
        sample('1)Невзвешенный ориентированный псевдограф.txt')
        sample('2)Взвешенный ориентированный псевдограф.txt')
        sample('3)Невзвешенный неориентированный псевдограф.txt')
        sample('4)Взвешенный неориентированный псевдограф.txt')
        sample('5)Полный невзвешенный неориентированный мультиграф.txt')
        sample('6)Полный взвешенный неориентированный мультиграф.txt')
        sample('7)Полный невзвешенный ориентированный мультиграф.txt')
        sample('8)Полный взвешенный ориентированный мультиграф.txt')
        sample('9)Полный невзвешенный неориентированный псевдограф.txt')
        sample('10)Полный взвешенный неориентированный псевдограф.txt')
        sample('11)Полный невзвешенный ориентированный псевдограф.txt')
        sample('12)Полный взвешенный ориентированный псевдограф.txt')
        sample('13)Невзвешенный ориентированный мультиграф.txt')
        sample('14)Взвешенный ориентированный мультиграф.txt')
        sample('15)Невзвешенный неориентированный мультиграф.txt')
        sample('16)Взвешенный неориентированный мультиграф.txt')
        sample('17)Дерево классическое( ориентированный ).txt')
        sample('18)Дерево взвешенное( ориентированный ).txt')
        sample('19)Несвязный невзвешенный ориентированный граф.txt')
        sample('20)Несвязный взвешенный ориентированный граф.txt')
        sample('21)Неориентированное дерево.txt')
        sample('22)Неориентированное взвешенное дерево.txt')
        sample('23)Несвязный взвешенный неориентированный граф.txt')
        sample('24)Несвязный невзвешенный неориентированный граф.txt')
    elif (row > MaxNM) or (column > MaxNM):
        print(' ','Ошибка!', 'Введите значения поменьше!' ,sep='\n')
    elif (row < MinNM) or (column < MinNM):
        print(' ','Ошибка!', 'Введите значения побольше!' ,sep='\n')
    print('Для продолжения нажмите Enter')
    Inp = input()
