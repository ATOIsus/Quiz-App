
import random 
import pickle



file_open = input("Enter the file to open: ")
file = open(f'Resource/1) Question/{file_open}.txt', 'rb')
ques = pickle.load(file)



question_str = []
anser = []
option1 = [] 
option2 = []
option3 = []
score = 0

for i in ques:
            
    if len(i) == 3 or len(i) == 4:
        option2.append('Both')
        option3.append('Neither')
 
    for j in range(len(i)) :
        if j == 0:
            question_str.append(str(i[0]))
        elif j == 1:
            anser.append(str(i[1])) 
        elif j == 2:
            option1.append(str(i[2]))
        elif j == 3:
            option2.append(str(i[3]))
        elif j == 4:
            option3.append(str(i[4]))
        else:
            pass




for k in range(len(ques)):
    
    choice = [anser[k], option1[k], option2[k], option3[k]]    
    random.shuffle(choice)

    print()
    print(question_str[k])
    print()

    print('1) ' + choice[0])
    print('2) ' + choice[1])
    print('3) ' + choice[2])
    print('4) ' + choice[3])
    print()

    ans = int(input('Enter the answer: '))

    if choice[ans-1] == anser[k]:
        score += 1
    else:
        print()
        print(f"Wrong! The right answer was {anser[k]}")
        print()



print(f'Your score is {score} out of {len(ques)}')


