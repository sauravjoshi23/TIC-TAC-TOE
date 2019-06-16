a = [] 
print("SELECTION SORT")
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
print("Enter those many elements: ")
for i in range(0, n): 
    x = int(input()) 
  
    a.append(x)


def selection_sort(a):
    for i in range(0, len(a) - 1):
        k = i
        for j in range(i + 1, len(a)):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]
 
selection_sort(a)
print('Sorted list: ', end='')
print(a)