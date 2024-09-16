import tkinter as tk
from tkinter import messagebox
import serial
import time


ser = serial.Serial('COM5', 9600,timeout=1 )
time.sleep(2)  # Wait for the connection to establish

def send_angle():
    try:
        angle = int(angle_entry.get())
        if 0 <= angle <= 180:
            ser.write(f"{angle}\n".encode())  # Send the angle to Arduino
          #  response = ser.readline().decode().strip()
           # messagebox.showinfo("Success", f"Arduino: {angle}")
        else:
            messagebox.showwarning("Invalid Input", "Angle must be between 0 and 180.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Servo Angle Control")
root.minsize(200,200)

# Create and place the widgets
tk.Label(root, text="Enter Angle (0-180):").pack(pady=10)
angle_entry = tk.Entry(root, width=10)
angle_entry.pack(pady=5)

send_button = tk.Button(root, text="Send Angle", command=send_angle)
send_button.pack(pady=20)

# Start the main loop
root.mainloop()

# Close the serial connection when the window is closed
ser.close()
