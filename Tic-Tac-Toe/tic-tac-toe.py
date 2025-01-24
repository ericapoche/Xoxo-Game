from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random


def with_player(row, column):
    global player, player_scores

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player

        # Set background color based on the player's turn
        color = "lightblue" if player == "O" else "lightcoral"
        buttons[row][column]['bg'] = color

        if len([button['text'] for row in buttons for button in row if button['text'] != ""]) >= 3:
            if check_winner():
                messagebox.showinfo("Game Over", f"Player {player} wins!")
                player_scores[player] += 1
                update_scores()
                new_game()
                return True

        if not empty_spaces():
            messagebox.showinfo("Game Over", "It's a Tie!")
            player_scores["X"] += 1
            player_scores["O"] += 1
            update_scores()
            new_game()
        else:
            player = players[1] if player == players[0] else players[0]
            update_turn_label()


def update_turn_label():
    turn_label.config(text=f"Player's Turn: ({player})")
    
def update_scores():
    score_label.config(text=f"Scores: X - {player_scores['X']} | O - {player_scores['O']}")


def empty_spaces():
    return any(buttons[row][column]['text'] == "" for row in range(3) for column in range(3))


def check_winner():
    for line in [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]:
        if all(buttons[row][column]['text'] == player for row, column in line) and buttons[line[0][0]][line[0][1]]['text'] != "":
            return True

    for x in range(3):
        if all(buttons[x][o]['text'] == player for o in range(3)) or all(buttons[o][x]['text'] == player for o in range(3)):
            return True
        
    return False


def new_game():
    global player
    player = random.choice(players)

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white")

    update_turn_label()

def restart():
    global player_scores
    player_scores = {"X" : 0, "O" : 0}
    update_scores()
    new_game()

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def confirm_exit():
    result = messagebox.askquestion("Confirm Exit", "Are you sure you want to exit?")
    if result == 'yes':
        window.destroy()


# Create a Tkinter window
window = Tk()
window.geometry("260x480")
window.attributes('-alpha', 0.95)
window.resizable(False, False)
window.configure()

# Background Image
try:
    pil_image = Image.open("image/bg.jpg")
    background_image = ImageTk.PhotoImage(pil_image)
    background_label = Label(window, image=background_image)
    background_label.place(relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading background image: {e}")

# Set up players, initial player, and player scores
players = ["X", "O"]
player = random.choice(players)
player_scores = {"X": 0, "O": 0}

# Header Label
label = Label(window, text="Tic-Tac-Toe", font=('Times New Roman', 20, 'bold'), background="#40A2D8", fg="white")
label.pack(pady=20)

# Game Board Frame
game_frame = Frame(window, background="#40A2D8", bd=2)
game_frame.pack(pady=45)

# Buttons
buttons = [[0, 0, 0] for _ in range(3)]

for x in range(3):
    for o in range(3):
        buttons[x][o] = Button(game_frame, text="", font=('Arial', 12, 'bold'),
                               command=lambda x=x, o=o: with_player(x, o), bg="white", bd=2)
        buttons[x][o].grid(row=x, column=o, padx=5, pady=5, ipadx=15, ipady=10)

# Turn Label
turn_label = Label(window, text=f"Player's Turn: ({player})", font=('Roboto', 13, 'bold'), bg="black", fg="#0D9276")
turn_label.place(x=60, y=73)

# Scores Label
score_label = Label(window, text=f"Scores: X - {player_scores['X']} | O - {player_scores['O']}",
                    font=('Roboto', 12, 'bold'), bg="white", fg="black")
score_label.place(x=50, y=350)

# Control Buttons
control_frame = Frame(window)
control_frame.pack(pady=70)

restart_button = Button(window, text="Restart", width=6, font=('Arial', 14), bg='green', fg='white', command=restart)
restart_button.place(x=40, y=400)

exit_button = Button(window, text="Exit", width=6, font=('Arial', 14), bg='red', fg='white', command=confirm_exit)
exit_button.place(x=145, y=400)

# Center the window
center_window(window)

window.mainloop()

#TicTacToeeee
#Game