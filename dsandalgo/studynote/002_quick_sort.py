numbers = [40, 35, 27, 75, 50]

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [number for number in array[1:] if number <= pivot]
        greater = [number for number in array[1:] if number > pivot]
        print("less:", less)
        print("greater::", greater)
        return quickSort(less) + [pivot] + quickSort(greater)
    
result = quickSort(numbers)
print(result)