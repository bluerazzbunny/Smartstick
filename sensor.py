import machine
import time
from machine import Pin, time_pulse_us

# ---- Pin setup (adjust to your board wiring if needed) ----
led_onboard = Pin(25, Pin.OUT)
light = Pin(7, Pin.OUT)
vibrate = Pin(11, Pin.OUT)

trig = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)

# ---- Ultrasonic settings ----
SPEED_CM_PER_US = 0.0343  # speed of sound in cm/us
MAX_ECHO_US = 30000       # timeout for echo pulse

def get_distance_cm():
    """Measure distance using an ultrasonic sensor. Returns distance in cm or None."""
    light.value(1)

    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)

    trig.value(0)

    duration = time_pulse_us(echo, 1, MAX_ECHO_US)
    if duration < 0:
        return None

    # Convert pulse duration to distance (cm)
    return (duration * SPEED_CM_PER_US) / 2

def run_sensor_logic():
    """Run one ultrasonic detection cycle."""
    dist = get_distance_cm()

    if dist is not None and dist < 100:
        led_onboard.value(1)
        vibrate.value(1)
        print("【Detection Mode】Object detected: {:.2f} cm".format(dist))
    else:
        led_onboard.value(0)
        vibrate.value(0)
        print("【Detection Mode】Out of range or no object detected")

def main():
    # Repeat continuously (comment out if you only want one cycle)
    while True:
        run_sensor_logic()
        time.sleep(0.2)

if __name__ == "__main__":
    main()
