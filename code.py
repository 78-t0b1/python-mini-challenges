# --------------
#Code starts here
def palindrome(num):
    x = [str(y) for y in str(num)]
    l = len(x)
    if l%2 == 0:
        for p in range(int(l/2)):
            
            if x[p]==x[(l-1)-p]:
                pass

            else:
                q=x[(l-1)-p]
                x[(l-1)-p]=x[p]
                if int(''.join(x))<num:
                    x[(l-1)-p]=q
                    x[p]=q

    else:
        x[int(l/2)]=str(int(x[int(l/2)])+1)
        for p in range(int(l/2)):
            
            
            if x[p]==x[(l-1)-p]:
                pass

            else:
                x[(l-1)-p]=x[p]

    return(int(''.join(x)))     

a = palindrome(12)    
print(a)      

    # if x[0]==x[-1]:




# --------------
#Code starts here
def a_scramble(str_1, str_2):
    x = [p for p in str_1.lower()]
    y = [p for p in str_2.lower()]
    print(x)
    print(y)
    for p in y:
        if p in x:
            x.remove(p)
            pass

        else:
            return False

    return True

print(a_scramble("Tom Marvolo Riddle","Voldemort"))


# --------------
#Code starts here
def check_fib(num):
    x=1
    y=1
    while (1):
        a=x
        x = x+y
        if x >= num:
            break
        y=a
    print(x)
    return x == num

print(check_fib(13))


# --------------
#Code starts here
def compress(word):
    
    word = word.lower()
    print(word)
    n = 0
    l = []
    for p in range(len(word)-1):
       

        if word[p]==word[p+1]:
            n+=1

        else:
            n+=1
            l.append(word[p]+str(n))
            n=0

    
    l.append(word[-1]+str(n+1))

    return (''.join(l))

print(compress("Ssass"))
            




# --------------
#Code starts here
def k_distinct(string,k):
    l=[]
    string = string.lower()
    
    for i in string:
        if i not in l:
            l.append(i)
            
    print(l)
    print(len(l))
    return len(l)==k

k_distinct('Messoptamia',8)

            
    


