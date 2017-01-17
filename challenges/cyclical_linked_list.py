def has_cycle(head):
    if is_terminated_soon(head):
        return False
    else:
        return is_cyclical(head, head.next.next)

def is_terminated_soon(head):
    if head is None:
        return True
    elif head.next is None:
        return True
    elif head.next.next is None:
        return True
    else:
        return False

def is_cyclical(hop, hophop):
    if hop == hophop:
        return True
    elif is_terminated_soon(hophop):
        return False
    else:
        return is_cyclical(hop.next, hophop.next.next)