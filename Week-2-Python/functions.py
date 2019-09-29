def my_abs(val):
    if val < 0:
        return 0 - val
    return val

def inc_val(val):
    val = val + 1
    return val

x = 7
inc_val(x)
print(x)

def swap(v1, v2):
    tmp = v1
    v1 = v2
    v2 = tmp
    return v1, v2

x = 6
y = 3
x, y = swap(x, y)
print(x, y)
