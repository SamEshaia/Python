#This quiz game, the idea behind it is we want to ask the users a bunch of questions, we will add 1 to their score.
#Then at the end of the program we'll print out what they got out of the number of questions.
#For example, if there was 10 questions, we would say: "Hey. You got 7 out of 10" and give them a percentage.



print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does DHCP stand for? ")
if answer.lower() == "dynamic host configuration protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTTP stand for? ")
if answer.lower() == "hypertext transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does TCP stand for? ")
if answer.lower() == "transmission control protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does UDP stand for? ")
if answer.lower() == "user datagram protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does DNS stand for? ")
if answer.lower() == "domain name system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RDP stand for? ")
if answer.lower() == "remote desktop protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SSH stand for? ")
if answer.lower() == "secure shell":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ICMP stand for? ")
if answer.lower() == "internet control message protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/10) * 100) + "%.")