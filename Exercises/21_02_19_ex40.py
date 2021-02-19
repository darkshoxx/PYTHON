class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
mayryo_lyrics = ["Do the Mario!",
                     "Swing your arms",
                     "from side to side",
                     "Come on it's time to go!"]

do_the_mario = Song(mayryo_lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

do_the_mario.sing_me_a_song()