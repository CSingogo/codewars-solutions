'''

Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"

'''

## solutions

def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return  "Player 1 won!"
    if p2 == "scissors" and p1 == "paper":
        return  "Player 2 won!"
    if p1 == "rock" and p2 == "paper":
        return  "Player 2 won!"
    if p2 == "rock" and p1 == "paper":
        return  "Player 1 won!"
    if p1 == "rock" and p2 == "scissors":
        return  "Player 1 won!"
    if p2 == "rock" and p1 == "scissors":
        return  "Player 2 won!"
    if p1 == p2:
        return  "Draw!"