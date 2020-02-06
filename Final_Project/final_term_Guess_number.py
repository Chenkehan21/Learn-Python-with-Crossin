import requests
import pandas as pd
import os

def initialize():
    global name, name_id, data, player, played_rounds, played_Least_times, played_ave, played_total_times, result
    global count, Round, num
    if not os.path.exists("RECORD.xlsx"):
        df = pd.DataFrame(columns=['Name', 'Rounds', 'Least_times', 'Average_times', 'Total_times'])
        df.to_excel("RECORD.xlsx", index=False)
    info = pd.read_excel("RECORD.xlsx")
    name = input("Please input your name: ")
    if name in list(info['Name']): # convert to a list to check !!!
        name_id = info[info['Name'] == name].index[0]
        data = info.loc[name_id]
        player = data["Name"]
        played_rounds = data["Rounds"]
        played_Least_times = data["Least_times"]
        played_ave = data["Average_times"]
        played_total_times = data["Total_times"]
        print("Hi %s, you have played %d rounds, you guessed the answer in at least %d times, "\
                  "you guessed the answer on average %.2f times each round."
                  % (player, played_rounds, played_Least_times, played_ave))
#         print(info)
#         print(name_id)
    else:
        info.loc[''] = [name, 0, 0, 0.0, 0]
        info.to_excel("RECORD.xlsx", index=False)
        info = pd.read_excel("RECORD.xlsx")
#         print(info)
        name_id = info[info['Name'] == name].index[0]
#         print("name_id: ", name_id)
        played_rounds = 0
        played_Least_times = 0
        played_ave = 0.0
        played_total_times = 0
        print("%s you have played 0 round, you guessed the answer in at least 0 time, "\
        "you guess the answer on average 0 time each round." % name)
        info.to_excel("RECORD.xlsx", index=False)
    print("\nRound1")
    result = get_result()
    count = 1
    Round = 1
    num = []
#     print(result)

    
def guess_and_check():
    global guess_number, Bingo
    num_type = False
    while num_type == False:
        try:
            guess_number = int(input("Please enter your answer: "))
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
    global Round, count, result, minimum, new_rounds, new_total, new_ave
    if played_Least_times == 0:
        minimum = min(num)
    else:
        minimum = min(min(num), played_Least_times)   
    restart = input("Do you want to replay? (Press 'Y' or 'y' to continue, press any other keys to quit): ")
    if restart == "Y" or restart == "y":
        result = get_result()
#         print(result)
        Round += 1
        print('\n' + "Round%d" % Round)
        count = 0
        return False
    else:
        average = sum(num) / len(num)
        new_rounds = Round + played_rounds
        new_total = played_total_times + sum(num)
        new_ave = new_total / new_rounds
        print('\n' + "THIS TIME: you played %d rounds, you guessed the answer in at least %d times, "\
              "you need to guess %.2f times per round"
              % (Round, min(num), average))           
        print('\n' + "TOTAL: you have played %d rounds, you guessed the answer in at least %d times, "\
              "you need to guess %.2f times per round" % (new_rounds, minimum, new_ave))
        update()
        return True

    
def update():
    info2 = pd.read_excel("RECORD.xlsx")
    info2.loc[name_id] = [name, new_rounds, minimum, new_ave, new_total]  # update   !!!
    info2.to_excel("RECORD.xlsx", index=False) # must save !!!              

    
def get_result():
    url = "https://python666.cn/cls/number/guess/"
    req = requests.get(url)
    req.encoding = "gbk"
    result = eval(req.text)
    return result
              
              
def play():
    global result, count
    initialize()
    while not compare(result, count):
        count += 1


play()