"""Task 2: Tic-Tac-Toe AI using Minimax."""
HUMAN, AI, EMPTY = "X", "O", " "

def winner(b):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,c,d in lines:
        if b[a] == b[c] == b[d] and b[a] != EMPTY:
            return b[a]
    return None

def show(b):
    v = [str(i+1) if x == EMPTY else x for i,x in enumerate(b)]
    print(f" {v[0]} | {v[1]} | {v[2]}\n---+---+---\n {v[3]} | {v[4]} | {v[5]}\n---+---+---\n {v[6]} | {v[7]} | {v[8]}")

def minimax(b, ai_turn, depth=0):
    w = winner(b)
    if w == AI: return 10-depth
    if w == HUMAN: return depth-10
    if EMPTY not in b: return 0
    if ai_turn:
        best = -float("inf")
        for i in range(9):
            if b[i] == EMPTY:
                b[i] = AI; score = minimax(b, False, depth+1); b[i] = EMPTY
                best = max(best, score)
        return best
    best = float("inf")
    for i in range(9):
        if b[i] == EMPTY:
            b[i] = HUMAN; score = minimax(b, True, depth+1); b[i] = EMPTY
            best = min(best, score)
    return best

def ai_move(b):
    best, move = -float("inf"), None
    for i in range(9):
        if b[i] == EMPTY:
            b[i] = AI; score = minimax(b, False, 1); b[i] = EMPTY
            if score > best: best, move = score, i
    return move

def main():
    b = [EMPTY]*9
    print("TIC-TAC-TOE — You are X; AI is O. Enter 1–9.")
    while True:
        show(b)
        raw = input("Your move (1-9): ").strip()
        if not raw.isdigit() or not 1 <= int(raw) <= 9:
            print("Please enter a number from 1 to 9."); continue
        i = int(raw)-1
        if b[i] != EMPTY:
            print("That square is occupied."); continue
        b[i] = HUMAN
        if winner(b) == HUMAN: show(b); print("You win!"); break
        if EMPTY not in b: show(b); print("Draw!"); break
        j = ai_move(b)
        if j is not None: b[j] = AI; print("AI chooses", j+1)
        if winner(b) == AI: show(b); print("AI wins. Try again!"); break
        if EMPTY not in b: show(b); print("Draw!"); break

if __name__ == "__main__":
    main()
