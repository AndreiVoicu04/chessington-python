from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Bishop, Pawn, King

MIN_COORD = 0
MAX_COORD = 7
directions = [
    (1, -1), (1, 1),
    (-1, -1), (-1, 1)
]

class TestBishop():

    @staticmethod
    def test_white_bishop_can_move_anywhere_in_bounds():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        row = 4
        col = 3
        square = Square.at(row, col)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 13
        for (dir_row, dir_col) in directions:
            base_row = row + dir_row
            base_col = col + dir_col

            while MIN_COORD <= base_row <= MAX_COORD and MIN_COORD <= base_col <= MAX_COORD:
                assert Square.at(base_row, base_col) in moves
                base_row += dir_row
                base_col += dir_col

    def test_black_bishop_can_move_anywhere_in_bounds(self):
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        row = 4
        col = 4
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 13
        for (dir_row, dir_col) in directions:
            base_row = row + dir_row
            base_col = col + dir_col

            while MIN_COORD <= base_row <= MAX_COORD and MIN_COORD <= base_col <= MAX_COORD:
                assert Square.at(base_row, base_col) in moves
                base_row += dir_row
                base_col += dir_col

    def test_white_bishop_stops_before_white_piece(self):
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        row = 3
        col = 2
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, bishop)

        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(5, 4)
        board.set_piece(pawn_square, pawn)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 8
        assert Square.at(pawn_square.row - 1, pawn_square.col - 1) in moves
        assert pawn_square not in moves

    def test_black_bishop_stops_before_black_piece(self):
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        row = 3
        col = 2
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, bishop)

        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(5, 4)
        board.set_piece(pawn_square, pawn)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 8
        assert Square.at(pawn_square.row - 1, pawn_square.col - 1) in moves
        assert pawn_square not in moves

    def test_white_bishop_stops_on_black_piece(self):
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        row = 3
        col = 2
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, bishop)

        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(5, 4)
        board.set_piece(pawn_square, pawn)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 9
        assert Square.at(pawn_square.row - 1, pawn_square.col - 1) in moves
        assert pawn_square in moves
        assert Square.at(pawn_square.row + 1, pawn_square.col + 1) not in moves

    def test_black_bishop_stops_on_white_piece(self):
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        row = 3
        col = 2
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, bishop)

        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(5, 4)
        board.set_piece(pawn_square, pawn)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 9
        assert Square.at(pawn_square.row - 1, pawn_square.col - 1) in moves
        assert pawn_square in moves
        assert Square.at(pawn_square.row + 1, pawn_square.col + 1) not in moves

    def test_white_bishop_stops_before_black_king(self):
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        row = 3
        col = 2
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, bishop)

        king = King(Player.BLACK)
        king_square = Square.at(5, 4)
        board.set_piece(king_square, king)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 8
        assert Square.at(king_square.row - 1, king_square.col - 1) in moves
        assert king_square not in moves

    def test_black_bishop_stops_before_white_king(self):
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        row = 3
        col = 2
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, bishop)

        king = King(Player.WHITE)
        king_square = Square.at(5, 4)
        board.set_piece(king_square, king)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 8
        assert Square.at(king_square.row - 1, king_square.col - 1) in moves
        assert king_square not in moves