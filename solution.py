from collections import defaultdict, Counter
 
 
def SmallestSub(S):
    p = ''.join(set(S))
    dict_t = Counter(p)
 
    required = len(dict_t)
 
    l = 0
    r = 0
 
    curr_window_uniq_chars_count = 0
 
    curr_window_uniq_dict = {}
  
    min_window_len = float("inf")
    desired_window_l = None
    desired_window_r = None
 
    while r < len(S):
 
        
        curr_window_uniq_dict[S[r]] = curr_window_uniq_dict.get(S[r], 0) + 1
 

        if S[r] in dict_t and curr_window_uniq_dict[S[r]] == dict_t[S[r]]:
            curr_window_uniq_chars_count += 1
 
        
        while l <= r and curr_window_uniq_chars_count == required:
 
            
            if r - l + 1 < min_window_len:
                min_window_len = r - l + 1
                desired_window_l = l
                desired_window_r = r
 
            
            curr_window_uniq_dict[S[l]] -= 1
            if S[l] in dict_t and curr_window_uniq_dict[S[l]] < dict_t[S[l]]:
                curr_window_uniq_chars_count -= 1
 
            
            l += 1
 
        
        r += 1
    return "" if min_window_len == float("inf") else len(S[desired_window_l: desired_window_r + 1])
 
 
S = input()
 
out_ = SmallestSub(S)
print (out_)
