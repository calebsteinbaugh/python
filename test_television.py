import pytest
from television import Television


class TestTelevision:


    def test_init_default_values(self):
        tv = Television()
        assert tv._Television__status is False
        assert tv._Television__muted is False
        assert tv._Television__volume == Television.min_volume
        assert tv._Television__channel == Television.min_channel

    def test_init_custom_values(self):
        tv = Television(True, True, 1, 2)
        assert tv._Television__status is True
        assert tv._Television__muted is True
        assert tv._Television__volume == 1
        assert tv._Television__channel == 2


    def test_power_turns_tv_on(self):
        tv = Television()
        tv.power()
        assert tv._Television__status is True

    def test_power_turns_tv_off(self):
        tv = Television()
        tv.power()
        tv.power()
        assert tv._Television__status is False


    def test_mute_when_tv_on_after_volume_up(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()

        assert tv._Television__status is True
        assert tv._Television__volume == 1
        assert tv._Television__muted is True

    def test_mute_then_unmute_when_tv_on(self):
        tv = Television()
        tv.power()
        tv.mute()
        tv.mute()

        assert tv._Television__status is True
        assert tv._Television__muted is False

    def test_mute_when_tv_off(self):
        tv = Television()
        tv.mute()

        assert tv._Television__status is False
        assert tv._Television__muted is True

    def test_mute_then_unmute_when_tv_off(self):
        tv = Television()
        tv.mute()
        tv.mute()

        assert tv._Television__status is False
        assert tv._Television__muted is False


    def test_channel_up_when_tv_off(self):
        tv = Television()
        tv.channel_up()

        assert tv._Television__status is False
        assert tv._Television__channel == 1

    def test_channel_up_when_tv_on(self):
        tv = Television()
        tv.power()
        tv.channel_up()

        assert tv._Television__status is True
        assert tv._Television__channel == 1

    def test_channel_up_wraps_past_max(self):
        tv = Television(channel=Television.max_channel)
        tv.power()
        tv.channel_up()

        assert tv._Television__status is True
        assert tv._Television__channel == Television.min_channel


    def test_channel_down_when_tv_is_off(self):
        tv = Television(channel=2)
        tv.channel_down()

        assert tv._Television__status is False
        assert tv._Television__channel == 1

    def test_channel_wraps_min_when_tv_on(self):
        tv = Television(channel=Television.min_channel)
        tv.power()
        tv.channel_down()

        assert tv._Television__status is True
        assert tv._Television__channel == Television.max_channel


    def test_volume_up_when_tv_off(self):
        tv = Television()
        tv.volume_up()

        assert tv._Television__status is False
        assert tv._Television__volume == 1

    def test_volume_up_when_tv_on(self):
        tv = Television()
        tv.power()
        tv.volume_up()

        assert tv._Television__status is True
        assert tv._Television__volume == 1

    def test_volume_up_when_tv_on_and_muted(self):
        tv = Television()
        tv.power()
        tv.mute()
        tv.volume_up()

        assert tv._Television__status is True
        assert tv._Television__muted is True
        assert tv._Television__volume == 1

    def test_volume_up_past_max(self):
        tv = Television(volume=Television.max_volume)
        tv.power()
        tv.volume_up()

        assert tv._Television__status is True
        assert tv._Television__volume == Television.max_volume


    def test_volume_down_when_tv_off(self):
        tv = Television(volume=1)
        tv.volume_down()

        assert tv._Television__status is False
        assert tv._Television__volume == 0

    def test_volume_down_when_tv_on(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.volume_down()

        assert tv._Television__status is True
        assert tv._Television__volume == 1

    def test_volume_down_when_tv_on_and_muted(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        tv.volume_down()

        assert tv._Television__status is True
        assert tv._Television__muted is True
        assert tv._Television__volume == 0
