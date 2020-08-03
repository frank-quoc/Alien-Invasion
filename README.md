# Alien-Invasion

This is Project 1 from the "Python Crash Course" book of the popular arcade game for me to practice my Python skills.

<div align=center margin= auto> 
  <img src="https://raw.githubusercontent.com/frank-quoc/Alien-Invasion/master/images/game_sample.png"  width=80%>
</div>

## Table of Contents
1. [Getting Started](README.md#getting-started)
    * [Prerequisites](README.md#prerequisites)
    * [Installation](README.md#installation)
    * [How to run the game](README.md#how-to-run-the-game)
2. [Game Rules](README.md#game-rules)
3. [File Descriptions](README.md#file-descriptions)
4. [Credits](README.md#credits)

## Getting Started
Please follow these instructions to download the game and play on your local machine. 

### Prerequisites
You will need to install the following:

```
Python 3.7.3
Pygame
```

### Installation

**Alien Invasion Game**

Enter the following into a Linux terminal and `cd` into the repository.

```
git clone https://github.com/frank-quoc/Alien-Invasion.git
```

**Python 3**

Install Python 3.7.3
```
cd scripts
./install_python3.7.sh
```


**Pygame**

Setting up Pygame for Python 3 is a two-step process; first you'll install some packages that Pygame depends on, then you'll download and install Pygame.

Run the following commands to install the packages required to run Alien Invasion. (If you use a command such as `python3.5` on your system, replace `python3-dev` with `python3.5-dev`):

    $ sudo apt-get install python3-dev mercurial
    $ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev

If you want to enable some more advanced functionality in Pygame such as the ability to add sounds, you can also install the following libraries:

    $ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
    $ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
    $ sudo apt-get install python-numpy

You'll need pip for the next step; if you haven't set up pip yet, see the [instructions for seting up pip](installing_pip.md). Enter the following to install Pygame:

    $ pip install --user hg+http://bitbucket.org/pygame/pygame

The output will pause for a moment, informing you which libraries were found. Press **Enter**, even if there are some libraries missing. You should see a message that Pygame installed successfully. To confirm the installation was successful, start a Python terminal session and try to import Pygame by entering the following:

    $ python3
    >>> import pygame
    >>>

If you see no error messages, you're ready to start working on Alien Invasion!

Once you have finished installing everything, you are ready to run the game.

### How to run the game

Move back to the root directory of the repository and execute

```
python3.7 alien_invasion.py
```

## Game Rules

> In Alien Invasion, the player controls a ship that appears at 
the bottom center of the screen. THe player can move the ship
right and left using the arrow keys and shoot bullets using the
spacebar. When the game begins, a fleet of aliens fills the sky
and moves across and down the screen. The player shoots and
destroys the aliens. If the player shoots all the aliens, a new fleet 
appears that moves faster than the previous fleet. If any alien hits 
the player's ship or reaches the bottom of the screen, the player
loses a ship. If the player loses three ships, the game ends.

## File Descriptions
---
File|Task
---|---
__pycache__ | Folder of bytcode .pyc files
images | Player's ship, alien ship, and game sample
alien.py | Alien's sprite and attributes
alien_invasion.py | Runs the game
bullet.py | Bullet's sprite and attributes
button.py | Game's start button attributes
game_functions.py | Game's settings, including screen, rules, player movement, etc
game_stats.py | Stats for Alien Invasion
pygame-1.9.6-cp37-cp37m-win_amd64.whl | Python wrapper module for the SDL multimedia library
scoreboard.py | Class to report scoreboard info
settings.py | Class to store all settings for Alien Invasion
ship.py | Player's ship and attributes


## Credits

Made by Frank Ho | [@frank_quoc](https://twitter.com/frank_quoc)

Originally created by [Eric Matthes](https://github.com/ehmatthes/pcc/tree/master/chapter_12)
