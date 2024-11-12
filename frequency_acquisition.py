import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

class FrequencyLogger:
    def __init__(self, data_pin=23, clock_pin=24, filename="frequency_log.csv"):
        self.data_pin = data_pin
        self.clock_pin = clock_pin
        self.filename = filename
        
        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(data_pin, GPIO.IN)
        GPIO.setup(clock_pin, GPIO.IN)
        
    def initialize_file(self):
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            with open(self.filename, "a") as file:
                file.write("Time,Frequency(Hz)\n")
    
    def read_frequency(self):
        """Read 32-bit frequency value from Arduino"""
        # Wait for clock to go low (start of transmission)
        while GPIO.input(self.clock_pin) == 1:
            pass
            
        value = 0
        # Read 32 bits
        for i in range(32):
            # Wait for clock to go high
            while GPIO.input(self.clock_pin) == 0:
                pass
            
            # Read data bit
            if GPIO.input(self.data_pin):
                value |= 1 << (31 - i)
                
            # Wait for clock to go low
            while GPIO.input(self.clock_pin) == 1:
                pass
                
        # Convert back to frequency (divide by 10 to restore decimal place)
        return value / 10.0
        
    def log_data(self, frequency):
        try:
            with open(self.filename, "a") as file:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
                file.write(f"{timestamp},{frequency:.3f}\n")
                file.flush()
                print(f"Logged: {timestamp}: {frequency:.3f} Hz")
        except Exception as e:
            print(f"Error logging: {e}")
            
    def run(self):
        print("Starting Digital Frequency Logger")
        print(f"Data Pin: GPIO{self.data_pin}")
        print(f"Clock Pin: GPIO{self.clock_pin}")
        print(f"Logging to: {self.filename}")
        print("Press Ctrl+C to stop...")
        
        self.initialize_file()
        
        try:
            while True:
                frequency = self.read_frequency()
                self.log_data(frequency)
                time.sleep(0.01)  # 10ms delay for 0.01s precision
                
        except KeyboardInterrupt:
            print("\nStopping logger...")
        except Exception as e:
            print(f"Error in main loop: {e}")
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
    try:
        logger = FrequencyLogger()
        logger.run()
    except Exception as e:
        print(f"Error: {e}")
        GPIO.cleanup()
