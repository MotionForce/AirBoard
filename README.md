# AirBoard: Virtual Typing in Mid-Air

AirBoard is an innovative solution that transforms hand gestures into keystrokes, allowing you to type without the need for a physical keyboard or even a flat surface. Inspired by science-fiction movies and augmented reality technology, AirBoard offers a seamless and intuitive typing experience using only a webcam and a desktop app.

## 🧠 Inspiration

The concept for AirBoard is inspired by futuristic sci-fi depictions of holographic keyboards, along with the virtual keyboard used in Apple’s Vision Pro. The idea is to create a typing experience that feels like something from the future — no physical keyboard required.

## ⚙️ Problem Statement

Traditional keyboards can be limiting, particularly for individuals with physical disabilities or those who require more ergonomic solutions. There's a growing need for innovative, flexible, and accessible input methods. AirBoard addresses this challenge by using hand gestures to simulate typing in mid-air, offering a more efficient and accessible way to interact with digital devices.

## 💡 What it does

AirBoard allows you to type without needing a physical keyboard or a flat surface. With just a webcam pointed at your hands, and a desktop app to process the data, you can start typing seamlessly and intuitively. It's easy to set up, and no additional hardware is required beyond your webcam.

## 🛠️ How we built it

### Backend

- **Python & MediaPipe**: MediaPipe's Hand Landmarker tracks key hand landmarks (21 points per hand) in real-time, enabling precise gesture recognition.
- **Gesture Recognition**: Processes hand landmarks to recognize different typing gestures, interpreting finger height and movement as keystrokes.
- **Keystroke Simulation**: PyAutoGui simulates keystrokes based on recognized hand gestures.
- **WebSocket & FastAPI**: WebSocket ensures real-time, low-latency communication between the backend and frontend, enabling live data updates.

### Frontend

- **SvelteKit**: A modern framework used to create a dynamic and responsive UI that visualizes live video, hand data, and keystrokes.
- **Real-Time Updates**: The frontend uses WebSocket to provide instant data updates, with error handling and reconnection logic for a smooth experience.
- **User-Friendly Design**: The UI is designed for intuitive feedback and easy interaction, improving the overall virtual typing experience.

## 🚧 Challenges We Ran Into

We initially attempted to support touch typing, but training AI models with sample images didn’t give satisfactory results. The initial approach only predicted one character out of five correctly, so we had to refine our approach and focus on gesture recognition and tracking instead.

## 🏆 Accomplishments We're Proud Of

A major breakthrough was being able to type *mid-air*! After fine-tuning the detection height and limits of where keys would be recognized, we could allow users to type without needing a surface at all. By focusing purely on hand landmarks, independent of environmental data, this becomes possible.

## 📚 What We Learned

The importance of a varied dataset cannot be overstated. In order to train an AI model that accurately recognizes keypresses, the data must include a wide range of hand gestures, with some randomness to account for real-world variation. Without this, the model struggles to generalize its predictions.

## 🌟 Why AirBoard is Exceptional

- **Accessibility**: AirBoard makes digital interaction more inclusive, particularly for individuals with mobility challenges, by eliminating the need for physical keys.
- **Ergonomics**: AirBoard offers a more comfortable and natural typing posture, reducing the strain caused by traditional keyboards.
- **Innovation**: By combining cutting-edge hand tracking and gesture recognition technology, AirBoard represents a significant advancement in human-computer interaction and sets the stage for future innovations in virtual input methods.

## 🚀 What's Next for AirBoard

- **Augmented Reality Integration**: AirBoard could be integrated into AR products like smart glasses, allowing users to type seamlessly in augmented reality environments.
- **Increased Accessibility**: AirBoard can be used in various positions and on almost any surface, providing a versatile typing experience that goes beyond the limitations of traditional keyboards.

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/motionforce/airboard.git
   cd airboard
   ```
2. Install the required dependencies.
3. Launch the application.
