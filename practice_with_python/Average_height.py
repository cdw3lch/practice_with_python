student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
for heights in student_heights:
    total += int(heights)

avg_mean = round(total / int(len(student_heights)))
print(avg_mean)
