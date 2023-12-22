running = True

while running:
    test = input("More Letters ?")
    if test == "Yes":
        type = input("Job Offer or Rejection?")
        if type == "Job Offer":
            firstName = input("First Name: ")
            if len(firstName) < 2 and len(firstName) > 10 and firstName[0].islower() and firstName.isdigit():
                print("Input error")
                running = False
            lastName = input("Last Name: ")
            if len(lastName) < 2 and len(lastName) > 10 and lastName[0].islower() and lastName.isdigit():
                print("Input error")
                running = False
            jobTitle = input("Job Title: ")
            if len(jobTitle) < 10:
                print("Input error")
                running = False
            valid_salary = False
            while not valid_salary:
                annualSalary = input("Annual Salary: ")
                salary = annualSalary.replace(".", "")
                salary = salary.split(",")
                salary_int = int(salary[0])
                if salary_int < 20000 or salary_int > 80000:
                    print("Input error")
                else:
                    valid_salary = True
            startDate = input("Start Date: ")
            startDateSplit = startDate.split("-")
            year = int(startDateSplit[0])
            month = int(startDateSplit[1])
            day = int(startDateSplit[2])
            if startDate[4] != '-' and startDate[7] != '-':
                print("Input error")
                running = False
            if day > 31 or month > 12:
                print("Input error")
                running = False
            if year != 2022 and year != 2021:
                print(year)
                print("Input error")
                running = False
            print("Here is the final letter to send:",
                  "Dear " + firstName + " " + lastName + ",",
                  "After careful evaluation of your application for the position of " + jobTitle + ",",
                  "we are glad to offer you the job. Your salary will be " + annualSalary + " euro annually.",
                  "Your start date will be on " + startDate +
                  ". Please do not hesitate to contact us with any questions.",
                  "Sincerely,",
                  "HR Department of XYZ", sep='\n')
        elif type == "Rejection":
            firstName = input("First Name: ")
            if len(firstName) < 2 and len(firstName) > 10 and firstName[0].islower() and firstName.isdigit():
                print("Input error")
                running = False
            lastName = input("Last Name: ")
            if len(lastName) < 2 and len(lastName) > 10 and lastName[0].islower() and lastName.isdigit():
                print("Input error")
                running = False
            jobTitle = input("Job Title: ")
            if len(jobTitle) < 10:
                print("Input error")
                running = False
            wantFeedback = input("Feedback ?")
            if wantFeedback == "Yes":
                feedback = input("Feedback: ")
            print("Here is the final letter to send:",
                  "Dear " + firstName + " " + lastName + ",",
                  "After careful evaluation of your application for the position of " + jobTitle + ",",
                  "at this moment we have decided to proceed with another candidate.",
                  (wantFeedback == "Yes") and
                  "Here we would like to provide you our feedback about the interview. " + feedback or "",
                  "We wish you the best in finding your future desired career. Please do not hesitate to " +
                  "contact us with any questions.",
                  "Sincerely,",
                  "HR Department of XYZ", sep='\n')
        else:
            print("Input error")
            running = False
    elif test == "No":
        running = False
    else:
        print("must awnser with Yes or No")