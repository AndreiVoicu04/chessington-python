from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Rook, Pawn, King

MIN_COORD = 0
MAX_COORD = 7
directions = [
    (1, 0), (0, 1),
    (-1, 0), (0, -1)
]


class TestRook():

    @staticmethod
    def test_white_rook_can_move_anywhere_in_bounds():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        row = 3
        col = 3
        square = Square.at(row, col)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 14
        for (dir_row, dir_col) in directions:
            base_row = row + dir_row
            base_col = col + dir_col

            while MIN_COORD <= base_row <= MAX_COORD and MIN_COORD <= base_col <= MAX_COORD:
                assert Square.at(base_row, base_col) in moves
                base_row += dir_row
                base_col += dir_col

    @staticmethod
    def test_black_rook_can_move_anywhere_in_bounds():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        row = 3
        col = 3
        square = Square.at(row, col)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 14
        for (dir_row, dir_col) in directions:
            base_row = row + dir_row
            base_col = col + dir_col

            while MIN_COORD <= base_row <= MAX_COORD and MIN_COORD <= base_col <= MAX_COORD:
                assert Square.at(base_row, base_col) in moves
                base_row += dir_row
                base_col += dir_col

    @staticmethod
    def test_white_rook_stops_before_white_piece():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        row = 3
        col = 3
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, rook)

        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(row + 2, col)
        board.set_piece(pawn_square, pawn)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 11
        assert Square.at(row + 1, col) in moves
        assert Square.at(pawn_square.row, pawn_square.col) not in moves

    @staticmethod
    def test_black_rook_stops_before_black_piece():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        row = 3
        col = 3
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, rook)

        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(row + 2, col)
        board.set_piece(pawn_square, pawn)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 11
        assert Square.at(row + 1, col) in moves
        assert Square.at(pawn_square.row, pawn_square.col) not in moves

    @staticmethod
    def test_white_rook_stops_on_black_piece():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        row = 3
        col = 3
        rook_square = Square.at(row, col)
        board.set_piece(rook_square, rook)

        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(row + 2, col)
        board.set_piece(pawn_square, pawn)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 12
        assert Square.at(row + 1, col) in moves
        assert Square.at(pawn_square.row, pawn_square.col) in moves
        assert Square.at(pawn_square.row + 1, pawn_square.col) not in moves

    @staticmethod
    def test_black_rook_stops_on_white_piece():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        row = 3
        col = 3
        rook_square = Square.at(row, col)
        board.set_piece(rook_square, rook)

        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(row + 2, col)
        board.set_piece(pawn_square, pawn)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 12
        assert Square.at(row + 1, col) in moves
        assert Square.at(pawn_square.row, pawn_square.col) in moves
        assert Square.at(pawn_square.row + 1, pawn_square.col) not in moves

    @staticmethod
    def test_white_rook_stops_before_black_king():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        row = 3
        col = 3
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, rook)

        king = King(Player.BLACK)
        king_square = Square.at(row + 2, col)
        board.set_piece(king_square, king)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 11
        assert Square.at(row + 1, col) in moves
        assert Square.at(king_square.row, king_square.col) not in moves

    @staticmethod
    def test_black_rook_stops_before_white_king():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        row = 3
        col = 3
        bishop_square = Square.at(row, col)
        board.set_piece(bishop_square, rook)

        king = King(Player.WHITE)
        king_square = Square.at(row + 2, col)
        board.set_piece(king_square, king)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 11
        assert Square.at(row + 1, col) in moves
        assert Square.at(king_square.row, king_square.col) not in moves
