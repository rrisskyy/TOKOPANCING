# def interpolationSearch(arr, lo, hi, x):

#     if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

#         pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
#                     (x - arr[lo]))

#         if arr[pos] == x:
#             return pos
#         if arr[pos] < x:
#             return interpolationSearch(arr, pos + 1, hi, x)
#         if arr[pos] > x:
#             return interpolationSearch(arr, lo, pos - 1, x)

#     return -1

help_dict = { 
    'a': '1', 
    'b': '2', 
    'c': '3', 
    'd': '4', 
    'e': '5', 
    'f': '6', 
    'g': '7', 
    'h': '8', 
    'i': '9', 
    'j': '10',
    'k': '11', 
    'l': '12', 
    'm': '13', 
    'n': '14', 
    'o': '15', 
    'p': '16', 
    'q': '17', 
    'r': '18', 
    's': '19', 
    't': '20',
    'u': '21',
    'v': '22', 
    'w': '23', 
    'x': '24', 
    'y': '25', 
    'z': '26'
}


arr = 'R I S K Y'
arr.lower()
res = ''.join(help_dict[ele] for ele in arr.split()) 
# n = len(arr)
# x = 'a'

print("The string after performing replace : " + res)  

# index = interpolationSearch(arr, 0, n - 1, x)
 
# if index != -1:
#     print("Element found at index", index)
# else:
#     print("Element not found")