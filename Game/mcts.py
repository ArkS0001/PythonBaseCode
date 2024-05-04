import chess
import random

class Node:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent 
        self.children = []
        self.visits = 0
        self.wins = 0

    def expand(self):
        if not self.children:
            legal_moves = list(self.board.legal_moves)
            for move in legal_moves:
                next_board = self.board.copy()
                next_board.push(move)
                self.children.append(Node(next_board,self))

    def select_child(self):
        if self.visits == 0:
            return random.choice(self.children) if self.children else None
        else:
            return max(self.children, key=lambda c: c.wins/(c.visits or 1) + 1.4 * (2 * (c.visits/(self.visits or 1))) ** 0.5)
    def rollout(self):
        board_copy = self.board.copy()  
        while not board_copy.is_game_over():  
            legal_moves = list(board_copy.legal_moves) 
            random_move = random.choice(legal_moves) 
            board_copy.push(random_move) 
        result = board_copy.result()
        if result == '1-0':
            return 1
        elif result == '0-1':
            return -1
        else:
            return 0
        
    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)

class MCTS:
    def __init__(self, board):
        self.root = Node(board)
    def select_move(self):
        for _ in range(100):
            node = self.select_node()
            #node = self.select_node()
            result = node.rollout()
            node.backpropagate(result)
        return self.root.select_child().board.peek()
    
    def select_node(self):
        node = self.root
        while node.children:
            if all(child.visits > 0 for child in node.children):
                node = node.select_child()
            else:
                return random.choice(node.children)
        node.expand()
        return random.choice(node.children)

board = chess.Board()
mcts = MCTS(board)
best_move = mcts.select_move()
print("Best Move:", best_move)
            
        


       

           
        
        
            






