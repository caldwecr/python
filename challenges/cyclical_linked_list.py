def has_cycle(head):
    return is_cyclical(head)

def is_terminated_soon(head):
    if head is None:
        return True
    elif head.next is None:
        return True
    elif head.next.next is None:
        return True
    else:
        return False

def is_cyclical(hop, hophop=False):
    if hophop is False:
        if is_terminated_soon(hop):
            return False
        else:
            hophop = hop.next.next

    if is_terminated_soon(hophop):
        return False
    elif hop == hophop:
        return True
    else:
        return is_cyclical(hop.next, hophop.next.next)