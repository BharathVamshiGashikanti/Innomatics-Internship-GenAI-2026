# List of student marks
marks = [45, 78, 90, 33, 60]

# Initialize counters for pass and fail students
pass_count = 0
fail_count = 0

# Loop through each student's marks
for mark in marks:
    # Check if the student passed
    if mark >= 50:
        pass_count += 1  # Increase pass counter
    else:
        fail_count += 1  # Increase fail counter

# Print the final results clearly
print("Total Students :", len(marks))
print("Number of Students Passed :", pass_count)
print("Number of Students Failed :", fail_count)
