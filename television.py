class Television:
    """
    Television class that has 4 attributes:
    power, mute, volume, and channel
    """
    
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self, status: bool = False, muted: bool = False, volume: int = min_volume, channel: int = min_channel):

        """
        Intializes a Television object.
        
        Args:
            status (bool): Power state of the Tv; default is OFF (True = ON, False = OFF)
            muted (bool): Mute state of the Tv; default is UNMUTED (True = MUTED, False = UNMUTED)
            volume (int): Intial volume level; default is MIN_VOLUME
            channel (int): Intial channel; default value is is MIN_CHANNEL
        """
        if volume > Television.max_volume or volume < Television_min_volume:
            raise ValueError("Volume out of range")
        if channel > Television.max_channel or channel < Television_min_channel:
            raise ValueError("Volume out of range")
        
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self) -> None:
        """
        Toggle power of the Tv between ON/OFF (TRUE/FALSE)
        """
        self.__status = not self.__status 

    def mute(self) -> None:
        """
        Toggle the mute state of Tv between MUTED/UNMUTED (TRUE/FALSE)
        """
        if self.__status:
            self.__muted = not self.__muted  

    def channel_up(self) -> None:
        
        """
        Increment channel by 1
        Sets channel to MIN_CHANNEL if channel reaches MAX_CHANNEL
        """
        if self.__status:
            if self.__channel == Television.max_channel:
                self.__channel = Television.min_channel
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrement channel by 1
        Sets channel to MAX_CHANNEL if channel reaches MIN_CHANNEL
        """
        if self.__status:
            if self.__channel == Television.min_channel:
                self.__channel = Television.max_channel
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        
        """
        Increment volume by 1
        Cannot exceed MAX_VOLUME
        """
        
        if self.__status:
            if self.__muted:
                self.__muted = not self.__muted
                
            if self.__volume < Television.max_volume:
                self.__volume += 1

    def volume_down(self) -> None:
        
        """
        Decrement volume by 1
        Cannot exceed MIN_VOLUME
        """
        if self.__status: 
            if self.__muted:
                self.__muted = not self.__muted

            if self.__volume > Television.min_volume:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns formatted string of the power, channel, and volume
        of the Tv
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
