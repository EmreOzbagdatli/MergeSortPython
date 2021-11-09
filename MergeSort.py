def MergeSort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]

        MergeSort(Left)
        MergeSort(Right)

        i=j=k=0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

arr = [5,2,8,4,1,3,6,7]
MergeSort(arr)
print(arr)
