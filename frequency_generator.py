from machine import Pin, PWM
from time import sleep

# Set up clock output pin
clock_out = PWM(Pin(0))  # GPIO0 as clock output
clock_out.freq(10000)     # 1kHz frequency
clock_out.duty_u16(32767)  # 50% duty cycle for clean square wave

# Set up ground pin
gnd_pin = Pin(1, Pin.OUT)  # GPIO1 as ground
gnd_pin.value(0)  # Set to low (ground)

# Keep program running
while True:
    sleep(0.1)  # Small sleep to prevent CPU hogging