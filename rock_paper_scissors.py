import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps =[rock,paper,scissors]

player_choice_str=input("What do you choose? Print 0 for rock, 1 for paper, 2 for scissors\n")
input_range= ['0','1','2']
if player_choice_str not in input_range:
  print("You typed an invalid number, you lose!")
else:
  player_choice=int(player_choice_str)
  print(rps[player_choice])
  randomindex = random.randint(0,2)
  print("Computer choice:\n" + rps[randomindex])

  if randomindex==player_choice:
    print("It's a draw")
  elif player_choice==0 and randomindex==2:
    print("You win")
  elif player_choice==2 and randomindex==0:
    print("You loose")
  elif player_choice > randomindex:
    print("You win")
  elif player_choice < randomindex:
    print("You loose")  
