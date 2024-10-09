import random

list_check = [-1 for i in range(27)]

for i in range(13):
    sel_one = 0
    sel_two = 0
    
    while (1):
        sel_one = random.randint(1,26)
    
        if list_check[sel_one] == -1:
            break

    while(1):
        sel_two = random.randint(1,26)
        
        if (sel_one == sel_two):
            continue
            
        if list_check[sel_two] == -1:
            break
    
    list_check[sel_one] = sel_two
    list_check[sel_two] = sel_one

print(list_check)
        