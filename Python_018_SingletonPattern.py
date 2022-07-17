class MusicPlayer:

    instance = None
    init_flag = False

    def __init__(self):
        if MusicPlayer.init_flag:
            return

        MusicPlayer.init_flag = True
        print("Initiation")

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance # have to write this or program won't call constructor


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)
