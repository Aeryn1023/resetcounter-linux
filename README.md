# resetcounter-linux
 Welcome to the terminal-based reset counter! There are a few things worth mentioning, so I'll mention them real quick.

 This program is something I whipped up in a matter of a couple hours, using ChatGPT for debugging purposes as I'm still learning python, and figured this was an easy enough project to make.
 The program itself takes the keyboard input "h" (As it's the default hotkey for resetting a game in RetroArch), and adds a 1 to the counter, essentially removing the need to alt-tab and manually add a 1 to a counter, saving a lot of time in the process. I'm sure there are better, more well-built applications out there that handle this kind of thing, although I haven't been able to find anything like that myself.

 The program itself, when started, should detail the default controls. If for any reason you need to edit the file (such as changing the keys you need to press), it's recommended that you also install the "pylsp" package, especially if you're using Kate like I did, the process for which should be something along the lines of: sudo insertpackagemanagerhere install python3-pylsp. In my case I use Ubuntu, so you should refer to the internet for installing packages for your distro of choice if you aren't at all familiar with your distro or the terminal.

 If the script fails to run, try running the test_pynput.py script to make sure pynput is working correctly

 Here are the dependencies needed to run the script:
    - Python 3.x
    - pynput

If you don't already have python installed, you can install it and pynput with the following commands depending on your distro:

    - For Ubuntu/Debian-based distros (Ubuntu, Debian, Linux Mint, PopOS, etc.):
    sudo apt install python3
    sudo apt install python3-pynput

    - For OpenSUSE
    sudo zypper install python3
    sudo zypper install python3-pynput

    - For CentOS/Fedora Linux
    Fedora: sudo dnf install python3
            sudo dnf install python3-pynput
    CentOS: sudo yum install python3
            sudo yum install python3-pynput

    - For Arch Linux and distros based on it
    sudo pacman -S python
    sudo pacman -S python3-pynput

If for some reason the necessary packages are not available, it's recommended that you look up the proper package names for your distro of choice. Most of these distros are ones I have not used before (save for Arch),
or are ones I haven't used in over 3+ years.

If for some reason the required packages are only available in the AUR (Arch users only), then it's recommended you install the application "yay", and install them with yay -S. Yaourt works, however yay is ideal if you
want minimalism and as little bloat as possible, although that's up to personal preference. I do not have Arch set up on my end, so I don't know if any of these packages are AUR-only, however I figured this note here
should suffice in the event that they are AUR-only, like many other packages are.

Once you have the dependencies installed, simply run resetcounter.py with "python3 resetcounter.py" or alternatively, use the included bash script, runcounter.sh.

If you want to run the shell script to run the counter, simply use the following command after cd'ing into the correct folder (or opening a new terminal window there):
./runcounter.sh

You can also add a menu entry by using a menu editor like KDE Menu Editor, and under the "Program" field, put in the path to the .sh file like so:
        - /home/youruserhere/Applications/resetcounter/resetcounter.sh

Once that's done, go to "Advanced" and click "Open in Terminal". The instructions may vary slightly, but the .sh file should still find the script regardless of how you set it up.

Also included is an older shell script I made which relies on fish being your default shell (yes, I know it's kinda mid, I just prefer it, don't @ me.) If need-be, you can replace the line that defines which shell to run with your shell of choice, although please be aware it's lacking many of the things present in the .py script, and should only be used to mess around with.

That should be all there is to it, I hope you enjoy this simple little application, and good luck shiny hunting/anything else you may need to use it for!

-Mayravixx
