'''
Type hinting notes!

local variables
'var_name: type = value'

On parameters 
def Function(param1: type = value, param2: type = value) -> type:


'''


class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__ (self):
        '''
        
        
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Sets the status of the TV to the opposite bool value
        if status is True -> set to False
        and if is False -> set to True

        :return: None
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False



    def mute(self) -> None:
        '''
        mutes TV, when str func is called, volume prints as 0

        :return: None
        '''
        if self.__status == False: #making sure the TV is powered ON
            return
        

        if self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False



    def channel_up(self) -> None:
        '''
        increase channel by one, if channel is on the MAX channel then switch to the MINIMUM channel

        :return: None
        '''
        if self.__status == False: #making sure the TV is powered ON
            return
    

        if self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        else:
            self.__channel += 1

        

    def channel_down(self) -> None:
        '''
        decreases channel by one, if channel is on the MINIMUM channel then switch to the MAX channel

        :return: None
        '''
        if self.__status == False: #making sure the TV is powered ON
            return

        if self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        else:
            self.__channel -= 1


    def volume_up(self) -> None:
        '''
        increases the volume of TV by one, if TV is on MAX volume then no change

        :return: None
        '''
        if self.__status == False: #making sure the TV is powered ON
            return

        self.__muted = False
        if self.__volume == Television.MAX_VOLUME:
            pass
        else:
            self.__volume += 1



    def volume_down(self) -> None:
        '''
        decreases the volume of the TV by one, if TV in on the MINIMUM volume then no change

        :return: None
        '''
        if self.__status == False: #making sure the TV is powered ON
            return

        self.__muted = False
        if self.__volume == Television.MIN_VOLUME:
            pass
        else:
            self.__volume -= 1



    def __str__(self) -> None:
        '''
        :return: status of power, channel, and volume
        if TV is muted, then volume is 0

        :return: None
        '''
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'






if __name__ == "__main__":
    tv1 = Television()
    tv1.power()
    tv1.volume_up()
    tv1.mute()

    print(tv1)
    pass