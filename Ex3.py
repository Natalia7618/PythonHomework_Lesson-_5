# Создайте программу для игры в ""Крестики-нолики"".

fields = [1,2,3,
        4,5,6,
        7,8,9]

victories_terms = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
def print_fields():
    print(fields[0], end = " ")
    print(fields[1], end = " ")
    print(fields[2])
 
    print(fields[3], end = " ")
    print(fields[4], end = " ")
    print(fields[5])
 
    print(fields[6], end = " ")
    print(fields[7], end = " ")
    print(fields[8])
     
def step_fields(step,symbol):
    ind = fields.index(step)
    fields[ind] = symbol
 
def get_result():
    win = ""
    for i in victories_terms:
        if fields[i[0]] == "X" and fields[i[1]] == "X" and fields[i[2]] == "X":
            win = "X"
        if fields[i[0]] == "O" and fields[i[1]] == "O" and fields[i[2]] == "O":
            win = "O"         
    return win
 
def check_line(sum_O,sum_X):
    step = ""
    for line in victories_terms:
        o = 0
        x = 0
        for j in range(0,3):
            if fields[line[j]] == "O":
                o = o + 1
            if fields[line[j]] == "X":
                x = x + 1
        if o == sum_O and x == sum_X:
            for j in range(0,3):
                if fields[line[j]] != "O" and fields[line[j]] != "X":
                    step = fields[line[j]]              
    return step
 
def comp_step():        
    step = ""
    step = check_line(2,0)
    if step == "":
        step = check_line(0,2)        
    if step == "":
        step = check_line(1,0)           
    if step == "":
        if fields[4] != "X" and fields[4] != "O":
            step = 5           
    if step == "":
        if fields[0] != "X" and fields[0] != "O":
            step = 1           
    return step
 
game_over = False
human = True
 
while game_over == False:
    print_fields()
    if human == True:
        symbol = "X"
        step = int(input("Ваш ход: "))
    else:
        print("Ход компьютера: ")
        symbol = "O"
        step = comp_step()
    if step != "":
        step_fields(step,symbol) 
        win = get_result() 
        if win != "":
            game_over = True
            win = 'компьютер'
        else:
            game_over = False
    else:
        print("Ничья!")
        game_over = True
        win = "мир"
    human = not(human)        
 
print_fields()
print("Победил", win) 

