#Author: Claudiu Moise
#GPA calculator for Java and Python

#Allows us to use the readline method





import sys

def main:
    #Constants
    S_NAME ="Derek Brambles"
    COL_GPA = 1.389454
    HIGH_GPA = 3.7
    #Booleans are capitalized
    WEIGHTED = True
    ROUNDED_GPA = 0.0
    #used as a temporary variable to store user choice
    kbw = "x";

    #by default stdin takes input as strings
    #therefore we have to explicitly cast the input as a float
    print("Please enter the students name:")
    S_NAME = sys.stdin.readline()
    print("Please enter the students College GPA:")
    COL_GPA = float(sys.stdin.readline())
    print("Please enter the students High School GPA:")
    HIGH_GPA = float(sys.stdin.readline())
    print("Is the High School GPA weighted? y/n:")
    KBW = sys.stdin.readline()

    KBW = kbw.strip()
    #print(kbw)
    if(KBW == "y"):
        weighted = True
    elif(kbw == "n"):
        weighted = False
    else:
        print("Invalid Input... Assuming GPA Unweighted")

    # #
    #
    if(weighted):
        RoundedGPA = round(((min(4, HighGPA) + (2 * ColGPA))/3), 2)
    else:
        RoundedGPA = round(((HighGPA + ColGPA)/2), 2)

    print("Student Name: ", Sname)
    print("College GPA: ", ColGPA)
    if(weighted):
        print("High School GPA (Weighted): ", HighGPA)
    else:
	    print("High School GPA (Unweighted): ", HighGPA)

    print("Rounded GPA (Weighted): ", RoundedGPA)

if __name__== "__main__":
  main()
