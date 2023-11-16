from television import Television
# from pytest import *
import pytest



#use:
#pytest test_name.py
#python3 -m pytest

class Test:
    def setup_method(self):
        self.tv1 = Television()
        # self.tv2 = Television()

    
    def teardown_method(self):
        del self.tv1
        # del self.tv2


    def test_init(self):
        #TV is created
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

    def test_power(self):
        #TV is on
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'

        #TV is off
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

    def test_mute(self):
        #TV is on, volume increased, and muted
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute() #MUTED
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'

        #TV is on, and unmuted
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [1]'

        #TV is off, and muted
        self.tv1.mute()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        #TV is off and unmuted
        self.tv1.power()
        self.tv1.mute()
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [1]'


    def test_channel_up(self):
        #TV is off, and channel increased
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        #TV is on, and channel increased
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [1], Volume = [0]'        

        #TV is on, and increased past the maximum volume
        self.tv1.channel_up() #changed to channel 2
        self.tv1.channel_up() #channel 3
        self.tv1.channel_up() #channel 0
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'


    def test_channel_down(self):
        #TV is off, channel decreased
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        #TV is on, channel decreased past minimum
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = [True], Channel = [3], Volume = [0]'


    def test_volume_up(self):
        #TV is off, volume increased
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        #TV is on, volume increased
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [1]'

        #TV is on, muted, volume increased
        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [2]'

        #TV is on, and one has increased the volume past the maximum value
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [2]'


    def test_volume_down(self):
        #TV is off, volume decreased
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = [False], Channel = [0], Volume = [0]'

        #TV is on, and one has decreased the volume past the minimum value
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [1]'

        #TV is on, muted, and volume decreased
        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'

        #TV is on, and one has decreased the volume past the minimum value
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = [True], Channel = [0], Volume = [0]'