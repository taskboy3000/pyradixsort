from RadixSort import RadixSort

list = [ 123, 403, 200, 500, 404, 901, 910, 902]

print("Radix sorting list: " + ",".join(map(str, list)) + "\n")

R = RadixSort(10, 3)
sorted_list = R.sort_list(list)

print("Sorted: " + ",".join(map(str, sorted_list)) + "\n")