def intersection_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    intersection = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not intersection or intersection[-1] != arr1[i]:
                intersection.append(arr1[i])
            i += 1
            j += 1
    
    return intersection

# Example usage
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 5, 7, 8]
print("Intersection:", intersection_sorted_arrays(arr1, arr2))
