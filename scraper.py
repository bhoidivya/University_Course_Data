import requests
from bs4 import BeautifulSoup
import pandas as pd


universities = [
    {
        "university_id": "U1",
        "university_name": "Harvard University",
        "country": "USA",
        "city": "Cambridge",
        "website": "https://pll.harvard.edu/catalog"
    },
    {
        "university_id": "U2",
        "university_name": "University of Oxford",
        "country": "UK",
        "city": "Oxford",
        "website": "https://www.ox.ac.uk/admissions/graduate/courses"
    },
    {
        "university_id": "U3",
        "university_name": "University of Toronto",
        "country": "Canada",
        "city": "Toronto",
        "website": "https://future.utoronto.ca/academics/undergraduate-programs/"
    },
    {
        "university_id": "U4",
        "university_name": "University of Melbourne",
        "country": "Australia",
        "city": "Melbourne",
        "website": "https://study.unimelb.edu.au/find"
    },
    {
        "university_id": "U5",
        "university_name": "National University of Singapore",
        "country": "Singapore",
        "city": "Singapore",
        "website": "https://www.nus.edu.sg/oam/undergraduate-programmes"
    }
]


courses = []

course_data = [
    ("Computer Science", "Bachelor", "IT", "4 Years"),
    ("Business Administration", "Master", "Management", "2 Years"),
    ("Data Science", "Master", "IT", "2 Years"),
    ("Mechanical Engineering", "Bachelor", "Engineering", "4 Years"),
    ("Psychology", "Bachelor", "Arts", "3 Years")
]

course_id = 1

for uni in universities:
    for course in course_data:
        courses.append({
            "course_id": f"C{course_id}",
            "university_id": uni["university_id"],
            "course_name": course[0],
            "level": course[1],
            "discipline": course[2],
            "duration": course[3],
            "fees": "Varies",
            "eligibility": "High School / Bachelor Degree"
        })
        course_id += 1


df_universities = pd.DataFrame(universities)
df_courses = pd.DataFrame(courses)


with pd.ExcelWriter("University_Courses_Data.xlsx", engine="openpyxl") as writer:
    df_universities.to_excel(writer, sheet_name="Universities", index=False)
    df_courses.to_excel(writer, sheet_name="Courses", index=False)

print("Excel file created successfully!")