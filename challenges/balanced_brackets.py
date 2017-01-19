from collections import deque

def is_matched(expression):
    pairings = { '{': '}', '[': ']', '(': ')'}
    d = deque(expression)
    lefties = deque()
    while len(d) > 0:
        x = d.popleft()
        if x in pairings.keys():
            lefties.append(x)
        else:
            if(len(lefties) == 0):
                return False
            l = lefties.pop()
            if pairings[l] != x:
                return False

    return len(lefties) == 0
