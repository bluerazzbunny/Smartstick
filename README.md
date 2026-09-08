# Smartstick

A prototype of a smart cane using ultrasonic sensing to detect obstacles and alert users via vibration, designed to assist visually impaired individuals in navigating through public spaces.

## Introduction
For this project, we have observed that visually-impaired individuals face
significant challenges navigating crowded public spaces. Traditional tools
like the white cane offer limited functionality, primarily detecting obstacles
at ground level but they fail to account for dynamic environments, such as
moving crowds.

Moreover, everyday interactions can be challenging to the
visually-impaired. For instance, visually-impaired individuals cannot
determine if another individual is blocking their path. Consequently, if the
blind are in danger because of this, signaling for help from other
individuals becomes even more complicated, increasing their vulnerability.

Concerning the difficulties the visually-impaired face during their daily
lives, current technological innovations frequently rely on visual stimuli,
such as smartphone notifications that display texts or images. However,
these solutions fail to accommodate the needs of visually-impaired users.
The reliance on visual cues not only limits accessibility but also perpetuates
the challenges faced by the blind. It has always been a challenge for
inventors to create suitable products for the visually-impaired.

To address these pressing challenges, our project introduces an innovative
solution using Raspberry Pi ultrasonic motion detection technology. This
system is designed to assist visually-impaired individuals by detecting
moving obstacles well in advance, enhancing their spatial awareness and
improving their ability to navigate through crowded spaces safely,
overcoming the limitations of the traditional white cane and other similar
products in the market.

We believe that every individual should have the right to move freely,
without the constraints of their physical limitations. Our design aims to
transform the daily experience of visually-impaired individuals,
empowering them with greater confidence in navigating the world.

## Design and features
-projector: emits a flashlight to indicate the presence of an obstacle, creates a visible circular warning zone noticeable by nearby individuals

-sensor: triggers vibration to the handle when an obstacle reaches the warning zone

-button (located on top of handle): double tapping activates the projector, while long pressing makes it flicker and emit a beeping sound, signaling for help from others

-foldable stick: increases convenience, allowing easy storage

## Technology behind design
-Raspberry Pi ultrasonic motion detector: a DIY security / automation device created by connecting a sensor to a Raspberry Pi's GPIO pins

-HC-SR04 ultrasonic sensor programmed to detect movements of objects within the projected zone by measuring distance changes overtime, sending vibrations to the handle of the stick

-Vibration motor: located in the handle of the stick, vibrates when sensor detects obstacles

## Testing

Folding mechanism test:
This is a test for testing the folding mechanism on the stick to ensure
durability and reliability of the folding feature for daily storage and
portability. We will test this by opening and closing the stick 50 times, and
then checking it for looseness or failure.

Functionality of our design:
This is a test for testing whether our design works to ensure a consistent
performance of our product. The test will be conducted by letting 5
visually impaired users use the cane to navigate different situations and
determine whether our design worked. By analysing the end results of this
experiment, we will make changes to its design accordingly and conduct
this test again until a successful result is achieved.

Button test:
A test for the functionality of the buttons to verify tactile responsiveness
and reliability of control interfaces. Press each button repeatedly under
different conditions. For example, with gloves or wet hands. This makes
sure our controls could work and react with the user’s commands.

Warning zone test:
This test aims to evaluate the effectiveness of the warning zone
feature by verifying whether the vibration signal correctly alerts
the user when another individual enters the predetermined
proximity. Determine a range for the warning zone (1 metre, 2
metres etc.) for initial testing. The user holds the cane while
volunteers walk towards the cane from various angles and
distances. The distance at which the vibration activates will be
recorded. Multiple increments will be tested until the user
receives a signal.
