"""""
def age_program():
    user_age = input("Enter your age: ")
    age_secs = int(user_age)*365*24*60*60
    print("Your age in seconds is {}".format(age_secs))

age_program()
"""""
def ask_age():
    age = input("Enter your age: ")
    return int(age)

def calculate_secs_from_yrs(age_years):
    return age_years * 365 * 24 * 3600

def prompt_user_and_calculate_age():
    age = ask_age()
    seconds_lived = calculate_secs_from_yrs(age)
    print("You have lived for {} seconds".format(seconds_lived))

prompt_user_and_calculate_age()
