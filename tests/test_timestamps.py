from utc_time import timestamp


def test_timestamps():
    assert timestamp.now()
    assert timestamp.past()
    assert timestamp.future()
