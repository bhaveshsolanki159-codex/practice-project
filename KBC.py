ques=[
    ["Which planet is known as the Red Planet?","Earth","Venus","Mars","Jupiter", 3],
    ["What is the capital of India?","Mumbai", "Delhi","Kolkata","Chennai",2],
    ["What is the capital of India?","Mumbai", "Delhi","Kolkata","Chennai",2]
]

print("Welcome to KBC")
prize = [1000, 2000, 3000, 5000, 10000]
choice=input("Enter your choice (yes/no): ")
if choice.lower()=='yes':
    for i ,q in enumerate(ques,start=1):
        if i == 1:
            print(f"lets start with your {i} question")
        if i>0 and i<len(ques):
            print(f"{i}.{q[0]}")
            print(f"1.{q[1]}\t 2.{q[2]}")
            print(f"3.{q[3]}\t 4.{q[4]}")
            ans = int(input("Enter your answer:"))
            if ans == q[5]:
                overall_prize = prize[i]
                print(f"congratulation you have given correct answer,you had won {prize[i]} Rs")
                print("\n \n")
            else:
                print("sorry you have given wrong answer")
                break
        else:
            break
print(f"you have won {overall_prize} Rs")   