from symptoms import list as symptoms_list
print("Welcome to Rehospics\n","You have been transfered to one of our representative...")
user_name = input("Please, May i know your name?\n")
# checking if the user inserted a valid name
while user_name:
    if len(user_name) > 2:
        user_name = user_name
        break                 
    else:
        print("Please, your name is too short to be called a name")
        user_name = input("May i know your name?\n")
    
first_question = input("Greetings of the day,\n how may i help you?\n").lower()

checkup = True
while checkup:
    # if the user is here for checkup
    fq = first_question
    if ("checkup" in fq) or ("sick" in fq) or ("medical" in fq) :
        print("Okay, you are on the right place")
        # creating a default for the users sickness name
        illness_name = None
        answers = []
        # howlong the illness has been disturbing you.
        duration = int(input("for how many days have you been experiencing this illness? \n"))
        if duration < 10 :
            duration = "an Acute disease"
        else:
            duration = "Likely to be chronic disease "
        print(user_name,", I am about to be stating out some symptoms if you are experiening that kindly\n Indicate by answering 'yes' or 'no' if not related to yours.\n Are you with me?")
        for item in symptoms_list:

            question = input("Are you experiencing "+ item + "\n")
            while question:
                if question != "yes" and question != "no":
                    print("Please, you are only to enter either 'yes" or 'no')
                    question = input("Are you experiencing "+ item+"\n").lower()
                else:    
                    answers.append(question)
                    break
        # Analzing my data in terms of my grouped symptoms
        if answers[:3].count("yes") >= 2:
            illness_name = "Chicken Pox"
        if answers[3:7].count("yes") >= 3:
            illness_name = "Conjunctivities"
        if answers[7:11].count("yes") >= 3:
            illness_name = "maleria / Hepatitis"
        if answers[11:12].count("yes") >= 1:
            illness_name = "Hepatitis"
        if answers[12:15].count("yes") >= 2:
            illness_name = "influenza (flu)"
        if answers[15:17].count("yes") >= 1:
            illness_name = "pnuemonia"
        if answers[17].count("yes") > 0:
            illness_name = "tuberculosis"
        # printing out the result    
        print(user_name,",We have finally come to the end of our analysis\n","And from our readings")
        print("\nYour Sickness is:",duration)
        print('By name ',illness_name,"It can be healed with the drugs our pharmacist will recommend to you...")
        print("Nice hearing from you",user_name)
        ending_question = input("Do you wish to restart the conversation again?").lower()
        while ending_question:
            if ending_question=="yes" or ending_question=="restart":
                first_question = input("How may i help you again?\n")
            else:
                break
    # if not for checkup
    else:
        print("Thanks for checking on us but we are only meant to solve problem for the sick ones")
        break