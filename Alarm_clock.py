import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm time set for {alarm_time}")
    sound_file = "Alarm_sound.mp3"
    is_running = True

    pygame.mixer.init()

    alarm_time_dt = datetime.datetime.strptime(alarm_time, "%H:%M:%S")

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current time :", current_time)

        # convert current_time string → datetime
        current_time_dt = datetime.datetime.strptime(current_time, "%H:%M:%S")

        if current_time_dt >= alarm_time_dt:
            print("     Wake Up buddy 😊       :")

            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            start = time.time()
            while pygame.mixer.music.get_busy():
                if time.time() - start >= 30:  
                    pygame.mixer.music.stop()
                    break
                time.sleep(1)

            is_running = False

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
