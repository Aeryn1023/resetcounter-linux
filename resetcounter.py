from pynput import keyboard

counter = 0
paused = False
print("Welcome to the Reset Counter. This is a simple program I made as an autonomous counter for resets in Pokemon games via RetroArch")
print ()
print("Here are the hotkeys used in order to use this program:")
print("-----------------------------------------------------------------")
print("H: Default reset key for RetroArch. If your hotkey is different, Replace the h in line 16 with the correct keyboard button")
print("F9: Pauses/Unpauses the counter should it be required.")
print()
print("If you'd prefer to bind the pause key to a letter key, replace keyboard.Key.f9 with keyboard.KeyCode.from_char('letter'):")
print ()

def on_press(key):
    global counter, paused

    if not paused:
        if key == keyboard.KeyCode.from_char('h'):
            counter += 1
            print ("Resets:", counter)

def on_release(key):
    global paused

    if key == keyboard.Key.f9:
        paused = not paused
        if paused:
            print("Counter Paused")
        else:
            print("Counter Resumed")

# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

while True:
    pass
