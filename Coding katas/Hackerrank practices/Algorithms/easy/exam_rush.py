import sys

def examRush(tm, t):

    sum_tm = 0                      # assign variables a value
    answer = 0
    
    while(True):                    
        if sum_tm < t:              # If the sum of the terms is less than the hours available
            sum_tm += min(tm)       # Sum the smallest term to the number of hours to study
            tm.remove(min(tm))      # Remove that smallest term
            answer += 1             # Add 1 to the answer
                    
        if sum_tm > t :             # Uf the number of terms is greater
            answer -= 1             # Remove 1 from the answer
            break                   # Get out of the while
        
        if sum_tm == t:             # If the number of hours to study and the hours available to study are identical
            break                   # Get out of the while
                                    
                                    # Repeat if conditions don't match
                                     
    return answer                   # Return the last value

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    tm = []
    tm_i = 0
    for tm_i in range(n):
        tm_t = int(input().strip())
        tm.append(tm_t)
    result = examRush(tm, t)
    print(result)
