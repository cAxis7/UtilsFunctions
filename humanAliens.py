from itertools import combinations
import math

def coefficients(str):
    '''
    This function takes a String of two unique characters where it appends the index i if the
    next character is different from the previous one. It also multiplies the index by 2 and adds 1.

    Parameters:
    argument1 (string): a string of two unique characters

    Returns:
    list: odd integers
    '''
    return [i * 2 + 1 for i in range(len(str) - 1) if str[i] != str[i+1]]

def getFuncCoffs(zeros):
    '''
    This function takes a list of Zeros of a polymonomial function
    and returns the coefficients order in descending grade

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

def printFunction(cfs, state = True):
    size = len(cfs)
    print(f"{cfs[0] if cfs[0] != 1 else ''}x^{size - 1}" if state else f"- {cfs[0]}x^{size - 1 if }", end = ' ')
    for i in range(1, len(cfs)):
        state = not state
        print(f"{'+' if state else '-'}", end = ' ')
        print(f"{cfs[i] if cfs[i] != 1 else ''}x^{size - 1 - i}", end = ' ')

if __name__ == "__main__":
    '''
    Let's solve the problem Alien vs Human

    We want to find the function of a polynomial graph where each index i represents whether f(x)
    is positive or negative.

    Where the input is a string of A's and H's, where A represents that at index i a polynomial.
    Then, will find the zeros of the function and calculate the coefficients and then display the
    function.
    '''
    list1 = input("Enter a string of A's and H's: ")
    nums = coefficients(list1)
    coffs = getFuncCoffs(nums)
    printFunction(coffs)

