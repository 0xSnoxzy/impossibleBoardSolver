# prisonersChessboardSolver
Just a program that solves the famous prisoners puzzle, 3blue1brown made a video about, here is the link: https://youtu.be/wTJI_WuZSwE?si=Bw1feObsWtTTR1zL

## Disclaimer:
This is a simplified version of the problem, the original is in a 8x8 board, but the steps to achieve freedom should be the same :)

### The problem:
You and a fellow prisoner are imprisoned in a dungeon and are facing execution. As is usual in these problems, the prison warden has both a love of recreational mathematics and an unusual amount of judicial latitude when it comes to deciding your fate. They want to give you and your cellmate a chance of freedom but don’t want to make it too easy for you.

They have a chessboard where each square is covered by a coin — either heads or tails. Moreover it’s a special chess board with a hidden compartment in each square. A single one of these squares contains a symbolic key to the jail and freedom for you and your cell companion. You will know which square contains the key and your fellow prisoner has to guess.

The rules are as follows:

(1) You and your cellmate can discuss how to encode a message using the chessboard but the prison warden can hear and understand everything that you say.
(2) Once you have decided on a system, your companion leaves the room.
(3) You observe the prison warden hiding the key in one square and then arranging the 64 coins as heads or tails however they deem fit — presumably trying to frustrate your system.
(4) You then turn over exactly one coin on the chess board and leave the room.
(5) Your companion re-enters the room, without having any opportunity to see or communicate with you. He observes the chessboard and the arrangement of coins and points to the square where he believes the key and freedom reside.
(6) Nothing sneaky is allowed on pain of immediate death i.e. This is a pure logic problem- there is no meta game. Paper and Pencil, calculator and plenty of time are available to you and your cellmate if necessary.

### The solution:
For clarity we will divide the two players calling them Player 1 and Player 2 (obviously player 1 will go first)
The problem can be solved by a simple step-by-step path:

Player 1 (The first who sees the chessboard and know where the key is) should:
Firstly find all positions that are heads up: 

To simplify the steps lets set a testcase:
{0011, 0101, 1000, 1010, 1100}

Then he will XOR all positions:

0011 XOR 0101 XOR 1000 XOR 1010 XOR 1100 -> 1000

Find different bits between the keys position and the current message: 0010 XOR 1000 -> 1010
Flip the coin at position 1010

Then Player 2 will enter the room and will follow a similar path as Player 1:

He will find all positions that are heads up: 

{0011, 0101, 1000, 1100}

XOR all positions:
0011 XOR 0101 XOR 1000 XOR 1100 -> 0010

Look under the coin in position 0010 and he will find the key, winning freedom for the both of the prisoners ;D
