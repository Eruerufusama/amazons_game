def get_path(start, end):
    direction = "diagonal"
    x, y = 1, 1
    
    if start[0] > end[0]: x = -1
    if start[0] == end[0]: direction = "horizontal"
    if start[1] > end[1]: y = -1
    if start[1] == end[1]: direction = "vertical"

    if direction == "diagonal":
        return [(i, j) for i, j in zip(
                range(start[0] + x, end[0] + x, x),
                range(start[1] + y, end[1] + y, y))
                ]
    elif direction == "vertical":
        return [(i, start[1]) for i in range(start[0] + x, end[0] + x, x)]
    elif direction == "horizontal":
        return [(start[0], i) for i in range(start[1] + y, end[1] + y, y)]

def val_end_pos(start, end):
    if start[0] == end[0]:
        if start[1] != end[1]: return True
        else: return False
    if start[1] == end[1]:
        return True
    else:
        if start[0] - start[1] == end[0] - end[1]: return True
        if start[0] + start[1] == end[0] + end[1]: return True
        else: return False