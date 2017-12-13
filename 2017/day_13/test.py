

def scanner(height, time):
    offset = time % ((height - 1) * 2)
    print offset

    return 2 * (height - 1) - offset if offset > height - 1 else offset

print scanner(3, 3)
