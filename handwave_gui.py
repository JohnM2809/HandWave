import cv2
import mediapipe as mp
import pyautogui
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

class HandWaveGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HandWave - Gesture Control")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1e1e2e")
        
        # Initialize variables
        self.cap = None
        self.hand_detector = mp.solutions.hands.Hands()
        self.drawing_utils = mp.solutions.drawing_utils
        self.screen_width, self.screen_height = pyautogui.size()
        self.index_y = 0
        self.is_running = False
        self.thread = None
        
        # Gesture counters
        self.click_count = 0
        self.scroll_up_count = 0
        self.scroll_down_count = 0
        
        # Gesture enable flags
        self.click_enabled = tk.BooleanVar(value=True)
        self.scroll_enabled = tk.BooleanVar(value=True)
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Title frame
        title_frame = tk.Frame(self.root, bg="#1e1e2e")
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="✋ HandWave",
            font=("Helvetica", 32, "bold"),
            fg="#89dceb",
            bg="#1e1e2e"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Control your computer with hand gestures",
            font=("Helvetica", 12),
            fg="#cdd6f4",
            bg="#1e1e2e"
        )
        subtitle_label.pack()
        
        # Main container
        main_container = tk.Frame(self.root, bg="#1e1e2e")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left panel - Video feed
        left_panel = tk.Frame(main_container, bg="#313244", relief=tk.RAISED, bd=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        video_label = tk.Label(
            left_panel,
            text="Video Feed",
            font=("Helvetica", 14, "bold"),
            fg="#cdd6f4",
            bg="#313244"
        )
        video_label.pack(pady=10)
        
        self.video_canvas = tk.Label(left_panel, bg="#181825")
        self.video_canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Right panel - Controls and Stats
        right_panel = tk.Frame(main_container, bg="#313244", relief=tk.RAISED, bd=2, width=300)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        right_panel.pack_propagate(False)
        
        # Control buttons
        control_frame = tk.Frame(right_panel, bg="#313244")
        control_frame.pack(pady=20, padx=10, fill=tk.X)
        
        control_label = tk.Label(
            control_frame,
            text="Controls",
            font=("Helvetica", 14, "bold"),
            fg="#cdd6f4",
            bg="#313244"
        )
        control_label.pack(pady=(0, 10))
        
        self.start_button = tk.Button(
            control_frame,
            text="▶ Start Tracking",
            font=("Helvetica", 12, "bold"),
            bg="#a6e3a1",
            fg="#1e1e2e",
            activebackground="#94d994",
            command=self.start_tracking,
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=10
        )
        self.start_button.pack(fill=tk.X, pady=5)
        
        self.stop_button = tk.Button(
            control_frame,
            text="⏸ Stop Tracking",
            font=("Helvetica", 12, "bold"),
            bg="#f38ba8",
            fg="#1e1e2e",
            activebackground="#e37d98",
            command=self.stop_tracking,
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.stop_button.pack(fill=tk.X, pady=5)
        
        # Status indicator
        status_frame = tk.Frame(right_panel, bg="#313244")
        status_frame.pack(pady=20, padx=10, fill=tk.X)
        
        status_label = tk.Label(
            status_frame,
            text="Status",
            font=("Helvetica", 14, "bold"),
            fg="#cdd6f4",
            bg="#313244"
        )
        status_label.pack(pady=(0, 10))
        
        self.status_indicator = tk.Label(
            status_frame,
            text="● Stopped",
            font=("Helvetica", 11),
            fg="#f38ba8",
            bg="#313244"
        )
        self.status_indicator.pack()
        
        # Statistics
        stats_frame = tk.Frame(right_panel, bg="#313244")
        stats_frame.pack(pady=20, padx=10, fill=tk.X)
        
        stats_label = tk.Label(
            stats_frame,
            text="Statistics",
            font=("Helvetica", 14, "bold"),
            fg="#cdd6f4",
            bg="#313244"
        )
        stats_label.pack(pady=(0, 10))
        
        self.clicks_label = tk.Label(
            stats_frame,
            text="Clicks: 0",
            font=("Helvetica", 11),
            fg="#89dceb",
            bg="#313244"
        )
        self.clicks_label.pack(anchor=tk.W, pady=2)
        
        self.scroll_up_label = tk.Label(
            stats_frame,
            text="Scroll Up: 0",
            font=("Helvetica", 11),
            fg="#89dceb",
            bg="#313244"
        )
        self.scroll_up_label.pack(anchor=tk.W, pady=2)
        
        self.scroll_down_label = tk.Label(
            stats_frame,
            text="Scroll Down: 0",
            font=("Helvetica", 11),
            fg="#89dceb",
            bg="#313244"
        )
        self.scroll_down_label.pack(anchor=tk.W, pady=2)
        
        # Gesture settings
        settings_frame = tk.Frame(right_panel, bg="#313244")
        settings_frame.pack(pady=20, padx=10, fill=tk.X)
        
        settings_label = tk.Label(
            settings_frame,
            text="Gesture Settings",
            font=("Helvetica", 14, "bold"),
            fg="#cdd6f4",
            bg="#313244"
        )
        settings_label.pack(pady=(0, 10))
        
        click_check = tk.Checkbutton(
            settings_frame,
            text="Enable Click Gesture",
            variable=self.click_enabled,
            font=("Helvetica", 10),
            fg="#cdd6f4",
            bg="#313244",
            selectcolor="#1e1e2e",
            activebackground="#313244",
            activeforeground="#cdd6f4"
        )
        click_check.pack(anchor=tk.W, pady=5)
        
        scroll_check = tk.Checkbutton(
            settings_frame,
            text="Enable Scroll Gesture",
            variable=self.scroll_enabled,
            font=("Helvetica", 10),
            fg="#cdd6f4",
            bg="#313244",
            selectcolor="#1e1e2e",
            activebackground="#313244",
            activeforeground="#cdd6f4"
        )
        scroll_check.pack(anchor=tk.W, pady=5)
        
        # Instructions
        instructions_frame = tk.Frame(right_panel, bg="#313244")
        instructions_frame.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)
        
        instructions_label = tk.Label(
            instructions_frame,
            text="Gestures Guide",
            font=("Helvetica", 14, "bold"),
            fg="#cdd6f4",
            bg="#313244"
        )
        instructions_label.pack(pady=(0, 10))
        
        instructions_text = [
            "👆 Index finger: Move cursor",
            "👌 Thumb + Index: Click",
            "🖖 Ring finger up: Scroll up",
            "🤚 Middle finger: Scroll down"
        ]
        
        for instruction in instructions_text:
            inst_label = tk.Label(
                instructions_frame,
                text=instruction,
                font=("Helvetica", 9),
                fg="#a6adc8",
                bg="#313244",
                justify=tk.LEFT
            )
            inst_label.pack(anchor=tk.W, pady=3)
        
    def start_tracking(self):
        if not self.is_running:
            self.is_running = True
            self.cap = cv2.VideoCapture(0)
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_indicator.config(text="● Running", fg="#a6e3a1")
            
            # Reset counters
            self.click_count = 0
            self.scroll_up_count = 0
            self.scroll_down_count = 0
            self.update_stats()
            
            self.thread = threading.Thread(target=self.process_video, daemon=True)
            self.thread.start()
    
    def stop_tracking(self):
        self.is_running = False
        if self.cap:
            self.cap.release()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_indicator.config(text="● Stopped", fg="#f38ba8")
        self.video_canvas.config(image='', text="Camera stopped")
    
    def process_video(self):
        while self.is_running:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            frame = cv2.flip(frame, 1)
            frame_height, frame_width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = self.hand_detector.process(rgb_frame)
            hands = output.multi_hand_landmarks
            
            if hands:
                for hand in hands:
                    self.drawing_utils.draw_landmarks(frame, hand)
                    landmarks = hand.landmark
                    for id, landmark in enumerate(landmarks):
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)
                        
                        if id == 12:  # Middle finger
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            middie_x = self.screen_width / frame_width * x
                            middie_y = self.screen_height / frame_height * y
                            if self.scroll_enabled.get() and abs(middie_y - self.index_y) < 40:
                                pyautogui.scroll(-320)
                                self.scroll_down_count += 1
                                self.root.after(0, self.update_stats)
                                pyautogui.sleep(0.1)
                        
                        if id == 4:  # Thumb
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            index_x = self.screen_width / frame_width * x
                            self.index_y = self.screen_height / frame_height * y
                        
                        if id == 8:  # Index finger
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                            thumb_x = self.screen_width / frame_width * x
                            thumb_y = self.screen_height / frame_height * y
                            pyautogui.moveTo(thumb_x, thumb_y)
                            if self.click_enabled.get() and abs(self.index_y - thumb_y) < 50:
                                pyautogui.click()
                                self.click_count += 1
                                self.root.after(0, self.update_stats)
                        
                        if id == 16:  # Ring finger
                            cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 255))
                            ring_x = self.screen_width / frame_width * x
                            ring_y = self.screen_height / frame_height * y
                            if self.scroll_enabled.get() and abs(ring_y - self.index_y) < 50:
                                pyautogui.scroll(320)
                                self.scroll_up_count += 1
                                self.root.after(0, self.update_stats)
                                pyautogui.sleep(0.1)
            
            # Convert frame to PhotoImage for tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img = img.resize((640, 480), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image=img)
            
            # Update video canvas
            self.video_canvas.config(image=photo)
            self.video_canvas.image = photo
    
    def update_stats(self):
        self.clicks_label.config(text=f"Clicks: {self.click_count}")
        self.scroll_up_label.config(text=f"Scroll Up: {self.scroll_up_count}")
        self.scroll_down_label.config(text=f"Scroll Down: {self.scroll_down_count}")
    
    def on_closing(self):
        self.stop_tracking()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = HandWaveGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
