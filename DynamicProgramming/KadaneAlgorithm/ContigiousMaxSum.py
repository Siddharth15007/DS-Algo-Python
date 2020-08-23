import sys

def maxSubArraySum(a,n):
    max_ending_here, max_so_far = 0, 0
    for i in range(0, n):
        max_so_far += a[i]
        if max_so_far < 0:
            max_so_far = 0
            #print(max_so_far,max_ending_here)
        elif max_ending_here < max_so_far:
            max_ending_here = max_so_far
            #print(max_ending_here)
            #print(max_so_far)
    return max_so_far

if __name__ == '__main__':
    a = [5, 15, -30, 10, -5, 40, 10]
    n = int(sys.getsizeof(a) / sys.getsizeof(a[0]))
    #print(n)
    max_sum_result = maxSubArraySum(a,n)
    print("Max Contigious Sum is:",max_sum_result)