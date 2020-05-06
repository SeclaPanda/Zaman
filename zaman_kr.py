n = int(input('Enter N: ')) #User input list size
s = [] #initiate list
for a in range(n): #list pass for add number into list
    b = int(input('Enter number: ')) #User input number 
    s.append(b) #Add user number in list
big = s[0] #initiate max element of list 
count = 0 #initiate count of max element
for a in range(len(s)): #list pass for doing ex
    if big < s[a]: #Check equal of max and current list number
        big = s[a]
for a in range(len(s)):    
    if big == s[a]: #Check equal for count
        count += 1
print(f'Max number in list: {big}. Count of max number in list is: {count}.') #Answer output