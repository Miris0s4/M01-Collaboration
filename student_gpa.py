# Miriana Martinez-sosa
# student_gpa_checker.py
# This app accepts studnet names and GPA's and checks if the student 
#qualifies for the Honor roll list of Dean's list.

def main():
    while True:
        # whats the student's last name?
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ").strip()

        # if last name is 'ZZZ' ...
        if last_name == 'ZZZ':
            print("Exiting from program.")
            break
        
        # whats the student's first name?
        first_name = input("Enter student's first name: ").strip()

        # the student's GPA and any invalid input
        try:
            gpa = float(input("Enter student's GPA: "))
        except ValueError:
            print("Invalid GPA entered. Please enter a numeric value for GPA.")
            continue 
        
        # checking if the student qualifies for the Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        
        # check if the student qualifies for the Honor Roll
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
if __name__ == "__main__":
    main()