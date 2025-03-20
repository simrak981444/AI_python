def grade_eligibility(score):
    if score >= 90:
       return "Wao! You have bagged GRADE A."
    elif score >= 80:
       return "GOOD! You have bagged GRADE B."
    elif score >= 70:
       return"You have bagged GRADE C."
    elif score >= 60:
        return"You have bagged GRADE D. NEED TO WORK HARD"
    else:
       return"You have bagged GRADE E. WORK HARD!!!"
score = int(input("Please enter your score: "))
result =(grade_eligibility(score))
print(result)