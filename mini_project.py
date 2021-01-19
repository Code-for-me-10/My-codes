# weighted exam score average
# Entering how many exams you have done
number_of_exams = int(input("Enter the number of exam:"))
# print(number_of_exams)
# entering how many credit this exam cover
total_credits = int(input("Enter how many credits these exam cover: "))


average = 0
for exam in range(number_of_exams):
     score = int(input("Enter exam score:"))
     exam_credits = int(input("enter how many credit these exam covered:"))
     average = average + score*exam_credits/total_credits
     print("your average is", average)






