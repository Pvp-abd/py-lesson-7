c= ["fart","poop","food","dove","dave"]
print("class list:",c)

print("total kids:",len(c))
print("first student:",c[0])
print("last student:",c[-1])
print("first three:",c[:3])

c.append("essen")
print("/nAfter adding essen:",c)
c.remove ("dave")
print("after removing dave:",c)
c.sort()
print("sorted aphabetically:",c)
c.reverse()
print("reversed:",c)

teacher = {"name": "Mr. Sharma", "subject": "Python", "experience": 5}
print("\nTeacher profile:", teacher)

print("Subject:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not found"))
teacher["experience"] = 6
teacher["email"] = "sharma@school.com"
teacher.pop("experience")
print("Updated teacher profile:", teacher)

roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Meera"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student at Roll 3:", student_directory[3])