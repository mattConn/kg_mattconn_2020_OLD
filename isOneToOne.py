# check if there is a 1-to-1 mapping from string s1 to string s2
def isOneToOne(s1, s2):
    
    # if strings do not have same length, some characters will go unmapped
    if len(s1) != len(s2):
        return False

    # if no duplicate characters exist in s1, then a 1-to-1 mapping is possible (no duplicate mappings)
    if len(set(s1)) == len(s1):
        return True 
    else:
       return False 
