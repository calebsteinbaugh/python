import pytest
from television import Television


class TestTelevision:

    def test_init_defaults(self):
        tv = Television()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        tv = Television()
        tv.power()
        assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    def test_mute(self):
        tv = Television()
        tv.mute()
        assert tv._Television__muted is True

    def test_channel_up(self):
        tv = Television(channel=0)
        tv.channel_up()
        assert str(tv) == "Power = False, Channel = 1, Volume = 0"

    def test_channel_down(self):
        tv = Television(channel=1)
        tv.channel_down()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_channel_up_wrap(self):
        tv = Television(channel=Television.max_channel)
        tv.channel_up()
        assert str(tv) == f"Power = False, Channel = {Television.min_channel}, Volume = 0"

    def test_channel_down_wrap(self):
        tv = Television(channel=Television.min_channel)
        tv.channel_down()
        assert str(tv) == f"Power = False, Channel = {Television.max_channel}, Volume = 0"

    def test_volume_up(self):
        tv = Television(volume=0)
        tv.volume_up()
        assert str(tv) == "Power = False, Channel = 0, Volume = 1"

    def test_volume_down(self):
        tv = Television(volume=1)
        tv.volume_down()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    def test_volume_up_stops_at_max(self):
        tv = Television(volume=Television.max_volume)
        tv.volume_up()
        assert str(tv) == f"Power = False, Channel = 0, Volume = {Television.max_volume}"

    def test_volume_down_stops_at_min(self):
        tv = Television(volume=Television.min_volume)
        tv.volume_down()
        assert str(tv) == f"Power = False, Channel = 0, Volume = {Television.min_volume}"

    def test_str(self):
        tv = Television(status=True, muted=False, volume=1, channel=2)
        assert str(tv) == "Power = True, Channel = 2, Volume = 1"

    def test_volume_validation_above_max(self):
        with pytest.raises(ValueError, match="Volume out of range"):
            Television(volume=Television.max_volume + 1)

    def test_volume_validation_below_min(self):
        with pytest.raises(ValueError, match="Volume out of range"):
            Television(volume=Television.min_volume - 1)

    def test_channel_validation_above_max(self):
        with pytest.raises(ValueError, match="Volume out of range"):
            Television(channel=Television.max_channel + 1)

    def test_channel_validation_below_min(self):
        with pytest.raises(ValueError, match="Volume out of range"):
            Television(channel=Television.min_channel - 1)

    def test_valid_volume_at_boundaries(self):
        tv_min = Television(volume=Television.min_volume)
        assert tv_min._Television__volume == Television.min_volume
        
        tv_max = Television(volume=Television.max_volume)
        assert tv_max._Television__volume == Television.max_volume

    def test_valid_channel_at_boundaries(self):
        tv_min = Television(channel=Television.min_channel)
        assert tv_min._Television__channel == Television.min_channel
        
        tv_max = Television(channel=Television.max_channel)
        assert tv_max._Television__channel == Television.max_channel
