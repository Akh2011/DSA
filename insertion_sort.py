from BUbble_sort import swap

def insertionsort_witharray(arr):
    new_array = []
    new_array.insert(0,arr[0])
    for i in range(len(arr)):
        for j in (range(len(new_array))):
            if arr[i] > new_array[j]:
                new_array.insert(j,arr[i])
                break
        

    return new_array
    
'''

def insert_array(a,arry):
	for i in range(len(arry)):
		if a > arry[i]:
			arry.insert(a,arry[range(len(arry)+1)])
			return arry
            break

'''
			
if __name__=='__main__':
	
        
    arr =[ 
    [2, 81, 75, 9, 43],
    [1,2,3,4],
    [4,3,2,1],
	[1]
]


    for i in arr:
        print(insertionsort_witharray(i))
	





    