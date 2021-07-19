source = [3,2,1]
aux = []
target = []
moves = 1

print("\n\t\t\t Tower of Hanoi Puzzal...\n")
print("\t\t Minimum Moves   7\t Maximum Moves  21")
print("this is your initial state of rods......\n")
print('source','Auxiliery','target',sep = '\t    ')
print()
for i in range(len(source),-1,-1):
    if(i == 3):
        print('  |','|','|',sep = '\t\t')
    else:
        print('  ',end='')
        print(source[i],'|','|',sep = '\t\t')


print("\n Start to Play .....\n")

while True:
    if(moves != 1):
        print('Stacks are:\tSource: ',source,' Auxiliry: ',aux,' Target: ',target)
    print("\nthis is your ", moves," move\n")
    if moves ==1 or len(source) == 3:
        print("in which stack you want to move top element of stack source....")
        b = int(input("Enter 1 for Aux and 2 for target"))
        if b == 1:
            aux.append(source.pop())
        else:
            target.append(source.pop()) 
    else:
        print("\nfrom which stack you want to move top element of stack ....")
        if(len(source)!= 0 and len(aux) != 0 and len(target) == 0):
            s= input("Enter 's' for source Enter x for Auxiliry.....")
            print("\nEnter stack in which you want to move")
            if s == 's':
                b = int(input("Enter 1 for Aux and 2 for target "))
                print()
                if a == 1:
                    if source[len(source)-1] < aux[len(aux)-1]:
                        aux.append(source.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                elif b == 2:
                    target.append(source.pop())
            elif s == 'x':
                 b = int(input("Enter 3 for source and 2 for target "))
                 if b == 3:
                    if source[len(source)-1] > aux[len(aux)-1]:
                        source.append(aux.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                 elif b == 2:
                    target.append(aux.pop())
        elif(len(source)!= 0 and len(aux) == 0 and len(target) != 0):
            s= input("Enter 's' for source Enter t for Target.....")
            print("\nEnter stack in which you want to move")
            if s == 's':
                b = int(input("Enter 1 for Aux and 2 for target "))
                print()
                if b == 2:
                    if source[len(source)-1] < target[len(target)-1]:
                        target.append(source.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                elif b == 1:
                    aux.append(source.pop())
            elif s == 't':
                 b = int(input("Enter 3 for source and 1 for Auxiliry "))
                 if b == 3:
                    if source[len(source)-1] > target[len(target)-1]:
                        source.append(aux.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                 elif a == 1:
                    aux.append(target.pop())
        elif(len(source)== 0 and len(aux) != 0 and len(target) != 0):
            s= input("Enter 'x' for Auxiliry Enter 't' for Target.....")
            print("\nEnter stack in which you want to move")
            if s == 'x':
                b = int(input("Enter 3 for Source and 2 for Target "))
                print()
                if b == 2:
                    if aux[len(aux)-1] < target[len(target)-1]:
                        target.append(aux.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                elif b == 3:
                    source.append(aux.pop())
            elif s == 't':
                 b = int(input("Enter 3 for source and 1 for Auxiliry "))
                 if b == 1:
                    if aux[len(aux)-1] > target[len(target)-1]:
                        aux.append(target.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                 elif b == 3:
                    source.append(target.pop())            
        elif(len(source)!= 0 and len(aux) != 0 and len(target) != 0):
            s= input("Enter 's' for source Enter x for Auxiliry and t for Target.....")
            print("\nEnter stack in which you want to move")
            if s == 's':
                b = int(input("Enter 1 for Aux and 2 for target "))
                print()
                if a == 1:
                    if source[len(source)-1] < aux[len(aux)-1]:
                        aux.append(source.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                elif b == 2:
                    if source[len(source)-1] < target[len(target)-1]:
                        target.append(source.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
            elif s == 'x':
                 b = int(input("Enter 3 for source and 2 for target "))
                 if b == 3:
                    if source[len(source)-1] > aux[len(aux)-1]:
                        source.append(aux.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                 elif b == 2:
                     if target[len(target)-1] > aux[len(aux)-1]:
                         target.append(aux.pop())
                     else:
                         print("\n you can not move large element into smaller ..... move not possible")
            elif s == 't':
                 b = int(input("Enter 3 for source and 1 for Auxiliry "))
                 if b == 3:
                    if source[len(source)-1] > target[len(target)-1]:
                        source.append(target.pop())
                    else:
                        print("\n you can not move large element into smaller ..... move not possible")
                 elif b == 1:
                     if aux[len(aux)-1] > target[len(target)-1]:
                         aux.append(target.pop())
                     else:
                         print("\n you can not move large element into smaller ..... move not possible")
                 
    
    if(moves > 21 or (moves != 1 and len(target) == 3)):
        break
    moves = moves+1

print(source,aux,target)      
if moves > 21:
    print("\n.. you exceed your maximum limit\nSorry ..... better luck next time.....")
else:
    print("Congratulation.... you won this puzzal in ", moves)
    if (moves == 7):
        print("Wow .... you solved in minimum number of moves....heades off")
    print("\nFinal ..... Tower Of Hanoi ......\n\n")
    print('source','Auxiliery','target',sep = '\t    ')
    print()
    for i in range(len(target),-1,-1):
        if(i == 3):
            print('  |','|','|',sep = '\t\t')
        else:
            print('  ',end='')
            print('|','|',target[i],sep = '\t\t')

input()
