
#worst/best/ave

#O(n^2)/O(n^2)/O(n^2)
def selectionSort(input):
    if isinstance(input, (int,float,complex)):
        return input
    for i in range(len(input)):
        held = input[0]
        for j in range(i+1, len(input)):
            if input[i] > input[j]:
                input[i],input[j] = input[j],input[i]
    return input

#O(n^2)/O(n)/O(n^2)
def insertionSort(input):
    length = len(input)
    if length < 2 or isinstance(input, (int,float,complex)):
        return input 
    div = 0
    while div+1 < length: 
        if input[div + 1] < input[div]:
            for i in range(div+1):
                if input[div+1] < input[i]:
                    input[i],input[div+1] = input[div+1],input[i]
        div += 1
    return input

def mergeSort(input):
    if len(input) < 2:
        return input
    elif len(input) == 2:
        print(input)
        if input[0] > input[1]:
            input[0],input[1] = input[1],input[0]
            return input
        else: return input
    else:
        l = mergeSort(input[:int(len(input)/2)])
        r = mergeSort(input[int(len(input)/2):])
        return(l+r)
        

l = [1.1,12.4,3,52,123,34,5,12,0]
print(mergeSort(l))
#def quickSort():


#def heapSort():


#def countingSort():


#def radixSort():

