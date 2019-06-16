a = [] 
print("INSERTION SORT")
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
print("Enter those many elements: ")
for i in range(0, n): 
    x = int(input()) 
  
    a.append(x)

for i in a:
    j = a.index(i)
    #i is not the first element
    while j>0:
        #not in order
        if a[j-1] > a[j]:
            #swap
            a[j-1],a[j] = a[j],a[j-1]
        else:
            #in order
            break
        j = j-1
print("Sorted list using Insertion sort is: ")
print (a)