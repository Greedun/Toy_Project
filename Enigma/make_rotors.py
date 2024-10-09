import random

list_total = []
for i in range(5): # rotor의 종류
    #print(f"> {i}")
    list_rotor = ['' for j in range(53)]
    list_check = [-1 for k in range(27)] # 1+26 / 중복 방지용 
    
    for j in range(1,27):

        while(1):
            idx = (random.randint(1,26)) # A - Z idx+64
            
            if j == idx:
                continue

            #print(idx)
            if list_check[idx] == -1 :
                list_check[idx] = 1
                list_rotor[j] = idx # 1-26
                list_rotor[idx+26] = j # 27-52
                break
            else:
                continue
    list_rotor[0] = -1
    list_total.append(list_rotor)
    del list_rotor
    del list_check


# check
"""
for i in range(5):
    print(f"[{i}]")
    print(list_total[i][1:27])
    print(list_total[i][27:])
    print()
"""

# print
print("{")
for i in range(5):
    print("    ",end="{")
    print(list_total[i],end="}\n")
print("}")