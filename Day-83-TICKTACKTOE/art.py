# TODO 1: Create tick / tack grid
def print_grid():
    p_1 = [1, 2, 4, 8]
    p_2 = [3, 9, 5, 7]

    markers = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    for i in p_1:
        markers[i] = 'x'
    for i in p_2:
        markers[i] = 'o'
    # print(markers)
    # print(a, b, c, d, e, f, g, h, i)

    h_grid = "---|---|---"

    line_1 = f" {markers[1]} | {markers[2]} | {markers[3]} "
    line_2 = f" {markers[4]} | {markers[5]} | {markers[6]} "
    line_3 = f" {markers[7]} | {markers[8]} | {markers[9]} "

    print(line_1)
    print(h_grid)
    print(line_2)
    print(h_grid)
    print(line_3)
# TODO 2: Collect User input
# TODO 3: Build Syntax

print_grid()
