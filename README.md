# HandWave

Control your computer using just hand gestures.  
Built with **MediaPipe**, **OpenCV**, and **PyAutoGUI**.

## Features
- Cursor movement using index finger
- Click using thumb + index gesture
- Scroll up/down with ring and middle finger movement
- Real-time hand tracking with webcam
- **NEW:** Beautiful GUI with modern design
- Real-time gesture statistics tracking
- Enable/disable individual gestures
- Start/stop tracking with easy controls

## 🛠️ Tech Stack
- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Tkinter (GUI)
- Pillow (Image processing)

## 🚀 Getting Started

### Installation
```bash
pip install -r requirements.txt
```

### Running the Application

**With GUI (Recommended):**
```bash
python handwave_gui.py
```

**Original CLI Version:**
```bash
python handwave.py
```

Make sure your webcam is enabled.

## 🎨 GUI Features
- Modern dark theme interface
- Real-time video feed display
- Gesture statistics (clicks, scroll counts)
- Start/Stop controls
- Enable/disable specific gestures
- Visual status indicators
- Built-in gesture guide

## 📝 Gesture Guide
- 👆 **Index finger**: Move cursor
- 👌 **Thumb + Index**: Click
- 🖖 **Ring finger up**: Scroll up
- 🤚 **Middle finger**: Scroll down

## 📸 Screenshots

### Beautiful GUI Interface
![HandWave GUI](https://github.com/user-attachments/assets/6ce7f99f-3f3a-43b6-8bd6-b400d4bc172a)

The new GUI features:
- **Modern dark theme** with Catppuccin-inspired colors
- **Real-time video display** with hand landmark visualization
- **Interactive controls** for starting/stopping tracking
- **Live statistics** showing gesture counts
- **Configurable gestures** - enable/disable individual gestures
- **Visual status indicators** showing tracking state
- **Built-in gesture guide** for quick reference

## 📊 Comparison: CLI vs GUI

| Feature | Original (CLI) | New (GUI) |
|---------|---------------|-----------|
| Interface | OpenCV window | Modern Tkinter GUI |
| Controls | Keyboard only | Click buttons |
| Statistics | None | Real-time counters |
| Gesture Config | Code editing | Toggle switches |
| Status Display | None | Visual indicators |
| User Experience | Basic | Professional |

Made with ❤️ by John
