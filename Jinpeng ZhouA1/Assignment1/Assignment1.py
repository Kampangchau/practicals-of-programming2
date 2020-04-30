"""
Replace the contents of this module docstring with your own details
Name: Zhou Jinpeng
Date started: 30/4/2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-01-songs-app-Kampangchau.git
"""

MENU = """Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit
"""

def main():
    # This function involves the printing Menu and the choice
    print("Songs to Learn 1.0 - by Jinpeng Zhou")
    print(MENU)
    choice = input(">>> ").upper()
    all_songs = load_songs()
    while choice != "Q":  # If user enter Q, print the end message
        if choice == "L":
            list_songs(all_songs)
        elif choice == "A":
            all_songs.append(add_songs())
        elif choice == "C":
            led_songs(all_songs)
        else:  # If user enter other word, it will display the invalid message
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_to_file(all_songs)  # If user enter Q, it will overwrite the csv file
    print(len(all_songs), "7 songs saved to", 'songs.csv', "\nHave a nice day :)")


def load_songs():  # This function is used for open the csv file and put the data to the list
    all_songs = []  # Create a list for saving songs data
    songs_file = open('songs.csv', 'r')   # Open the csv file with 'r' read module
    for line in songs_file:
        line = line.strip("\n")
        song_director_year_list = line.split(",")
        all_songs.append(song_director_year_list)
    songs_file.close()
    return all_songs


def list_songs(all_songs):  # This function is used to display the songs list
    count = 0
    for i in range(len(all_songs)):   # Using the for loop with constant i
        if all_songs[i][3] == "c":
            count += 1  # If the movie is watched, count + 1
            symbol = " "
            print(" ", str(i) + ".", symbol, "", end="")
        else:
            symbol = "*"  # Add * symbol beside the learned songs list
            print(" ", str(i) + ".", symbol, "", end="")
        for j in range(len(all_songs[i]) - 2):  # Using the for loop to add the dash before the singer
            if j == 1:
                dash = "-"  # If there is a director, add the dash
            else:
                dash = ""  # Else add the blank
            print(dash, "{:30}".format(all_songs[i][j]), end=" ")
        print("({:4})".format(all_songs[i][-2]))
    print(len(all_songs) - count, "songs learned,", count, "songs learned,""songs still to learned")

def led_songs(all_songs):  # This function is used to mark the songs as learned
    count = 0
    for i in range(len(all_songs)):  # Using the for loop with constant i
        if all_songs[i][3] == "c":
            count += 1  # If the movie is watched, count + 1
            symbol = " "
        else:
            symbol = "*"  # Add * symbol beside the learned song list
        print(" ", str(i) + ".", symbol, "", end="")
        for j in range(len(all_songs[i]) - 2):  # Using the for loop to add the dash before the singer
            if j == 1:
                dash = "-"  # If there is a singer, add the dash
            else:
                dash = ""
            print(dash, "{:30}".format(all_songs[i][j]), end=" ")  # Printing format
        print("({:4})".format(all_songs[i][-2]))
    if count == 0:
        print("No more songs to learn! Please kindly enter Q to Quit")

    print(len(all_songs) - count, "songs learned,", count, "songs still to learned")
    song_number = count_number("Enter the number of a song to mark as learned\n>>> ")  # Asking which number of song that user want to learn
    if all_songs[song_number][3] == "u":  # If there is "u" in forth position in csv file, it show the duplicate message
        print("You have already learned", all_songs[song_number][0])
    else:
        all_songs[song_number][3] = "u"
        print(all_songs[song_number][0], "by", all_songs[song_number][1], "learned")  # Print which songs has been learned
        return all_songs


def count_number(choice):
    valid = False  # to make variable as False
    while not valid:
        try:
            input_number = int(input(choice))
            if input_number < 0:  # If the user input is less than 0, display the following message
                print("Number must be >= 0")
            elif input_number >= 7:   # If the user input more than 7, display the following message
                print("Song number is not in the list")
            else:
                return input_number
        except ValueError:  # except the error
            print("Invalid input; enter a valid number")

def add_songs():   # This function is used for adding new song
    new_song = []  # Create a list to save the new song detail
    song_title = word_input("Title: ")  # Ask for the title
    singer = word_input("Singer: ")  # Ask for the singer
    year = str(count_number_year("Year: "))  # Ask for the song year
    new_song.append(song_title)
    new_song.append(singer)
    new_song.append(year)
    new_song.append("c")
    print(song_title, "by", singer, "({:4})".format(year), "added to song list")  # Print and show new songs details to user
    return new_song


def word_input(choice):  # This function is used for collecting user put and error checking
    input_string = input(choice)
    while len(input_string) == 0:  # Using the while loop to check if the user input blank
        print("Input can not be blank")  # Display the error message
        input_string = input(choice)
    return input_string.title()

def count_number_year(choice):  # This function is used for checking the new song year while user entering year
    valid = False  # Make the variable as False
    while not valid:
        try:
            input_number = int(input(choice))  # Connect it with integer user input
            if input_number < 0:
                print("Number must be >= 0")  # Remind the user to enter the valid number
            else:
                return input_number  # Ask for the user input to rewrite the input_number
        except ValueError:  # Except the error
            print("Invalid input；enter a valid number")


def save_to_file(all_songs):  # This function is used to write the song list to the csv file
    final_save = open("songs.csv", 'w')
    for i in range(len(all_songs)):  # Using the for loop and declare variable
        if i != 0:
            print("\n", end="", file=final_save)
            for j in range(len(all_songs[i])):  # Constant k represent the range of the list
                final_save.write(all_songs[i][j])  # Write the arranged data into the csv file
                if j != 3:
                    print(",", end="", file=final_save)
    final_save.close()  # Close the csv file

if __name__ == '__main__':
    main()