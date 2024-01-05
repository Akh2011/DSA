from BUbble_sort import swap


def shellsort(arr):
	gap = len(arr) // 2

	while gap >= 1:
		for i in range(len(arr)):
			j = i+gap

            
			if arr[i] > arr[j]:	
				arr[i] , arr[i+gap]  = swap(arr[i],arr[i+gap])

		gap = gap//2

					
	return arr





if __name__ == '__main__':
    arr = [2, 75, 81, 9, 43]
	
    print(shellsort(arr))