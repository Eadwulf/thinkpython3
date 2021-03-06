from unit_tester import test

def merge(xs, ys):
    """ Merge sorted lists xs and ys. Return a sorted result. """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):           # If xs list is finished,
            result.extend(ys[yi:])  # add remaining items from ys.
            return result
        
        if yi >= len(ys):           # If xs list is finished,
            result.extend(xs[xi:])  # add remaining items from xs.
            return result

        # If both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else: 
            result.append(ys[yi])
            yi += 1


xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24, 28, 32, 34, 38]

zs = xs + ys
zs.sort()

test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5])
test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
     ["a", "big", "big", "bite", "cat", "dog"])
