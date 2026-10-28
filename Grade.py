
import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Student": ["Rahul", "Priya", "Amit", "Sneha", "Neha"],
    "Marks": [92, 78, 65, 45, 85]
}

df = pd.DataFrame(data)

# Calculate grades
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Marks"].apply(get_grade)

# Display student details
print("STUDENT GRADE DISTRIBUTION ANALYSIS")
print("Project by: Kshitija Mohite")
print(df)

# Grade distribution
grade_count = df["Grade"].value_counts()

print("\nGrade Distribution:")
print(grade_count)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# Create bar chart
grade_count.plot(kind="bar")

plt.title("Student Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
