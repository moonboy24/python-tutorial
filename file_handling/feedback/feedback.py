
# feedback = input("Enter your feedback: ")
# with open("feedback.txt" , "a") as log:
#     log.write(feedback + "\n")   
# print("Thanks , your feedback has been received")

# with open("feedback.txt" , "r") as log:
#     print(log.readlines().strip())

# with open("feedback.txt") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         if "good" in line:
#             print(line.strip())

with open("feedback.txt") as f:
    for _ in range(3):
        print(f.readline().strip())