import threading
import time

def walk(location):
    time.sleep(4)
    print(f"Walking some times to relieve stress by the {location}")

def water_plants():
    time.sleep(1)
    print("Water the flower and fruit plants")

def cooking():
    time.sleep(3)
    print("Cooking for dinner")

def bathing():
    time.sleep(2)
    print("Baths in the tub")

def start_code():
    print("Threading starts...")
    ch1 = threading.Thread(target=walk,args=("Sea Beach,"))
    ch1.start()
    ch2 = threading.Thread(target=water_plants)
    ch2.start()
    ch3 = threading.Thread(target=cooking)
    ch3.start()
    ch4 = threading.Thread(target=bathing)
    ch4.start()

    ch1.join()
    ch2.join()
    ch3.join()
    ch4.join()

    print("Threading ends...")

if __name__ == '__main__':
    start_code()