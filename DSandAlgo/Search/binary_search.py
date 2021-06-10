def binary_search(i, j, arr, key):
    if i > j:
        return -1
    mid = int((i + j) / 2)
    if(arr[mid] == key):
        # element found, return the position
        return mid
    elif(arr[mid] > key):
        return binary_search(i, mid - 1, arr, key)
    else:
        return binary_search(mid + 1, j, arr, key)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10,20,45,68,79]
    key = 78
    loc = binary_search(0, len(arr), arr, key)
    if loc == -1:
        print("Element bot found")
    else:
        print("Element found at loc : {}".format(loc))