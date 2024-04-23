

def sequentialSearch(m, index = 0, items: list[T], searched = 'match') -> list[T]:
    switch (searched):
        case 'max':
            most = list[0]
            for i in range(index, length(list)):
                if most < i:
                    most = i
                if i == :
                    return most,i 
        case 'min':
            least = list[0]
            for i in list:
                if most > i:
                    least = i
            return least 
        case 'match':
            for i,x in list:
                if m == i:
                    return True,i 

def depthFirstSearch(m, i = 0, items: list[T], searched = 'match') -> list[T]:
    switch (searched):
        case 'max':
        case 'min':

        case 'match':
            if m == list[i]:
                return True
            elif m == list:
                pass


#def breadthFirstSearch():

#def binarySearch():

#def interpolationSearch():
