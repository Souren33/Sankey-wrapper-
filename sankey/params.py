

print(1, 2, 3, 4, 5, "hello", True, [1, 2, 3])



def add(x, y, *args, msg="hello", **kwargs):
    print(x, y, args)
    print(type(args))

    print(msg, "John")

    total = x + y
    for z in args:
        total += z
    return total


print(add(3, 5, msg="hi"))