11.21.2025
Project Team Members: Angel Wu and Carol Wang
Project Overview:
Our group aims to expand and optimize Connect4 Game by firstly introducing a
harder gravity-changing mode. User can choose the difficulty. In higher difficulty mode, 
the pieces on the board will randomly shift their gravity to either left or right after each round.

Secondly, we will introduce the AI vs. AI mode, which can serve as tutorial for new players.

Lastly, we will integrate those functions and change hostGame() to implement the newer version of Connect4. If possible, we will display the game through Pysript online to better visualize the game progress.

Starter code:
We've finished the first part of our game. We split our gravitg-changing mode into two parts, gravity-storing function and gravity-changing (to the right & left) function.

11.24.2025
Milestone overview:
In this milestone.py, we keep the original rules for playing connect 4. 
In addition to that, we integrated gravity_storeData, gravity_backToRight, and gravity_backToLeft into hostGame function, 
in order to shift the gravity to right or left randomly every turn, and successfully run the game for several turns.
The process of integrating the function is very smooth and we are glad that we are halfway done in finishing our project. 
In the following weeks, we aim to develop and refine AImove methods to
increase its intellect. 

12.19.2025
In the final project version, our group improved the previous AI player behaviors and introduced the mode of AI vs. AI.
For improvement of AI behaviours, we implemented new functions to let AI play more intelligently by looking for threats and opportunities, not just random moves.
For example, AI now can actively form 2-in-a-row and 3-in-a-row to form the final winning situation; at the same time,
AI now can intentionally block the opponent's 2 and 3-in-a-row potentials.
In this way, the behaviours of AI are more intellectual.

We also revised hostGame function and implemented a new aihostGame function, corresponding to two modes, either human vs. AI or AI vs. AI.

After all efforts, this rough code finally show a connect4 game played by relatively human-like AIs. Hope you enjoy playing with the AI!
