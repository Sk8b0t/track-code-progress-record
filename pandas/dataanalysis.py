import pandas as pd
import numpy as np
d = {
    "student_id": [
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 119, 120
    ],
    "name": [
        "Aarav Sharma", "Ananya Iyer", "Vivaan Patel", "Diya Nair", "Kabir Verma",
        "Isha Gupta", "Arjun Reddy", "Kiara Joshi", "Sai Teja", "Riya Sen",
        "Rohan Das", "Meera Rao", "Aditya Mishra", "Sanya Malhotra", "Dev Shah",
        "Tanya Kapoor", "Yash Singhal", "Kavya Saxena", "Pranav Choudhury", "Avani Deshmukh"
    ],
    "course": [
        "Computer Science", "Data Science", "Mathematics", "Physics", "Chemistry",
        "Biology", "Mechanical Eng.", "Electrical Eng.", "Computer Science", "Data Science",
        "Economics", "Psychology", "Statistics", "Civil Eng.", "Business Admin.",
        "Literature", "History", "Political Science", "Computer Science", "Data Science"
    ],
    "gpa": [
        3.8, 3.9, 3.4, 3.7, 3.1,
        3.6, 3.2, 3.5, 9.0, 3.3,
        3.6, 3.8, 3.5, 3.0, 9.7,
        3.9, 3.2, 3.4, 3.6, 3.8
    ]
}


df=pd.DataFrame(d)
print(df)
print(df.describe())
df.to_csv("student_data.csv",index=False)
print(df.to_string(index=False))
ser=pd.Series(np.random.rand(10))
print(ser)
df.to_numpy()
print(df.columns)
print(df.T)
