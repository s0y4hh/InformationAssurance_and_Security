"""Simple Password Strenght Checker"""
import string

def check_password_strength(password):
    """Check password strength
    Criteria: 
    - At least 8 characters
    - At least 1 digit
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 special character
    """
    
    """Strength Rating
    Strong: meets all criteria
    moderate: meets 3 or 4 criteria
    Weak: meets less than 3 criteria
    """
    if password == "":
        return False
    rating = 0
    if len(password) >= 8:
        rating += 1
        if any(c.isdigit() for c in password):
            rating += 1
            if any(c.isupper() for c in password):
                rating += password.isupper().count(True)
                if any(c.islower() for c in password):
                    rating += password.islower().count(True)

                    if any(c in string.punctuation for c in password):
                        rating += 1
                        
    if rating == 5:
        return "Strong"
    elif rating >= 3:
        return "Moderate"
    else:
        return "Weak"
def main():
    password = input("Enter a password: ")
    if check_password_strength(password) == False:
        print("\nPassword cannot be empty")
        main()
    else:
        print(f"Password strength: {check_password_strength(password)}")
if __name__ == "__main__":
    main()