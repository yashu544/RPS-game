import random
user_score=0
comp_score=0
for i in range(5):
    arr=["rock","paper","scissor"]
    a=random.randint(0,2)
    c_choice=arr[a]
    u_choice=input("enter choice:").lower()
    if u_choice not in arr:
        print("invalid choice")
    else:
        if c_choice=="paper" and u_choice=="rock":
            comp_score+=1
            print("comp won")
        elif c_choice=="scissor" and u_choice=="paper":
            comp_score+=1
            print("comp won")
        elif c_choice=="rock" and u_choice=="scissor":
            comp_score+=1
            print("comp won")
        elif c_choice==u_choice:
            print("draw match")
            pass
        else:
            print("user won")
            user_score+=1
    print(f"comp:{comp_score},user:{user_score}")
if user_score>comp_score:
    print("user won")
else:
    print("comp won")
