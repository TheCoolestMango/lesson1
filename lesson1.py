n = [26,26,13,8,89]
set_n = set(n)
#print(set_n)
# Вывести все пары
#for x in n:
#    for y in n:
#        print(x,y)

def strcounter_slow(s):
    for sym in s:
        count = 0
        for sub_sym in s:
            if sym==sub_sym:
                count+=1
        print(sym, count)

def strcounter_med(s):
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym==sub_sym:
                count+=1
        print(sym, count)

def strcounter_fast(s):
    syms_count = {}
    for sym in s:
        syms_count[sym] = syms_count.get(sym,0)+1

    for sym, count in syms_count.items():
        print(sym,count)


s = 'aabbbbccd'
strcounter_fast(s)