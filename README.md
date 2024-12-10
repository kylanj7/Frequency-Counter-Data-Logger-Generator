# Digital Frequency Logger

A distributed system for measuring and logging frequencies using Arduino, Raspberry Pi, and a PicoW signal generator. The system provides accurate frequency measurements with real-time display and data logging capabilities.

## Components

### 1. Raspberry Pi Logger (frequency_logger.py)
- Reads frequency data from Arduino
- Logs measurements with timestamps
- Saves data to CSV file
- Uses GPIO for communication
- Error handling and cleanup

### 2. Arduino Frequency Counter (frequency_counter.ino)
- Measures input signal frequency
- LCD display interface
- Serial communication with Raspberry Pi
- 32-bit data transmission protocol
- Real-time updates

### 3. PicoW Signal Generator (signal_generator.py)
- Generates test clock signal
- PWM-based frequency output
- Configurable frequency/duty cycle
- Ground pin configuration

## Hardware Requirements

- Raspberry Pi (any model)
- Arduino (with LCD shield)
- Raspberry Pi Pico W
- LCD Display (16x2)
- Connecting wires

## Pin Connections

### Raspberry Pi
- Data: GPIO23
- Clock: GPIO24

### Arduino
- Pulse Input: Pin 8
- Data Out: Pin 2
- Clock Out: Pin 3
- LCD Pins: 4, 6, 10, 11, 12, 13

### PicoW
- Clock Out: GPIO0
- Ground: GPIO1

## Setup

1. Connect hardware according to pin configuration
2. Upload Arduino sketch
3. Run Raspberry Pi logger:
```bash
python frequency_logger.py
```
4. Deploy PicoW code for signal generation

## Data Logging

- CSV format with timestamp and frequency
- Default filename: `frequency_log.csv`
- 0.01s measurement precision
- Auto-creates log file if not present

## Features

- Real-time frequency display on LCD
- Continuous data logging
- Timestamp precision to milliseconds
- Error handling and recovery
- GPIO cleanup on exit
- Configurable pins and settings

## Limitations

- Maximum frequency determined by Arduino pulseIn()
- 0.1s minimum sampling interval
- Single channel measurement

## Error Handling

- File I/O error recovery
- GPIO cleanup on exit
- Communication error detection
- Graceful shutdown on Ctrl+C

## Contributing

Feel free to submit issues and enhancement requests!

## License

[Specify your license here]
