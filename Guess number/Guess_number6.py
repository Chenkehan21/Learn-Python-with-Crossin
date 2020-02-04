import requests
import os

def initialize():
    global name, info, info2
    name = input("Please tell me your name: ")
    if not os.path.exists("record2.txt"):
        with open("record2.txt", 'w'):
            pass
    with open("record2.txt", 'r+') as f:
        f.seek(0)
        info = [m.strip().split('\t') for m in f.readlines()]
        f.seek(0)
        info2 = f.read()
          
    global played_rounds, played_least_times, played_ave_times, played_total_guess_times    
    for i in info:
        if name in i:
            played_rounds = int(i[i.index(name) + 1])
            played_least_times = int(i[i.index(name) + 2])
            played_ave_times = float(i[i.index(name) + 3])
            played_total_guess_times = played_rounds * played_ave_times
            print("Hi %s, you have played %s rounds, you guessed the answer in at least %s times, "\
                  "you guessed the answer on average %s times each round."
                  % (name, i[i.index(name) + 1], i[i.index(name) + 2], i[i.index(name) + 3]))
            print("Let's start!", '\n')
    if name not in info2:
        try:
            with open("record2.txt", 'a') as f:
                f.seek(2)
                f.write("%s\t0\t0\t0\n" % name) # Creat a new record for new player.
        except:
            print("write failed!")
        played_rounds = 0
        played_least_times = 0
        played_ave_times = 0.0
        played_total_guess_times = 0.0
        print("%s you have played 0 round, you guessed the answer in at least 0 time, "\
        "you guess the answer on average 0 time each round." % name)
        print("Let's start!", '\n')

    print("You need to guess the number I think." + '\n' + "hint: It's an integer from 1 to 100")
    print('\n' + "Round1")


def guess_and_check():
    global guess_number
    global Bingo
    num_type = False
    while num_type == False:
        try:
            guess_number = int(input("Please enter your answer: ")) # make sure players enter right type.
        except:    
            print("You must enter an integer!!!")
        else:
            if type(guess_number) == int:
                Bingo = False
                break


def compare(result, count):
    guess_and_check()
    if guess_number < result:
        print("Too small!")
        return False
    elif guess_number > result:
        print("Too big!")
        return False
    else:
        print("Bingo!!!")
        print("You guessed %d times" % count + '\n')
        num.append(count)
        return replay()  # there must be "return replay()"!!! if omit "return", it doesn't work!!!


def replay():
    global Round, count, result, minimum
    Round = 1
    restart = input("Do you want to replay? (Press 'Y' or 'y' to continue, press any other key to quit): ")
    if restart == "Y" or restart == "y":
        url = "https://python666.cn/cls/number/guess/"
        req = requests.get(url)
        req.encoding = "gbk"
        result = eval(req.text)
        Round += 1
        print('\n' + "Round%d" % Round)
        count = 0
        return False
    else:
        average = sum(num) / len(num)
        print('\n' + "THIS TIME: you played %d rounds, you guessed the answer in at least %d times, "\
              "you need to guess %.2f times per round"
              % (Round, min(num), average))
        
        if played_least_times == 0:
                minimum = min(num)
        else:
            minimum = min(min(num), played_least_times)
        print('\n' + "TOTAL: you have played %d rounds, you guessed the answer in at least %d times, "\
              "you need to guess %.2f times per round"
              % (Round + played_rounds, minimum,
                         (sum(num) + played_total_guess_times) / (Round + played_rounds)))
        update()
        return True


def update():
    try:
        with open("record2.txt", 'r+') as f:
            f.seek(0)
            data = ''            
            for line in f.readlines():
                if line.find("%s" % name) == 0:
                    line = "%s\t%d\t%d\t%.2f" % (name, Round + played_rounds, minimum,
                     (sum(num) + played_total_guess_times) / (Round + played_rounds))
                    print(line)
                data += line
        with open("record2.txt", "r+") as f:
            f.writelines(data)
    except:
        print("open failed!")


def play():
    global result
    url = "https://python666.cn/cls/number/guess/"
    req = requests.get(url)
    req.encoding = "gbk"
    result = eval(req.text)
    global count
    initialize()
    while not compare(result, count):
        count += 1


count = 1
Round = 1
num = []
play()