import pygame
import chess
import random 

pygame.init()
BOARD_SIZE = 512 
screen = pygame.display.set_mode((BOARD_SIZE,BOARD_SIZE))
chessboard_img = pygame.image.load("/Users/christaldika/Desktop/chessboardgreen.png")
chessboard_img = pygame.transform.scale(chessboard_img, (BOARD_SIZE,BOARD_SIZE))

piece_images = {
    chess.PAWN: {
        chess.WHITE: pygame.image.load("/Users/christaldika/Desktop/Chess/whitepawn.png"),
        chess.BLACK: pygame.image.load("/Users/christaldika/Desktop/Chess/blackpawn.png")
    },
    chess.ROOK: {
        chess.WHITE: pygame.image.load("/Users/christaldika/Desktop/Chess/whiterook.png"),
        chess.BLACK: pygame.image.load("/Users/christaldika/Desktop/Chess/blackrook.png")
    },
    chess.KNIGHT: {
        chess.WHITE: pygame.image.load("/Users/christaldika/Desktop/Chess/whiteknight.png"),
        chess.BLACK: pygame.image.load("/Users/christaldika/Desktop/Chess/blackknight.png")
    },
    chess.BISHOP: {
        chess.WHITE: pygame.image.load("/Users/christaldika/Desktop/Chess/whitebishop.png"),
        chess.BLACK: pygame.image.load("/Users/christaldika/Desktop/Chess/blackbishop.png")
    },
    chess.QUEEN: {
        chess.WHITE: pygame.image.load("/Users/christaldika/Desktop/Chess/whitequeen.png"),
        chess.BLACK: pygame.image.load("/Users/christaldika/Desktop/Chess/blackqueen.png")
    },
    chess.KING: {
        chess.WHITE: pygame.image.load("/Users/christaldika/Desktop/Chess/whiteking.png"),
        chess.BLACK: pygame.image.load("/Users/christaldika/Desktop/Chess/blackking.png")
    }
}
board = chess.Board()
def get_square_from_mouse(pos):
    file = pos[0] // (BOARD_SIZE//8)
    rank = 7 - (pos[1]//(BOARD_SIZE//8))
    return chess.square(file,rank)
def make_random_move():
    legal_moves = list(board.legal_moves)
    if legal_moves:
        random_move = random.choice(legal_moves)
        board.push(random_move)

selected_square = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                square_clicked = get_square_from_mouse(pygame.mouse.get_pos())
                piece = board.piece_at(square_clicked)
                if piece is not None and piece.color == board.turn:
                    selected_square = square_clicked
                elif selected_square is not None:
                    legal_moves = [move for move in board.legal_moves if move.from_square == selected_square]
                    for move in legal_moves:
                        if move.to_square == square_clicked:
                            if board.piece_type_at(selected_square) == chess.PAWN and (chess.square_rank(square_clicked) == 0 or chess.square_rank(square_clicked) == 7):
                                board.push(chess.Move(selected_square, square_clicked, promotion=chess.QUEEN))
                            else:
                                board.push(move)
                            selected_square = None
                            make_random_move()
                            break
    
    screen.fill((255,255,255))
    screen.blit(chessboard_img, (0,0))
    if selected_square is not None:
        legal_moves = [move.to_square for move in board.legal_moves if move.from_square == selected_square]
        for move_square in legal_moves:
            x,y = chess.square_file(move_square) * (BOARD_SIZE // 8), (7 - chess.square_rank(move_square)) * (BOARD_SIZE // 8)
            pygame.draw.rect(screen, (173,216,230), (x,y, BOARD_SIZE // 8, BOARD_SIZE // 8))
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            row = 7 - chess.square_rank(square)
            col = chess.square_file(square)
            square_size = BOARD_SIZE // 8
            x = col * (BOARD_SIZE // 8) + (square_size - piece_images[piece.piece_type][piece.color].get_width()) // 2
            y = row * (BOARD_SIZE // 8) + (square_size - piece_images[piece.piece_type][piece.color].get_height()) // 2
            screen.blit(piece_images[piece.piece_type][piece.color],(x,y))
    pygame.display.flip()

pygame.quit()
            

        

                    







