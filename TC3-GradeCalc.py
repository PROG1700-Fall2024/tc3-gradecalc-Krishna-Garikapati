# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    #input
    grade=input("Please enter a letter grade: ")
    modifier=input("Please enter a modifier (+, - or nothing):")
    
    #print statements
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.\nValid grade modifiers are +, - or nothing.\nAll letter grades except F can include a + or - symbol.\nCalculated grade point value cannot exceed 4.0.\n")
    
    #conditions
    if grade.upper()=="A":
        if modifier=="+":
            NumericGrade=4.0
        elif modifier=="-":
            NumericGrade=(4.0)-(0.3)
        elif modifier=="":
            NumericGrade=4.0
        print("The numeric value is:{0:.1f}".format(NumericGrade))
    elif grade.upper()=="B":
        if modifier=="+":
            NumericGrade=(3.0)+(0.3)
        elif modifier=="-":
            NumericGrade=(3.0)-(0.3)
        elif modifier=="":
            NumericGrade=3.0
        print("The numeric value is:{0:.1f}".format(NumericGrade))
    elif grade.upper()=="C":
        if modifier=="+":
            NumericGrade=(2.0)+(0.3)
        elif modifier=="-":
            NumericGrade=(2.0)-(0.3)
        elif modifier=="":
            NumericGrade=2.0
        print("The numeric value is:{0:.1f}".format(NumericGrade))
    elif grade.upper()=="D":
        if modifier=="+":
            NumericGrade=(1.0)+(0.3)
        elif modifier=="-":
            NumericGrade=(1.0)-(0.3)
        elif modifier=="":
            NumericGrade=1.0
        print("The numeric value is:{0:.1f}".format(NumericGrade))
    elif grade.upper()=="F":
        NumericGrade=0
        print("The numeric value is:{0:.1f}".format(NumericGrade))
    else:
        print("You entered an invalid letter grade.\nThe numeric value is: 0.0")
   
main()
