# Working with List Comprehension
# EXAMPLE 1: BASIC LIST COMPREHENSION
# numbers = [
#     number for number in range(1,11)
# ]

# print(numbers)

# EXAMPLE 2: AI SCORE BOOSTER
# scores = [
#     60,
#     70,
#     80,
#     90
# ]
# boosted_scores = [
#     score + 5
#     for score in scores
# ]
# print(boosted_scores)

# EXAMPLE CANDIDATE FILTER
# scores = [
#     45,
#     82,
#     90,
#     55,
#     72
# ]
# qualified = [
#     score
#     for score in scores
#     if score >= 70
# ]
# print(qualified)

# EXAMPLE 4: DATA NORMALIZATION
# values = [
#     100,
#     200,
#     300,
#     400
# ]
# normalized = [
#     value / 100
#     for value in values
# ]
# print(normalized)

# EXERCISES
# Create a list,
# Add 10 to every number
# Create another list