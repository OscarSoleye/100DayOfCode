# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
height_count = 0
sum_height = 0
for height in student_heights:
    sum_height = height + sum_height
    height_count += 1

average = int(sum_height / height_count)

print(average)


