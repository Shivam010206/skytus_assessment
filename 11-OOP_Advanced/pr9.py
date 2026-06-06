class MusicPlayer:
    def play(self):
        print("Playing music")


class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")


music = Spotify()

music.play()