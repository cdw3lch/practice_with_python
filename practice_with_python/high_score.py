student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#Write your code below this row 👇
top_score = 0
for score in student_scores:  
    if score >= top_score:
        top_score = score
        
    
print(f'The highest score is {top_score}')