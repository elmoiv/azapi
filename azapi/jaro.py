# Python3 implementation of above approach
# Source: https://www.geeksforgeeks.org/jaro-and-jaro-winkler-similarity/
# This code is contributed by mohit kumar 29 (GeeksforGeeks.com)
from math import floor
  
def jaro_distance(s1, s2): 
    if (s1 == s2): 
        return 1.0
  
    len1, len2 = len(s1), len(s2)
    max_dist = floor(max(len1, len2) / 2) - 1
    match = 0
    hash_s1, hash_s2 = [0] * len(s1), [0] * len(s2)
  
    for i in range(len1):
        for j in range(max(0, i - max_dist),  
                       min(len2, i + max_dist + 1)):
            if (s1[i] == s2[j] and hash_s2[j] == 0):
                hash_s1[i], hash_s2[j] = 1, 1
                match += 1
                break

    if (match == 0): 
        return 0.0

    t = 0
    point = 0
  
    for i in range(len1): 
        if (hash_s1[i]): 
            while (hash_s2[point] == 0): 
                point += 1
  
            if (s1[i] != s2[point]): 
                point += 1
                t += 1
    t = t//2

    return (match/ len1 + match / len2 + 
            (match - t + 1) / match)/ 3.0