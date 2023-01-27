#list comprehension
my_list = [line.split() for line in open("board.txt")]
#for loop
my_list = []
for line in open("board.txt"):
    my_list.append(line.split())
my_list

# for printBoard.
print(" ".join(my_list[0]))
