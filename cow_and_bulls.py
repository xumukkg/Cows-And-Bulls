import random
n = random.randint(1000, 9999)
print('Welcome to the Cows and Bulls Game! ')
string_n = str(n)
print()
print("To close the game print \'exit\' \n ")
while True:
    user = str(input('Enter a number \n>>> '))

    bulls =(set(user) & set(string_n))
    if user == "exit":
        break

    elif len(user)==len(string_n):
        count = 0
        i=0
        while i<len(string_n):
            if string_n[i]==user[i]:
                count+=1
            i+=1
        if count==len(string_n):
            
            print("You win!")
            break
    

        print("%s cows, %s bulls" % (count, len(bulls)-count))
        

    
    

