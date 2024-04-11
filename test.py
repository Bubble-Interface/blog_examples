def isIsomorphic(s: str, t: str) -> bool:
    i = 0
    str_map = {}
    while i < len(s):
        if s[i] in str_map:
            if s[i] != t[i]:
                return False
        else:
            str_map[s[i]] = t[i]
        
        i += 1
    
    return True


isIsomorphic("egg", "add")