# deleting a line matching
# a specific pattern or
# containing a specific string
 
# we want to delete a line
# containing string = 'ber'
try:
    with open('BIBLE LOUIS SECOND_1.txt', 'r') as fr:
        lines = fr.readlines()
 
        with open('BIBLE LOUIS SECOND_2.txt', 'w') as fw:
            for line in lines:
               
                # find() returns -1
                # if no match found
                if line.find('^') == -1:
                    fw.write(line)
    print("Deleted")
except:
    print("Oops! something error")