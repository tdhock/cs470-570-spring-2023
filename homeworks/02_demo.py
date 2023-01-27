#list comprehension
my_list = [line.split() for line in open("board.txt")]
#for loop
my_list = []
for line in open("board.txt"):
    my_list.append(line.split())
my_list

# for printBoard.
print(" ".join(my_list[0]))

xy_pair = (0,3)
x, y = xy_pair
board_size = len(my_list)
for x_offset in [-1,0,1]:
    for y_offset in [-1,0,1]:
        new_pair = (x+x_offset, y+y_offset)
        is_good = True
        for coord in new_pair:
            if coord < board_size and coord >= 0:
                "good"
            else:
                is_good = False
        if is_good:
            print(new_pair)
