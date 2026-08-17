import machine
from machine import Pin
import time

# Import feature modules
import sensor
import emergency

# Initialize button (GPIO 10)
button = Pin(10, Pin.IN, Pin.PULL_DOWN)
buzzer = machine.Pin(3, machine.Pin.OUT)

# Mode definitions:
# 0 = Main Menu (Idle), 1 = Sensor Mode, 2 = Emergency Mode
current_mode = 0

# Button timing parameters
LONG_PRESS_TIME = 1.0
DOUBLE_CLICK_GAP = 0.4

def beep(times=1):
    """Buzzer prompt sound: default beeps 1 time (can specify 2 times)."""
    for _ in range(times):
        buzzer.value(1)
        time.sleep_ms(80)
        buzzer.value(0)
        time.sleep_ms(80)

def change_mode(new_mode):
    """Safely switch modes, shutting down outputs from the previous mode first."""
    global current_mode
    print(f"\n🔄 Mode change: from {current_mode} to {new_mode}")

    # Turn off all old mode hardware outputs
    sensor.stop_sensor()
    emergency.stop_emergency()

    current_mode = new_mode

def scan_button():
    """Scan the button and return the detected button action."""
    if button.value() == 1:
        press_start = time.ticks_ms()
        while button.value() == 1:
            time.sleep_ms(10)

        press_duration = time.ticks_diff(time.ticks_ms(), press_start) / 1000.0

        # 1) Check long press
        if press_duration >= LONG_PRESS_TIME:
            return "long_press"

        # 2) Check single click or double click
        else:
            is_double_click = False
            wait_start = time.ticks_ms()
            while time.ticks_diff(time.ticks_ms(), wait_start) < (DOUBLE_CLICK_GAP * 1000):
                if button.value() == 1:
                    is_double_click = True
                    while button.value() == 1:
                        time.sleep_ms(10)
                    break
                time.sleep_ms(10)

            return "double_click" if is_double_click else "single_click"

    return None

# --- Main program loop ---
print("System starting: currently in Main mode (Idle)...")

while True:
    # 1) Continuously detect button actions
    action = scan_button()

    if action == "single_click":
        # Single click -> switch to sensor mode
        beep(2)
        change_mode(0)
        print("Returned to main mode; stopped all sensing.")

    elif action == "double_click":
        # Double click -> return to main mode (Idle)
        beep(1)
        change_mode(1)

    elif action == "long_press":
        # Long press -> switch to emergency mode
        change_mode(2)

    # 2) Run logic based on the current mode
    if current_mode == 1:
        sensor.run_sensor_logic()
        time.sleep_ms(200)  # Reduce sampling frequency so the button is easier to trigger

    elif current_mode == 2:
        emergency.run_emergency_logic()

    else:
        # Main mode (Idle): do nothing, just wait for the button
        time.sleep_ms(50)
