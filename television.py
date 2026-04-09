class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self, status: bool = False, muted: bool = False, volume: int = min_volume, channel: int = min_channel):

        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
        if volume > Television.max_volume or volume < Television_min_volume:
            raise ValueError("Volume out of range")
        if channel > Television.max_channel or channel < Television_min_channel:
            raise ValueError("Volume out of range")
        
    def power(self):
        self.__status = not self.__status 

    def mute(self):
        self.__muted = not self.__muted  

    def channel_up(self):
        if self.__channel == Television.max_channel:
            self.__channel = Television.min_channel
        else:
            self.__channel += 1

    def channel_down(self):
        if self.__channel == Television.min_channel:
            self.__channel = Television.max_channel
        else:
            self.__channel -= 1

    def volume_up(self):
        if self.__muted:
            self.__muted = not self.__muted
            
        if self.__volume < Television.max_volume:
            self.__volume += 1

    def volume_down(self):
        if self.__muted:
            self.__muted = not self.__muted     
        if self.__volume > Television.min_volume:
            self.__volume -= 1

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
