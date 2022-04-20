from itertools import combinations
import math

def coefficients(list1):
    '''
    This function takes a list of A's and H's, where the latter means that f(x) is negative;
    while, the former means that f(x) is positive. x equals to the index i * 2. It returns a
    list of odd numbers where each represent a zero in f(x)

    Parameters:
    argument1 (list): A list of 'A' and 'H' which represent f(x), where x is the index i * 2, 
    and A means that f(x) is less than 0 while H means f(x) > 0

    Returns:
    list: Returns a list values x where the f(x) equals 0
    '''
    return [i * 2 + 1 for i in range(len(list1) - 1) if list1[i] != list1[i+1]]

def getFuncCoffs(zeros):
    '''
    This function takes a list of Zeros of a polymonomial function
    and returns the coefficients

    Parameters:
    argument1 (list): integer

    Returns:
    list: integer
    '''
    list_combinations = []
    for n in range(len(zeros) + 1):
        samples = list(combinations(zeros, n))
        mult = [math.prod(sample) for sample in samples]
        list_combinations.append(sum(mult))
    return list_combinations

if __name__ == "__main__":
    list1 = input("Enter a string of A's and H's: ")
    nums = coefficients(list1)
    coffs = getFuncCoffs(nums)
    print(coffs)

