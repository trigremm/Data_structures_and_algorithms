def sum_map_ord(s):
    r = sum(map(ord, s))
    print(s, ":", r)
        
s = 'hello world'; sum_map_ord(s)
s = 'world hello'; sum_map_ord(s)
s = 'gello xorld'; sum_map_ord(s)

def myhash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult * ord(ch)
        mult += 1
    print (s, ":", hv)
    return hv

s = 'hello world'; myhash(s)
s = 'world hello'; myhash(s)
s = 'gello xorld'; myhash(s)