array = [[-1, 4, 3],
         [-1, 6, 3],
         [-1, 4, 3]]

for j in range(0, len(array)):
    string = ''
    num = None
    equals = True
    for i in range(0, len(array[j])):
        string += str(array[i][j])
        if num == None:
            num = array[i][j]
        else:
            if num != array[i][j]:
                equals = False
    if equals:
        print(string)