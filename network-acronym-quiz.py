print("Welcome to My TCPIP Quiz!")

playing = input("Would you like to play?")

if playing.lower() != "yes":
    quit()

print("OK! Lets play!")
score =0
answer = input("What does LAN stand for? ")
if answer.lower() == "local area network":
    print('Correct!')
    score += 1
else:
    print("Incorrect")    
answer = input("What does RDP stand for? ")
if answer.lower() == "remote desktop protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect")    
answer = input("What does SMTP stand for? ")
if answer.lower() == "simple mail transfer protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect")          

print("You got " + str(score) + " question correct!!")
print("You got " + str(score/4 * 100) + "%.!!")