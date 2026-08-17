# Smartstick

A prototype of a smart cane using ultrasonic sensing to detect obstacles and alert users via vibration, designed to assist visually impaired individuals in navigating through public spaces.

## Design and features
-projector: emits a flashlight to indicate the presence of an obstacle, creates a visible circular warning zone noticeable by nearby individuals

-sensor: triggers vibration to the handle when an obstacle reaches the warning zone

-button (located on top of handle): double tapping activates the projector, while long pressing makes it flicker and emit a beeping sound, signaling for help from others

-foldable stick: increases convenience, allowing easy storage

## Technology behind design
-Raspberry Pi ultrasonic motion detector: a DIY security / automation device created by connecting a sensor to a Raspberry Pi's GPIO pins

-sensor is programmed to detect movements of objects within the projected zone by measuring distance changes overtime, sending vibrations to the handle of the stick
