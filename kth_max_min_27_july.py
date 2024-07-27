def kth_smallest(arr, k):
    arr_sorted = sorted(arr)
    return arr_sorted[k-1]

def kth_largest(arr, k):
    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[k-1]

arr = [7, 10, 4, 3, 20, 15]
k = int(input("Enter the value of k: "))
print(f"The {k}th smallest element is {kth_smallest(arr, k)}")
print(f"The {k}th largest element is {kth_largest(arr, k)}")
