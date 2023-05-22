height = float(input("How tall are you in m?"))
weight = float(input("How much do you weigh in kg?"))

bmi = round(weight/(height**2),1)
print(bmi)

if bmi <= 18.5:
    print(f"Your BMI is {bmi} and that means you are Underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and that means you have Normal Weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} and that means you are Overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi} and that means you are Obese")
else:
    print("You are Clinically Obese")


