import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30] 
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31] 

ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'

def demo(bisect_fn): 
    for needle in reversed(NEEDLES): 
        position = bisect_fn(HAYSTACK, needle) 
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))

def grad(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print(bisect_fn(HAYSTACK, 0))
    print('DEMO', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)