# check if there is a 1-to-1 mapping from string s1 to string s2
def is1to1(s1, s2):
    
    # if strings do not have same length, some characters will go unmapped
    if len(s1) != len(s2):
        print("false")
        return

    # if no duplicate characters exist in s1, then a 1-to-1 mapping is possible (no duplicate mappings)
    
    # remove duplicate characters from s1
    temp = set(s1)
    #  if length is the same, no duplicates were present
    if len(temp) == len(s1):
        print("true")
    else:
        print("false")
