#quick-sort function   
def quick_sort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quick_sort(a, low, pi-1)
        quick_sort(a, pi+1, high)


#partition function to sort elements to both sides of pivot
def partition(a, low, high):
    i = (low -1)
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1],a[high] = a[high], a[i+1]
    return (i+1)


list = []
size = int(input("Enter number of elements in list: "))
for i in range(size):
    elements = int(input())
    list.append(elements)
low = 0
high = len(list) - 1
quick_sort(list, low, high)
print(list)