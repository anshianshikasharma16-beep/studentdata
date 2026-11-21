# STUDENT PERFORMANCE AND ATTENDANCE ANALYSIS
# Beginner-friendly project using Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. LOAD THE DATASET
# --------------------------------------------------

# Keep this Python file and the CSV dataset in the same folder.
data = pd.read_csv("student_performance_attendance.csv")

print("\n===== STUDENT PERFORMANCE AND ATTENDANCE ANALYSIS =====")
print("\nFirst five records:")
print(data.head())

print("\nDataset information:")
print(data.info())

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

    # A loop checks each subject one by one.
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

    print(top_students[["Student_ID", "Average_Marks", "Attendance_Percentage"]].head(10))


# --------------------------------------------------
# 7. CLASS-WISE PERFORMANCE
# --------------------------------------------------

def class_analysis():
    print("\n===== CLASS-WISE PERFORMANCE =====")

    # unique() gives us the different class names.
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
# 9. DATA VISUALIZATION
# --------------------------------------------------

def create_charts():
    print("\nCreating charts...")

    # Chart 1: Average marks in each subject
    subjects = [
        "Mathematics_Marks",
        "Python_Marks",
        "Physics_Marks",
        "Communication_Marks"
    ]

    subject_averages = []

    for subject in subjects:
        subject_averages.append(data[subject].mean())

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, subject_averages)
    plt.title("Average Marks in Each Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()

    # Chart 2: Attendance distribution
    plt.figure(figsize=(8, 5))
    plt.hist(data["Attendance_Percentage"], bins=10, edgecolor="black")
    plt.title("Student Attendance Distribution")
    plt.xlabel("Attendance Percentage")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()

    # Chart 3: Attendance compared with average marks
    plt.figure(figsize=(8, 5))
    plt.scatter(data["Attendance_Percentage"], data["Average_Marks"])
    plt.title("Attendance vs Academic Performance")
    plt.xlabel("Attendance Percentage")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.show()

    # Chart 4: Number of students in each performance category
    category_count = data["Performance_Category"].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(
        category_count,
        labels=category_count.index,
        autopct="%1.1f%%"
    )
    plt.title("Student Performance Categories")
    plt.show()


# --------------------------------------------------
# 10. RUN ALL THE PROJECT FUNCTIONS
# --------------------------------------------------

overall_performance()
attendance_analysis()
subject_analysis()
top_performers()
class_analysis()
performance_categories()
create_charts()

print("\n===== ANALYSIS COMPLETED =====")
