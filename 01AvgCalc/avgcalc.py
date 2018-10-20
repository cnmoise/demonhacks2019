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
    
    rounded_gpa = 0.0
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
    kbw = sys.stdin.readline().strip

    #print(kbw)
    if(kbw == "y"):
        weighted = True
    elif(kbw == "n"):
        weighted = False
    else:
        print("Invalid Input... Assuming GPA Unweighted")

    # #
    #
    if(WEIGHTED):
        rounded_gpa = round(((min(4, HIGH_GPA) + (2 * COL_GPA))/3), 2)
    else:
        rounded_gpa = round(((HIGH_GPA + COL_GPA)/2), 2)

    print("Student Name: ", SNAME)
    print("College GPA: ", COL_GPA)
    if(WEIGHTED):
        print("High School GPA (Weighted): ", HIGH_GPA)
    else:
	    print("High School GPA (Unweighted): ", HIGH_GPA)

    print("Rounded GPA (Weighted): ", rounded_gpa)

if __name__== "__main__":
  main()
