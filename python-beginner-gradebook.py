last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Creating a list called subjects and filling it with classes

subjects = ["physics", "calculus", "poetry", "history"]

# Creating a list called grades and filling it with scores

grades = [98, 97, 85, 88]

# Creating a two-dimensional list combining subjects and grades

gradebook = [["physics", 98],["calculus", 97],["poetry", 85],["history", 88]]

# Printing gradebook

print(gradebook)

# Adding more subjects

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modifying the grade

gradebook[5][1] = 98

# Removing score value from the poetry class

gradebook[2].remove(85)

# Adding "Pass" instead of a score number to poetry class

gradebook[2].append("Pass")

# Adding last years grade and creating new gradebook

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)