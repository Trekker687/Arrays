import array as arr

arraynum = arr.array('i', [1,3,4,5,6,7,3,1,4,3])
print("Original array: ", arraynum)

print("Number of occurences of number 3 in the array: "+str(arraynum.count(3)))

arraynum.reverse()
print("Reversed array: " +str(arraynum))