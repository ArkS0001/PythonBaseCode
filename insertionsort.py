def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j =i-1        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
data = [3,6,8,2,5,1,5,7]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
