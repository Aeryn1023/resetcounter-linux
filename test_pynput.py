from pynput import keyboard

def on_press(key):
    print("Key pressed:", key)

# Create a listener for keyboard events
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the script running
listener.join()
