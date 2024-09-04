import numpy as np
import pytest
from mistercar_screenshooter import ScreenCapture


@pytest.fixture
def screen_capture():
    return ScreenCapture()


def test_recorder(screen_capture):
    recorder = screen_capture.create_recorder("screen")
    recorder.start()
    frame = recorder.get_latest_frame()
    recorder.stop()
    assert isinstance(frame, np.ndarray)
    assert frame.ndim == 3
