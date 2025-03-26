print('''
                 .
              /\\`.
      .------'\ \`.`-.
     /         \ \ `-.`------.
    |           \ \   `.-----'|
    [`-----------\//---'      |
     \             .---.      |
      `-._________/     \_____|  VK
      ''')

print("Wellcome to My Doggy ")

button = input("shall we move (y \ n)")
if button == "y":
    print("Let's start!")
    

print("Take you doggy to island")

choose = str(input("Will you choose to go right or left? \n"))
if choose == "right":
    print("ohhh....  you reached forest!")
    print("Game over!")
else:
    print("You have choosen right option!")
    print("move forward to island")
    
    choose1 = str(input("Will you take rope with you (y \ n)"))
    if choose1 == "y":
        print("hurryyy, you can reach island very fastly!")
        
        print("-----you reached the sea-----")
        boat = input("which boat will you choose to reach  your favorite island?")
        print("you have the option: yellow, green, red")
        
        if boat == "yellow":
            print("OPPP's you caught by crocodile!")
        elif boat == "green":
            print("You have choosen right one")
            
            print("Congradulations!  ")
        elif boat == "red":
            print("sorry, you have caught by octopus!")
    else:
        print("OPPPP's you got losed!")


