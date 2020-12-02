import sys

def name_of_function(var1, var2):
    sum = 0
    for i in range(var1):
        sum += var2
    return sum

if __name__ == '__main__':
    num_to_do = int(sys.argv[1])
    num_to_add = int(sys.argv[2])
    result = name_of_function(num_to_do, num_to_add)
    print(result)
