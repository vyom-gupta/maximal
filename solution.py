from collections import defaultdict, Counter
 
 
def SmallestSub(S):
    p = ''.join(set(S))
    dict_t = Counter(p)
 
    required = len(dict_t)
 
    l = 0
    r = 0
 
    uniq_chars_count = 0
 
    uniq_dict = {}
  
    min_window_len = float("inf")
    window_l = None
    window_r = None
 
    while r < len(S):
 
        
        uniq_dict[S[r]] = uniq_dict.get(S[r], 0) + 1
 

        if S[r] in dict_t and uniq_dict[S[r]] == dict_t[S[r]]:
            uniq_chars_count += 1
 
        
        while l <= r and uniq_chars_count == required:
 
            
            if r - l + 1 < min_window_len:
                min_window_len = r - l + 1
                window_l = l
                window_r = r
 
            
            uniq_dict[S[l]] -= 1
            if S[l] in dict_t and uniq_dict[S[l]] < dict_t[S[l]]:
                uniq_chars_count -= 1
 
            
            l += 1
 
        
        r += 1
    return "" if min_window_len == float("inf") else len(S[window_l: window_r + 1])
 
 
S = input()
 
result = SmallestSub(S)
print (result)
