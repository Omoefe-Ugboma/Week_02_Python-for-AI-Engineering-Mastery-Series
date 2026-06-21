# STRING MANIPULATION
# EXAMPLE 1: NAME FORMATTER
# name = "joHn sMith"
# print(name.upper())
# print(name.lower())
# print(name.title())

# EXAMPLE 2: CHAT MESSAGE CLEANER
# message = "     hello ai engineer   "
# print(message)
# clean_message = message.strip()
# print(clean_message)

# EXMAPLE 3: PROMPT ANALYZER
# prompt = input("Enter Prompt: ")
# print("Characters: ",len(prompt))
# print("Words: ", len(prompt.split()))
# EXAMPLE 4: EMAIL VALIDATION

# email = input("Enter Email:")
# if"@" in email:
#     print("Valid Email")
# else:
#     print("Invalid Email")
# PROJECT: CUSTOMER FEEDBACK ANALYZER
feedback = input("Enter Feedback:")
print()

print("Original Feedback:")
print(feedback)
print()
print("Upper Case:")
print(feedback.upper())
print()
print("Word Split:")
print(feedback.split())

print("Word Count:")
print(len(feedback.split()))