from node import *
import maze as mz
import score_new
import interface
import time

import numpy as np
import pandas
import time
import sys
import os

#執行的任務：匯入迷宮、紀錄分數、創建溝通介面、決定遊戲模式
def main():
    #讀取迷宮
<<<<<<< HEAD
    maze = mz.Maze("data/small_maze.csv")
=======
    maze = mz.Maze("data/final_map.csv")
    while True:
        try:
            interf = interface.interface()
            time.sleep(3)
            break
        except:
            pass 
>>>>>>> 6a88a4b7f5079e58aede62d5cd502295f011db22
    #建立計分表 在執行檔案時記得把遊戲模式當參數傳入!!!!
    point = score_new.Scoreboard("data/medium_maze_UID.csv", "Gru", sys.argv[1])    
    #建立溝通介面
    #在這裡會先要求輸入port，如果輸入quit則斷線
    
    # TODO : Initialize necessary variables
    maze.setNode()
    maze.nd_dict["h"] = "haha"

    #清除快取
    time.sleep(0.5)
    interf.ser.ser.flushInput()
    if (sys.argv[1] == '0'):
        print("Mode 0: for treasure-hunting with rule 1")
        # TODO : for treasure-hunting with rule 1, which encourages you to hunt as many scores as possible
        interf.send_action(input("Press s to activate: "))
        car_dir = 2                                                             
        #找到完整路徑(最近)
        interf.tell_you("---------------------------------------------------------------------------")
        solution = maze.strategy(1)
        interf.tell_you("Shortest path: {}".format(solution))
        #傳送指令給車，等到達下一個節點再傳送指令
        complete = False
        UID = 0
        while not complete:
            #先檢查藍芽
            if not interf.ser.is_open():
                interf.tell_you("Disconncted!")
                interf = interface.interface()
            #一條路徑跑完
            for i in range(len(solution)-1):
                information = maze.getAction(car_dir, solution[i], solution[i+1])
                interf.tell_you("Information: {}".format(information))
                #送這個東西的當下會馬上寫一樣的東西進buffer
                interf.send_action(information[0])
                #車收到指令開始計時(t=0)
                #我收到同樣的東西後洗掉
                if(information[0] == "2"):
                    time.sleep(2)
                    try:
                        UID = interf.get_UID()
                    except:
                        interf.tell_you("Wrong format")
                    print("UID ------", UID)
                    interf.send_action("c")
                    time.sleep(1)

                #等車子回傳一模一樣的指令
                time.sleep(0.5)
                try:
                    interf.tell_you("I have already received: {}".format(interf.get_status()))
                except:
                    pass
                #等車子送到達的hint
                #指令洗掉了
                try:
                    while not interf.arrival():
                        pass
                except:
                    interf.tell_you("Wrong format")
                car_dir = information[1]
            interf.tell_you("Arrive!")
            maze.nodes[solution[-2]-1].unvisited_deadend = False
            
            if UID:
                interf.tell_you(UID)
                point.add_UID(UID)
            interf.tell_you("Current score: {}".format(point.getCurrentScore()))
            interf.tell_you("---------------------------------------------------------------------------")
                
            solution = maze.strategy(solution[-1])
            if solution == "haha":
                complete = True
            else:
                complete = False
<<<<<<< HEAD

=======
>>>>>>> 6a88a4b7f5079e58aede62d5cd502295f011db22
                interf.tell_you("Shortest path: {}".format(solution))
            
        interf.tell_you("Mission completed!")
        interf.tell_you("Total score: {}".format(point.getCurrentScore()))
        input("Press enter to close.")
        try:
            not interf.ser.is_open()
        except:
            interf.end_process()
        
    elif (sys.argv[1] == '1'):
        print("Mode 1: for treasure-hunting with rule 2")
        # TODO : for treasure-hunting with rule 2, which requires you to hunt as many specified treasures as possible
        car_dir = 2
        UID = 0
        #傳送開始指令給車
        route = [1, 8, 24, 44, 41, 36]
        interf.send_action(input("Press s to start: "))
        cp = 1 # current point's order
        while cp < len(route):
            #找到路徑
            solution = maze.strategy_2(route[cp-1], route[cp])
            route[cp] = solution[-1]
            interf.tell_you("Shortest path: {}".format(solution))
            #一條路徑跑完
            for i in range(len(solution)-1):
                information = maze.getAction(car_dir, solution[i], solution[i+1])
                interf.tell_you(information)
                interf.send_action(information[0])
                if(information[0] == "2"):
                    time.sleep(2)
                    try:
                        UID = interf.get_UID()
                    except:
                        pass
                    print("UID ------", UID)
                    while not UID:
                        interf.send_action("g")
                        time.sleep(1)
                        try:
                            UID = interf.get_UID()
                            print("UID ------", UID)
                            if len(UID) != 8:
                                UID = ""
                        except:
                            interf.tell_you("Wrong format")
                    interf.send_action("c")
                    time.sleep(1)
                #等車子回傳一模一樣的指令
                time.sleep(0.5)
                try:
                    interf.tell_you("I have already received: {}".format(interf.get_status()))
                except:
                    interf.tell_you("Wrong format")
                #等車子送到達的hint
                #指令洗掉了
                try:
                    while not interf.arrival():
                        pass
                except:
                    interf.tell_you("Wrong format")
                car_dir = information[1]
            if UID:
                interf.tell_you(UID)
                point.add_UID(UID)
            interf.tell_you("Current score: {}".format(point.getCurrentScore()))
            interf.tell_you("---------------------------------------------------------------------------")
            cp += 1
        # completed !
        interf.tell_you("Mission completed!")
        interf.tell_you("Total score: {}".format(point.getCurrentScore()))
        input("Press enter to close.")
        try:
            not interf.ser.is_open()
        except:
            interf.end_process()
        

    #自我測試：執行main之後，在interface(terminal)傳送指令，儲存到藍芽
    elif (sys.argv[1] == '2'):
        print("Mode 2: Self-testing mode.")
        # TODO: You can write your code to test specific function.
        action = 1
        while(action):
            action = input("What should I do: ")
            legal = False
            for i in range(6):
                legal = legal or (action == str(i))
            if legal or action == "s":
                interf.send_action(str(action))
                reception = interf.get_status()
                print("I have already received: {}".format(reception))
            elif action == "exit":
                interf.end_process()
                print("Bye bye ~~~")
                break
            else:
                print("You have send a wrong instruction. Please try again.")

if __name__ == '__main__':
    main()
