#IndustryComparison.py

#This program will take the closing stock indexes for different industries from a user selected plain text file
#And graphically compare them to the S&P500

    # import math library, graphics, matplot lab
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

def main():

    #read in data from .txt or .csv (Plain text format)(excel can be converted and will suck if is not converted)
    #filename1 =(input("Enter file name: "))

    columns = defaultdict(list)
    with open(input("Input file name here: ")) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            for (header, value) in row.items():
                columns[header].append(value)              #Need to convert this data from strings to floats

    data1 = map(float,columns['Interest Rate'])
    #data2 = columns['Inflation']
    #data3 = columns['Constant']
    print(type(data1))
    print(data1)
    #print(data2)
    #print(data3)

    #Where the data gets dropped in to
    #for d in file1.readlines():             #Reads each column in the sheet and drops the data in to a list so that it can be graphed
     #   cells = d.split(",")
      #  data1.append(cells[0])              #slice off the last 1 character in the last set
    #file1.close()                          datai[:-1]


    #filename2 = (input("Enter file name: "))
    #file2 = open(filename2, "r")
    #data2 = []
    #for d in file1.readlines():
     #   cells = d.split(",")
      #  data2.append(cells[1])
    #print(data2)

    #file3 = (input("What numbers (file) would you like to use? "))     #Create a function if enter is pressed it stops asking for data
    #file3 = [float(s)for s in file3.split(",")]
    #file4 = (input("What numbers (file) would you like to use? "))
    #file4 = [float(s)for s in file4.split(",")]




    rng = []
    print(  )
    #for i in range(len(data1)):
    #    rng.append(i)
    #print(rng)

    plt.figure(figsize=(8,10))
    plt.axis([0, 11, 0, 15])
    plt.ylabel('Value')
    plt.xlabel('Time')

    #plt.plot(rng, data1)       #Plotting XY values
    #plt.plot(rng, data2)
    #plt.plot(rng, data3)
    #plt.plot([0, 1, 2, 3, 4], file4)


  #gotta figure out how to display dates at the bottom but still have it make sense for the xcoord
    plt.show()

main()
    #       Chapter 11 slides Titled: File Loops slide 42
    #       Also look at slide 50 for the line.split function
# create a x value that represents date
#
#
#
#
# use a while loop for the range of data set x
#       y.coord = i
#       x.coord = x
#       use plot or graphics tool to use the coords to make the lines using
#       y = y +1
#
# Maybe somewhere down here put the check box shit
#
#
# percent of change equations to solve for who has the highest rate of growth
# Who has the slowest rate of growth
# highest and lowest values at the end
