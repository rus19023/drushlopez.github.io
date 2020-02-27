from collections import deque


class Song:

    def __init__(self):
        self.title = "title"
        self.artist = "artist"

    def prompt(self):
        self.title = input("Enter song title: ")
        self.artist = input("Enter song artist/group: ")

    def display(self):
        print("Song: {} by {}".format(self.title, self.artist))


def process_choice(choice):
    playlist = deque()
    new_song = Song()
    song_info = new_song.prompt()
    while choice > 0 and choice < 5:
        if choice == 1:
            playlist.append(new_song.display())
        elif choice == 2:
            playlist.appendleft(new_song.display())
        elif choice == 3:
            if len(playlist) == 0:
                print("The playlist is currently empty.")
            else:
                next_song = playlist.popleft()
                print("Playing song: {}", next_song)
        elif choice == 4:
            break


def main():
    choice = 1
    while choice > 0 and choice < 5:
        print("Options:")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        menu_choice = int(input("Enter selection: "))
        process_choice(menu_choice)



if __name__ == "__main__":
    main()

