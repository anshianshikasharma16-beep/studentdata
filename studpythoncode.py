# STUDENT PERFORMANCE AND ATTENDANCE ANALYSIS
# Beginner-friendly project using only NumPy and Pandas

import numpy as np
import pandas as pd


# --------------------------------------------------
# 1. LOAD THE DATASET
# --------------------------------------------------

# Keep this Python file and the CSV dataset in the same folder.
data = pd.read_csv("student_performance_attendance.csv")

print("\n===== STUDENT PERFORMANCE AND ATTENDANCE ANALYSIS =====")
print("\nFirst five records:")
print(data.head())

print("\nDataset information:")
data.info()

print("\nNumber of rows and columns:")
print(data.shape)


# --------------------------------------------------
# 2. CHECK THE DATA
# --------------------------------------------------

print("\n===== DATA CHECK =====")

print("\nMissing values in each column:")
print(data.isnull().sum())

print("\nNumber of duplicate rows:")
print(data.duplicated().sum())


# --------------------------------------------------
# 3. OVERALL STUDENT PERFORMANCE
# --------------------------------------------------

def overall_performance():
    print("\n===== OVERALL PERFORMANCE =====")

    average_marks = data["Average_Marks"].mean()
    highest_marks = data["Average_Marks"].max()
    lowest_marks = data["Average_Marks"].min()

    print("Class average marks:", round(average_marks, 2))
    print("Highest student average:", highest_marks)
    print("Lowest student average:", lowest_marks)


# --------------------------------------------------
# 4. ATTENDANCE ANALYSIS
# --------------------------------------------------

def attendance_analysis():
    print("\n===== ATTENDANCE ANALYSIS =====")

    average_attendance = data["Attendance_Percentage"].mean()
    print("Average attendance:", round(average_attendance, 2), "%")

    # Students with attendance below 75 percent
    low_attendance = data[data["Attendance_Percentage"] < 75]

    print("\nStudents with attendance below 75%:")
    print(low_attendance[["Student_ID", "Attendance_Percentage"]])

    print("\nTotal students with short attendance:", len(low_attendance))


# --------------------------------------------------
# 5. SUBJECT-WISE PERFORMANCE
# --------------------------------------------------

def subject_analysis():
    print("\n===== SUBJECT-WISE PERFORMANCE =====")

    subjects = [
        "Mathematics_Marks",
        "Python_Marks",
        "Physics_Marks",
        "Communication_Marks"
    ]

    for subject in subjects:
        average = data[subject].mean()
        print(subject, "average:", round(average, 2))


# --------------------------------------------------
# 6. FIND THE TOP 10 STUDENTS
# --------------------------------------------------

def top_performers():
    print("\n===== TOP 10 PERFORMERS =====")

    # Sort students by average marks, from highest to lowest.
    top_students = data.sort_values(
        by="Average_Marks", ascending=False
    )

    print(top_students[
        ["Student_ID", "Average_Marks", "Attendance_Percentage"]
    ].head(10))


# --------------------------------------------------
# 7. CLASS-WISE PERFORMANCE
# --------------------------------------------------

def class_analysis():
    print("\n===== CLASS-WISE PERFORMANCE =====")

    class_names = data["Class"].unique()

    for class_name in class_names:
        class_data = data[data["Class"] == class_name]
        class_average = class_data["Average_Marks"].mean()
        print(class_name, "average marks:", round(class_average, 2))


# --------------------------------------------------
# 8. PERFORMANCE CATEGORY COUNT
# --------------------------------------------------

def performance_categories():
    print("\n===== PERFORMANCE CATEGORIES =====")

    category_count = data["Performance_Category"].value_counts()
    print(category_count)


# --------------------------------------------------
# 9. NUMPY ANALYSIS
# --------------------------------------------------

def attendance_marks_relationship():
    print("\n===== ATTENDANCE AND MARKS RELATIONSHIP =====")

    # Select the two columns and remove rows with missing values.
    relationship_data = data[
        ["Attendance_Percentage", "Average_Marks"]
    ].dropna()

    attendance = relationship_data["Attendance_Percentage"].to_numpy()
    marks = relationship_data["Average_Marks"].to_numpy()

    if len(attendance) < 2:
        print("Not enough data to calculate correlation.")
        return

    correlation = np.corrcoef(attendance, marks)[0, 1]

    print("Correlation between attendance and average marks:",
          round(correlation, 2))

    if correlation > 0:
        print("The relationship is positive.")
    elif correlation < 0:
        print("The relationship is negative.")
    else:
        print("There is no linear relationship.")


# --------------------------------------------------
# 10. RUN ALL THE PROJECT FUNCTIONS
# --------------------------------------------------

overall_performance()
attendance_analysis()
subject_analysis()
top_performers()
class_analysis()
performance_categories()
attendance_marks_relationship()

print("\n===== ANALYSIS COMPLETED =====")
