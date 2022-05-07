### Project Overview
The goal of our project was to recreate a simplified version of the video game 'Overcooked'. The original overcooked is a game where players try to create dishes to fulfill order tickets as fast as possible. If they go too fast and forget things, their food gets overcooked. In the real game there are many different stations, players can have dozens of things cooking or washing at a time, and the game increases in complexity the more the player plays. In our simplified version there are only eight stations; three ingredient stations, a cooking station, a plate station, a serve station, and a trash station. 

### How it Works

For each ticket, players must pick up a plate, fill the plate with the correct ingredients and serve the plate. If the plate contains a cooked item, the player also needs to get the raw ingredient from the ingredient station, drop the item off at the cooking station, and pick up to cooked item. The player engages with these actions using the AWSD or arrow keys to move around as well as the f key to pick up items and the e key to put down items. 

If a player serves a correct plate they make money; if they serve an incorrect plate or they need to trash the ingredients (such as if they pick up the wrong combination of ingredients), they lose money. Once the player serves the correct plate the ticket disappears and a new ticket appears in it's place. The player continues to fulfill tickets until they run out of time. 

### Unique Features

No idea what to put here

### Project Demo

Add video and screenshots here

### How to Play

In order to play our game, visit our github repository and fork the main branch. You will need to install pygame by running pip install pygame. Once you have done that, run python run_game.py and your pygame window will pop up. When you are done, press q to quit the game.

Once the game launches, move around the board using the AWSD or arrow keys. When you see a ticket in the top left, grab a plate by moving in range of the plate station and pressing f to pick up the item. Move to an ingredients station and press f to pick up the ingredient and add it to your plate. If you need to cook an ingredient, take the ingredient to the cooking station and put it down by pressing e. Wait 3 seconds for your ingredient to cook, then press f to pick up the cooked ingredient again. But don't wait too long! If you leave the ingredient cooking for more than 5 seconds, it'll be overcooked! If the ingredient is overcooked it will automatically be trashed and you'll lose money. 

Once your plate is ready, move to the serve station and press e to serve the plate. If you've made it correctly, you'll make money! If not, the plate will be trashed, you'll lose money, and you'll have to start again. If at any time throughout this process you pick up the wrong ingredient, you can trash your plate and start again, but you'll lose money.

Keep an eye on the clock in the top right corner. When that hits 0, it's game over!

### About Us

#### Evelyn Kessler
Class of 2024
Major: Engineering with Design
Best Quotes:
"Pygame WHY"
"I don't think this is the problem but let's try it anyway"
"I don't remember how to write unit tests" (x5)

#### Sophie Wu
Class of 2022
Major: Mechanical Engineering
Best Quotes:
"This is an artistic choice"
"What do I do with all these indentations?"
"Is it really a problem if the player can stand on the stove?"

### Attribution
We used Figma to create our game board and our player's sprites, along with the 'Iconify' plug in for the various icons. 

We used pygame tutorials on opensource.com to get started, including; https://opensource.com/article/17/12/game-framework-python, https://opensource.com/article/17/12/game-python-add-a-player, and https://opensource.com/article/17/12/game-python-moving-player.

We used the pygame library (https://www.pygame.org/wiki/about) to visualize our game.

Unique features of your project
Screenshots or demos of your project
Installation instructions (or link to the relevant portion of the README)
Download links for your project
A link to your project’s GitHub page
Information about you (to the extent you are comfortable)
Attribution for any external resources you used
