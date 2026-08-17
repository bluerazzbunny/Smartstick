import machine
import time

# Configure pins
LIGHT_PIN = 7
BUZZER_PIN = 3

light = machine.Pin(LIGHT_PIN, machine.Pin.OUT)
buzzer = machine.Pin(BUZZER_PIN, machine.Pin.OUT)

# Internal state
_emergency_running = False

def run_emergency_logic():
    """Emergency mode: fast synchronized blinking of the light and buzzer beeping."""
    global _emergency_running
    _emergency_running = True
    print("WARNING: [Emergency mode] is now running.")

    while _emergency_running:
        light.value(1)
        buzzer.value(1)
        time.sleep_ms(100)

        light.value(0)
        buzzer.value(0)
        time.sleep_ms(100)

def stop_emergency():
    """Stop emergency mode: ensure the light and buzzer are fully turned off."""
    global _emergency_running
    _emergency_running = False
    light.value(0)
    buzzer.value(0)
