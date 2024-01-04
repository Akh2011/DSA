from BUbble_sort import swap

def insertionsort_witharray(arr):
	new_array = []
	new_array.insert(0,arr[0])
	for i in range(len(arr)):
		for j in (range(len(new_array))):
			if arr[i] > new_array[j]:
				new_array.insert(j,arr[i])
	
	return new_array
	

if __name__=='__main__':
	
    arr =[2, 75, 9, 81, 43]
	 
    print(insertionsort_witharray(arr))