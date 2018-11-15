arr = [2, 5, 8, 0, 6]
# print(arr)
def sort_array_bubble(arr):     
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j]>arr[i]:
                tem = arr[i]
                arr[i] =arr[j]
                arr[j] = tem
    return arr

# print(sort_array_bubble(arr))

# arr_str = ['d', 'a', 'r', 'i', 'o']
# print(arr_str)



name_1 = "Wladymir"
name_2 = "Estephanie"

def string_compare(name_1, name_2):
    count  = 0 
    if len(name_1)< len(name_2):
        count = len(name_1)
    else:
        count = len(name_2)

    for i in range(0, count):
        if(name_1[i]<name_2[i]):
            return name_1
        elif(name_2[i]<name_1[i]):
            return name_2

    if len(name_1) == len(name_2):   
        return name_1
    elif len(name_1)< len(name_2):
        return name_1
    else:
        return name_2

def string_compare_int(name_1, name_2):
    count  = 0 
    if len(name_1)< len(name_2):
        count = len(name_1)
    else:
        count = len(name_2)

    for i in range(0, count):
        if(name_1[i]<name_2[i]):
            return 1
        elif(name_2[i]<name_1[i]):
            return -1

    if len(name_1) == len(name_2):   
        return 0
    elif len(name_1)< len(name_2):
        return 1
    else:
        return -1

def sort_string_array_bubble(arr):     
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if string_compare_int(arr[i], arr[j])==-1:
                tem = arr[i]
                arr[i] =arr[j]
                arr[j] = tem
    return arr

print(sort_string_array_bubble(["Wladymir", "Estephanie", "Daniel", "Dario"]))


