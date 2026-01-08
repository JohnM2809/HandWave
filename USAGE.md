# HandWave Usage Guide

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Webcam
- Working mouse/keyboard (for initial setup)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/JohnM2809/HandWave.git
   cd HandWave
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the GUI application**
   ```bash
   python handwave_gui.py
   ```

## Using the GUI

### Starting Hand Tracking
1. Click the green "▶ Start Tracking" button
2. Allow camera access if prompted
3. Your webcam will activate and show the video feed
4. Position your hand in front of the camera

### Hand Positioning Tips
- **Distance**: Keep your hand 1-2 feet from the camera
- **Lighting**: Ensure good lighting for better hand detection
- **Background**: A plain background works best
- **Hand visibility**: Keep your entire hand visible in the frame

### Gestures

#### Moving the Cursor
- **Gesture**: Point with your index finger (finger #8)
- **Action**: The cursor follows your index finger tip
- **Tip**: Move smoothly for better control

#### Clicking
- **Gesture**: Bring your thumb and index finger close together
- **Action**: Performs a mouse click
- **Distance threshold**: Less than 50 pixels
- **Debounce**: 0.5 seconds between clicks
- **Tip**: Make a pinching motion

#### Scrolling Down
- **Gesture**: Raise your middle finger close to your index position
- **Action**: Scrolls down the page
- **Distance threshold**: Less than 40 pixels
- **Debounce**: 0.3 seconds between scrolls
- **Tip**: Hold the gesture to scroll continuously

#### Scrolling Up
- **Gesture**: Raise your ring finger close to your index position
- **Action**: Scrolls up the page
- **Distance threshold**: Less than 50 pixels
- **Debounce**: 0.3 seconds between scrolls
- **Tip**: Hold the gesture to scroll continuously

### GUI Features

#### Controls Panel
- **Start Tracking**: Begins hand detection and gesture control
- **Stop Tracking**: Stops gesture control and releases camera

#### Status Indicator
- **● Running** (green): Hand tracking is active
- **● Stopped** (red): Hand tracking is stopped

#### Statistics
- **Clicks**: Total number of click gestures performed
- **Scroll Up**: Total number of upward scroll gestures
- **Scroll Down**: Total number of downward scroll gestures

#### Gesture Settings
- **Enable Click Gesture**: Toggle click detection on/off
- **Enable Scroll Gesture**: Toggle scroll detection on/off
- **Use case**: Disable gestures when you only need cursor movement

### Troubleshooting

#### Camera not working
- Check if another application is using the webcam
- Verify camera permissions
- Try restarting the application

#### Hand not detected
- Improve lighting conditions
- Ensure hand is fully visible in frame
- Remove any hand coverings (gloves, etc.)
- Try moving closer or farther from camera

#### Gestures not responding
- Check if gestures are enabled in settings
- Verify hand landmarks are being drawn (colored circles on fingers)
- Adjust hand position to meet distance thresholds
- Ensure movements are deliberate and clear

#### Performance issues
- Close other applications to free up resources
- Reduce other camera applications
- Check CPU usage

### Performance Notes

The application uses:
- **Threading**: Video processing runs in a background thread
- **Debouncing**: Prevents accidental repeated gestures
- **Optimized frame processing**: Efficient color space conversion and resizing
- **Real-time tracking**: MediaPipe's efficient hand landmark detection

### Tips for Best Experience

1. **Start with cursor movement**: Get comfortable moving the cursor before trying other gestures
2. **Practice gestures individually**: Enable only one gesture type while learning
3. **Use deliberate motions**: Quick, clear gestures work better than slow drifts
4. **Check statistics**: Use the counters to verify gestures are being detected
5. **Adjust lighting**: Good lighting dramatically improves detection accuracy
6. **Take breaks**: Hand gesture control can be tiring - take regular breaks

### Advanced Usage

#### Running the Original CLI Version
For minimal overhead or headless environments:
```bash
python handwave.py
```

Note: The CLI version opens an OpenCV window and has no GUI controls.

#### Customizing Gesture Thresholds
To adjust sensitivity, edit `handwave_gui.py`:
- Click threshold: Line ~334 (default: 50 pixels)
- Scroll threshold: Lines ~317, ~343 (default: 40-50 pixels)
- Debounce timing: Lines ~319, ~337, ~349 (default: 0.3-0.5 seconds)

#### Modifying Colors
The GUI uses the Catppuccin color scheme. To customize:
- Background: `#1e1e2e`
- Panels: `#313244`
- Accent: `#89dceb`
- Success: `#a6e3a1`
- Error: `#f38ba8`

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

See LICENSE file for details.
