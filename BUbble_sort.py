


def bubblesort(arr):
    for i in range(len(arr)):
        for j in (range(len(arr)- i-1)):

            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = swap(arr[j],arr[j+1])

    
    
    return arr


def swap(a,b):
    temp = a
    a=b
    b=temp

    return a,b

if __name__ == '__main__':

  
    
    arr =[ 
    [2, 81, 75, 9, 43],
    [],
    [1,2,3,4],
    [4,3,2,1],
	[1]
]


    for i in arr:
        print(bubblesort(i))
	




