# MINI AI PROJECT 1: AI RESUME SCANNER
# print("=" * 50)
# print("                AI RESUME SCANNER")
# print("=" *50)

# keywords = [
#     "python",
#     "sql",
#     "machine learning",
#     "cloud",
#     "ai"
# ]
# resume = input("Paste Resume Text: ")
# resume = resume.lower()
# score = 0

# for keyword in keywords:
#     if keyword in resume:
#         score += 1
#         print(keyword, "FOUND")

# print()

# print("Resume Score: ", score)

# if score >= 4:
#     print("Excellent Match")
# elif score >= 2:
#     print("Good Match")
# else:
#     print("Needs Improvement") 

# MINI AI PROJECT 2: AI SENTIMENT DETECTOR
# print("=" *50)
# print("        AI SENTIMENT DETECTOR")
# print("=" *50)

# positive_words = [
#     "good",
#     "excellent",
#     "great",
#     "amazing"
# ]

# comment = input("Comment: ")

# comment = comment.lower()

# positive_count = 0

# for word in positive_words:
#     if word in comment:
#         positive_count += 1
# print()

# print("Positive Score: ", positive_count)

# if positive_count >= 3:
#     print("Very Positive Feeddback")
# elif positive_count >= 1:
#     print("Positive Feedback")
# else:
#     print("Neutral Feedback")

# MINI AI PROJECT 3: STUDENT PERFORMANCE ANALYZER
print("=" *50)
print("        STUDENT PERFORMANCE ANALYZER")
print("=" *50)

students = {
    "John":88,
    "Mary":95,
    "David":72,
    "Sarah":91
}

highest_student = ""
highest_score = 0

total_score = 0

for student in students:
    score = students[student]
    total_score += score
    if score > highest_score:
        highest_score = score
        highest_student = student

average_score = total_score / len(students)

print()

print("Top Student : ",highest_student)
print("Highest Score : ",highest_score)
print("Average Score: ", average_score)