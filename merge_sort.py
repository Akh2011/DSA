from BUbble_sort import swap


def mergegsort(a,b):
    sorted_array = []
    i=0
    j=0
    while i< len(a) and j < len(b):
        
        if a[i] < b[j]:
            sorted_array.append(a[i])
            
            i += 1
        elif a[i] > b[j]:
            sorted_array.append(b[j])
            j += 1



    while i < len(a):
        sorted_array.append(a[i])
        i += 1
    while j < len(b):
        sorted_array.append(b[j])
        j += 1


    return sorted_array


def mergesort(a):
    if len(a) <= 1:
        return a
    
    half = len(a) // 2

    firstarray = mergesort(a[:half])
    secondarray = mergesort(a[half:])

    return mergegsort(firstarray,secondarray)

if __name__ == '__main__':

    arr = [2, 81, 75, 9, 43]


    print(mergesort(arr))
