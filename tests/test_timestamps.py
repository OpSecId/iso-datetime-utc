from iso_datetime_utc import timestamp


def test_timestamps():
    assert timestamp.now()
    assert timestamp.past()
    assert timestamp.future()
