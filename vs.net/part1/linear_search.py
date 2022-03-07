file = open("world.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

key = "Spanish"

i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1

if i < len(name_list):
    print( "The language is at position", i)
else:
    print( "The language was not in the list." )


def insertion_sort(my_list):
    for key_index in range(1, len(my_list)):
        key_value = my_list[key_index]
        scan_pos = key_index - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
        my_list[scan_pos + 1] = key_value

    for i in my_list:
        print(i)

insertion_sort(name_list)
