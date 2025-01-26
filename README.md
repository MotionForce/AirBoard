# AirBoard
A keyboard without the keys. Or the board.

---

## What is AirBoard?
AirBoard is a virtual keyboard that uses the webcam to track the user's hands. The hands' position and depth are then used to detect which key should be pressed.

## How does it work?
AirBoard was designed in two main parts. Firstly, the back-end was written in Python. Support for sample collection, hand tracking and key press simulation was implemented. The hand tracking is done using a MediaPipe Hand Landmarker, a library and AI model created by Google. The hand tracking data was then combined with the height of the fingers to differentiate between key presses and rest position. The combination of these two elements is then fed to a key press simulator that uses PyAutoGui to emulate a keyboard. Secondly, the front-end was developed using SvelteKit and connected to the back-end using FastAPI.

## Installation
```[WIP]```

## Usage
```[WIP]```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.