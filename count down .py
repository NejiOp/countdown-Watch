import time

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds
        self.paused = False
        self.start_time = None

    def start(self):
        self.start_time = time.monotonic()
        while True:
            if self.paused:
                time.sleep(0.1)
            else:
                elapsed_time = time.monotonic() - self.start_time
                remaining_time = self.seconds - elapsed_time
                if remaining_time <= 0:
                    print("Time's up!")
                    break
                else:
                    minutes, seconds = divmod(remaining_time, 60)
                    time_str = f"{int(minutes):02d}:{int(seconds):02d}"
                    print(time_str, end="\r")
                    time.sleep(0.1)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False
        self.start_time = time.monotonic() - (self.start_time - self.pause_time)

    def stop(self):
        self.seconds = 0

    def reset(self, seconds):
        self.seconds = seconds

timer = Timer(int(input("enter  time  : ")))  # 1 minute timer
timer.start()