a = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
print("Enter those many elements: ")
for i in range(0, n): 
    x = int(input()) 
  
    a.append(x)

#repeating loop len(a)(number of elements) number of times
for j in range(len(a)):
    #initially done is false
    done = False
    i = 0
    while i<len(a)-1:
        #comparing the adjacent elements
        if a[i]>a[i+1]:
            #swapping
            a[i],a[i+1] = a[i+1],a[i]
            #Changing the value of done
            done = True
        i = i+1
    #if done is false then the list is sorted
    #we can stop the loop
    if done == False:
        break
print("Sorted list is: ")
print (a)