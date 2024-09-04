import numpy as np
import pytest
from mistercar_screenshooter import ScreenCapture


@pytest.fixture
def screen_capture():
    return ScreenCapture()


def test_capture_screen(screen_capture):
    img = screen_capture.capture_screen()
    assert isinstance(img, np.ndarray)
    assert img.ndim == 3
    assert img.shape[2] == 3  # RGB


def test_capture_region(screen_capture):
    region = (0, 0, 100, 100)
    img = screen_capture.capture_region(region)
    assert isinstance(img, np.ndarray)
    assert img.shape[:2] == (100, 100)


def test_list_monitors(screen_capture):
    monitors = screen_capture.list_monitors()
    assert isinstance(monitors, list)
    assert len(monitors) > 0


def test_capture_monitor(screen_capture):
    monitors = screen_capture.list_monitors()
    if len(monitors) > 0:
        img = screen_capture.capture_monitor(0)
        assert isinstance(img, np.ndarray)
        assert img.ndim == 3
