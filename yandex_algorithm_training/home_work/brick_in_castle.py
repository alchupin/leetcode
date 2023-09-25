def can_run_away(brick, hole):
    brick.remove(max(brick))
    if (brick[0] < hole[0] and brick[1] < hole[1]) or (brick[0] < hole[1] and brick[1] < hole[0]):
        return True
    return False

b = [2, 4, 6]
h = [3, 4]
print(can_run_away(b, h))