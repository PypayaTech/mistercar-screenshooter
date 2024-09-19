from mistercar_screenshooter import ScreenCapture
import cv2
import time
import platform


def main():
    # Create a ScreenCapture instance
    sc = ScreenCapture()

    # 1. Capture the entire screen
    print("Capturing entire screen...")
    screen = sc.capture_screen()
    cv2.imwrite("full_screen.png", cv2.cvtColor(screen, cv2.COLOR_RGB2BGR))
    time.sleep(2)

    # 2. Capture a specific region
    print("Capturing specific region...")
    region = sc.capture_region((100, 100, 500, 500))
    cv2.imwrite("region.png", cv2.cvtColor(region, cv2.COLOR_RGB2BGR))
    time.sleep(2)

    # 3. Capture a specific window (Windows only)
    if platform.system().lower() == "windows":
        try:
            print("Capturing specific window (Windows only)...")
            window = sc.capture_window("*Untitled - Notepad")
            cv2.imwrite("window.png", window)
        except Exception as e:
            print(f"Failed to capture window: {str(e)}")
    else:
        print("Window capture is not supported on this platform.")
    time.sleep(2)

    # 4. List and capture from multiple monitors
    print("Listing and capturing from multiple monitors...")
    monitors = sc.list_monitors()
    for i, monitor in enumerate(monitors):
        print(f"Capturing monitor {i}: {monitor}")
        img = sc.capture_monitor(i)
        cv2.imwrite(f"monitor_{i}.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    time.sleep(2)

    # 5. Record a video
    print("Recording a 5-second video...")
    sc.record_video("output.mp4", duration=5, fps=60, capture_type="screen")
    time.sleep(2)

    # 6. Use the recorder for continuous capture
    print("Demonstrating continuous capture...")
    recorder = sc.create_recorder("screen")
    recorder.start()
    start_time = time.time()
    frame_count = 0
    while time.time() - start_time < 5:  # Record for 5 seconds
        frame = recorder.get_latest_frame()
        # In a real application, you might process or save the frame here
        frame_count += 1
    recorder.stop()
    print(f"Captured {frame_count} frames in 5 seconds (approx. {frame_count / 5:.2f} FPS)")


if __name__ == "__main__":
    main()
