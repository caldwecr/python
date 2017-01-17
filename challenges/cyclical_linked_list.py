def has_cycle(head):
    return is_cyclical(head, head.next.next)

def is_terminated_soon(head):
    if head.next is None:
        return True
    elif head.next.next is None:
        return True
    else:
        return False

def is_cyclical(hop, hophop):
    if is_terminated_soon(hophop):
        return False
    elif hop == hophop:
        return True
    else:
        return is_cyclical(hop.next, hophop.next.next)