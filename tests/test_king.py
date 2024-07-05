from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Knight, Bishop, Rook, Queen, King

MIN_COORD = 0
MAX_COORD = 7

class TestKing():
    @staticmethod
    def test_white_king_can_move_anywhere():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        row = 3
        col = 3
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 8
        assert Square.at(row + 1, col - 1) in moves
        assert Square.at(row + 1, col) in moves
        assert Square.at(row + 1, col + 1) in moves
        assert Square.at(row, col - 1) in moves
        assert Square.at(row + 1, col + 1) in moves
        assert Square.at(row - 1, col - 1) in moves
        assert Square.at(row - 1, col) in moves
        assert Square.at(row - 1, col + 1) in moves


    @staticmethod
    def test_black_king_can_move_anywhere():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        row = 3
        col = 3
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 8
        assert Square.at(row + 1, col - 1) in moves
        assert Square.at(row + 1, col) in moves
        assert Square.at(row + 1, col + 1) in moves
        assert Square.at(row, col - 1) in moves
        assert Square.at(row + 1, col + 1) in moves
        assert Square.at(row - 1, col - 1) in moves
        assert Square.at(row - 1, col) in moves
        assert Square.at(row - 1, col + 1) in moves

    @staticmethod
    def test_white_king_cannot_go_out_of_bounds():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        row = 0
        col = 0
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 3
        assert Square.at(row + 1, col) in moves
        assert Square.at(row + 1, col + 1) in moves
        assert Square.at(row, col + 1) in moves

    @staticmethod
    def test_black_king_cannot_go_out_of_bounds():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        row = 7
        col = 7
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 3
        assert Square.at(row, col - 1) in moves
        assert Square.at(row - 1, col - 1) in moves
        assert Square.at(row - 1, col) in moves

    @staticmethod
    def test_king_cannot_go_in_check_by_opposite_queen():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        row = 0
        col = 4
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        queen = Queen(Player.BLACK)
        queen_square = Square.at(row + 7, col - 1)
        board.set_piece(queen_square, queen)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 3
        assert Square.at(row, col - 1) not in moves
        assert Square.at(row + 1, col - 1) not in moves

    @staticmethod
    def test_king_does_not_get_checked_by_own_queen():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        row = 0
        col = 4
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        queen = Queen(Player.WHITE)
        queen_square = Square.at(row + 7, col - 1)
        board.set_piece(queen_square, queen)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 5
        assert Square.at(row, col - 1) in moves
        assert Square.at(row + 1, col - 1) in moves

    @staticmethod
    def test_king_cannot_go_in_check_by_opposite_rook():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        row = 0
        col = 4
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        rook = Rook(Player.BLACK)
        rook_square = Square.at(row + 7, col - 1)
        board.set_piece(rook_square, rook)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 3
        assert Square.at(row, col - 1) not in moves
        assert Square.at(row + 1, col - 1) not in moves

    @staticmethod
    def test_king_does_not_get_checked_by_own_rook():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        row = 0
        col = 4
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        rook = Rook(Player.WHITE)
        rook_square = Square.at(row + 7, col - 1)
        board.set_piece(rook_square, rook)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 5
        assert Square.at(row, col - 1) in moves
        assert Square.at(row + 1, col - 1) in moves

    @staticmethod
    def test_king_cannot_go_in_check_by_opposite_bishop():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        row = 0
        col = 4
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(row + 2, col - 1)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 3
        assert Square.at(row + 1, col) not in moves
        assert Square.at(row, col + 1) not in moves

    @staticmethod
    def test_king_does_not_get_checked_by_own_bishop():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        row = 0
        col = 4
        king_square = Square.at(row, col)
        board.set_piece(king_square, king)

        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(row + 2, col - 1)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 5
        assert Square.at(row + 1, col) in moves
        assert Square.at(row, col + 1) in moves