def read_input():
    f = open("input.txt","r")
    input_text = f.read()
    inputs = input_text.split('\n')
    return inputs

def bubbleSort(arr):
    n = len(arr) 
    count = 0  
    # Traverse through all array elements 
    for i in range(n):
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                count = count + 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count

def recommend(inputs):
    flag = 0
    res = {}
    for line in inputs:
        if flag == 0:
            line = line.strip('\n')
            l1,l2 = line.split(':')
            num = l2.split(',')
            dict_num = {num[i]: i for i in range(0, len(num))}  
            flag = 1
        else:
            #print(line)
            line = line.strip('\n')
            l1,l2 = line.split(':') 
            num = l2.split(',')
            dict_num1 = [dict_num[num[i]] for i in range(0, len(num))]
            ops = bubbleSort(dict_num1)
            res[l1] = ops
            #print(dict_num1)

    sorted_d = sorted(res.items(), key=lambda x: (x[1],x[0]), reverse=False)
    return sorted_d

inputs = read_input()
output = recommend(inputs)
print(output)
