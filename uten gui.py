import random
import pygame, sys





board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
def dboard():
    print(board[0] + board[1] + board[2])
    print(board[3] + board[4] + board[5])
    print(board[6] + board[7] + board[8])


def game():
    count = 0

    for i in range(10):
        dboard()
        if count % 2 == 0:
            turn = "X"
        else:
            turn = "O"

        choice = input("choose where u want to play " + turn )
        if choice == "a1":
            board[0] = turn
            count += 1
            print(count)
        elif choice == "a2":
            board[1] = turn
            count += 1
            print(count)

        elif choice == "a3":
            board[2] = turn
            count += 1
        elif choice == "b1":
            board[3] = turn
            count += 1
        elif choice == "b2":
            board[4] = turn
            count += 1
        elif choice == "b3":
            board[5] = turn
            count += 1
        elif choice == "c1":
            board[6] = turn
            count += 1
        elif choice == "c2":
            board[7] = turn
            count += 1
        elif choice == "c3":
            board[8] = turn
            count += 1
        else:
            print("?")

        if count > 5:
            if board[0] == board[1] == board[2] != "":
                print("Won " + turn)
                dboard()
                break
            elif board[3] == board[4] == board[5] != "":
                print("Won " + turn)
                dboard()
                break
            elif board[6] == board[7] == board[8] != "":
                print("Won " + turn)
                dboard()
                break
            elif board[0] == board[4] == board[8] != "":
                print("Won " + turn)
                dboard()
                break
            elif board[2] == board[4] == board[6] != "":
                print("Won " + turn)
                dboard()
                break
            elif board[0] == board[3] == board[6] != "":
                print("Won " + turn)
                dboard()
                break
            elif board[1] == board[4] == board[7] != "":
                print("Won " + turn)
                dboard()
                break
            elif board[2] == board[5] == board[8] != "":
                print("Won " + turn)
                dboard()
                break
            else:
                pass


        if count == 8:
            print("draw")


game()






