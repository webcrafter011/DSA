import tkinter as tk
import random
import time

# Sample text to type
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great language for building projects.",
    "A journey of a thousand miles begins with a single step.",
    "Code like a pro with Monkeytype clone.",
    "Success is the sum of small efforts repeated day in and day out.",
]


class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monkeytype Clone")
        self.root.geometry("700x500")
        self.root.config(bg="black")

        self.start_time = None
        self.end_time = None
        self.original_text = None
        self.typed_text = None
        self.countdown = 3

        # Create and place widgets
        self.title_label = tk.Label(
            self.root,
            text="Welcome to Monkeytype Clone",
            font=("Helvetica", 24, "bold"),
            bg="black",
            fg="yellow",
        )
        self.title_label.pack(pady=40)

        self.text_label = tk.Label(
            self.root,
            text="Press Start to begin",
            font=("Helvetica", 16),
            bg="black",
            fg="white",
            wraplength=600,
        )
        self.text_label.pack(pady=10)

        # Text box to show the text to be typed
        self.text_display = tk.Label(
            self.root, text="", font=("Helvetica", 16), bg="black", fg="white"
        )
        self.text_display.pack(pady=20)

        # Input area for user typing
        self.text_box = tk.Text(
            self.root,
            font=("Helvetica", 14),
            width=70,
            height=4,
            wrap=tk.WORD,
            bd=0,
            highlightthickness=0,
        )
        self.text_box.pack(pady=20)
        self.text_box.config(state="disabled")  # Disable the text box initially

        # Start/Submit button
        self.start_button = tk.Button(
            self.root,
            text="Start",
            font=("Helvetica", 16),
            command=self.start_test,
            bg="yellow",
            fg="black",
            relief="raised",
            width=15,
            height=2,
        )
        self.start_button.pack(pady=30)

        # Restart button (initially hidden)
        self.restart_button = tk.Button(
            self.root,
            text="Restart",
            font=("Helvetica", 16),
            command=self.restart_test,
            bg="yellow",
            fg="black",
            relief="raised",
            width=15,
            height=2,
        )
        self.restart_button.pack(pady=30)
        self.restart_button.config(state="disabled")  # Initially disabled

        # Result display area
        self.result_label = tk.Label(
            self.root, text="", font=("Helvetica", 16), bg="black", fg="white"
        )
        self.result_label.pack(pady=10)

        # Footer
        self.footer_label = tk.Label(
            self.root,
            text="Powered by Python & Tkinter",
            font=("Helvetica", 10),
            bg="black",
            fg="yellow",
        )
        self.footer_label.pack(side="bottom", pady=10)

    def start_test(self):
        self.text_box.delete(1.0, tk.END)  # Clear the text box
        self.text_box.config(state="normal")
        self.result_label.config(text="")

        # Countdown before starting the test
        self.countdown_timer()

    def countdown_timer(self):
        if self.countdown > 0:
            self.text_label.config(text=f"Starting in {self.countdown}...", fg="yellow")
            self.countdown -= 1
            self.root.after(
                1000, self.countdown_timer
            )  # Call the function again after 1 second
        else:
            self.original_text = random.choice(sample_texts)
            self.text_display.config(text=self.original_text)
            self.text_label.config(text="Start typing the above text:", fg="white")
            self.start_time = time.time()
            self.text_box.focus()  # Focus on the text box for user input
            self.start_button.config(
                text="Submit", command=self.end_test, bg="yellow", fg="black"
            )

    def end_test(self):
        self.typed_text = self.text_box.get(1.0, tk.END).strip()

        # Stop the timer
        self.end_time = time.time()

        # Calculate WPM and accuracy
        wpm = self.calculate_wpm()
        accuracy = self.calculate_accuracy()

        # Display results
        self.result_label.config(
            text=f"Words Per Minute: {wpm:.2f}\nAccuracy: {accuracy:.2f}%", fg="yellow"
        )
        self.text_box.config(state="disabled")
        self.start_button.config(
            state="disabled"
        )  # Disable the button after test submission
        self.restart_button.config(
            state="normal"
        )  # Enable the restart button after test completion

    def calculate_wpm(self):
        # Words per minute calculation
        words = len(self.typed_text.split())
        time_taken = (self.end_time - self.start_time) / 60  # time in minutes
        wpm = words / time_taken if time_taken > 0 else 0
        return wpm

    def calculate_accuracy(self):
        typed_text = self.typed_text.strip()
        original_text = self.original_text.strip()

        correct_chars = sum(1 for a, b in zip(typed_text, original_text) if a == b)
        accuracy = (
            (correct_chars / len(original_text)) * 100 if len(original_text) > 0 else 0
        )
        return accuracy

    def restart_test(self):
        # Reset the necessary elements to restart the test
        self.text_box.config(state="normal")
        self.text_box.delete(1.0, tk.END)  # Clear the text box
        self.result_label.config(text="")
        self.start_button.config(
            text="Start",
            command=self.start_test,
            bg="yellow",
            fg="black",
            state="normal",
        )
        self.restart_button.config(
            state="disabled"
        )  # Disable the restart button until the test ends
        self.text_display.config(text="")
        self.text_label.config(text="Press Start to begin", fg="white")
        self.countdown = 3  # Reset countdown to 3 for the new test


# Create the Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
