from collections import deque


class Song:

    def __init__(self):
        self.title = "title"
        self.artist = "artist"

    def prompt(self):
        self.title = input("Enter song title: ")
        self.artist = input("Enter song artist/group: ")
        print()

    def display(self):
        song_display = "{} by {}".format(self.title, self.artist)
        return song_display


def main():
    song = Song()
    playlist = deque()
    choice = 1
    while choice > 0 and choice < 5:
        print("Options:")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        choice = int(input("Enter selection: "))
        print()
        if choice == 4:
            print("Goodbye")
            break
        if choice == 1:
            song = Song()
            song.prompt()
            song.display()
            playlist.append(song.display())
        if choice == 2:
            song = Song()
            song.prompt()
            song.display()
            playlist.appendleft(song.display())
        elif choice == 3:
            if len(playlist) == 0:
                print("The playlist is currently empty.")
                print()
            else:
                next_song = playlist.popleft()
                print("Playing song: ", next_song)
                print()


if __name__ == "__main__":
    main()
