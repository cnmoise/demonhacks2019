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
    S_NAME = get_inputs("Please enter the students name:\n")
    COL_GPA = float(get_inputs("Please enter the students College GPA:\n"))
    HIGH_GPA = float(get_inputs("Please enter the students High School GPA:\n"))
    print("Is the High School GPA weighted? y/n:")
    kbw = check_kbw(get_inputs("Is the High School GPA weighted? y/n:\n").strip())

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

def get_inputs(msg):
    print(msg)
    return sys.stdin.readline()

def check_kbw(kbw):
    if (kbw == "y"):
        return True
    elif (kbw == "n"):
        return False
    else:
        print("Invalid Input... Assuming GPA Unweighted")
        return False

if __name__== "__main__":
    main()


