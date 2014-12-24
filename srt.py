# make a code that sorts  a list from greatest to least

#this a function that swaps the numbers at position pos1 and pos2
def swap(pos1,pos2):
    mylist[pos1],mylist[pos2] =mylist[pos2],mylist[pos1]
    return


#a list of random numbers which im trying to sort
mylist = [1,-1,812,8,-12,-8,98,73,-1,0,9,8,5,2774,7]
print(mylist)
#variable to use for a while loop
numberplacement = 0
#to make sure it runs enough time it is the length of the list
while numberplacement <len(mylist):
    #an embedded while loop to check the first number to all the other numbers
    c=0
    while c+1 <len(mylist):
        #Find the positions of the numbers which you are swapping
        a = mylist[c]
        b = mylist[c + 1]
        if a < b:
            #use the swap function to switch the positions
            swap(c,c+1)
        print(mylist)
        c = c + 1

    #repeat with the new placement of numbers
    numberplacement = numberplacement + 1

#print the list
print(mylist)
