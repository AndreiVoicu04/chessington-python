from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Knight, Pawn, King

class TestKnight():

    @staticmethod
    def test_whie_knight_can_move_anywhere():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 3)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 8
        assert Square.at(4, 1) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 1) in moves

    def test_black_knight_can_move_anywhere(self):

        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 8
        assert Square.at(4, 1) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 1) in moves

    def test_white_knight_cannot_move_over_white_piece(self):
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square_knight = Square.at(3, 3)
        board.set_piece(square_knight, knight)

        pawn = Pawn(Player.WHITE)
        square_pawn = Square.at(4, 1)
        board.set_piece(square_pawn, pawn)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 7
        assert Square.at(5, 2) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 1) in moves

    def test_black_knight_cannot_move_over_black_piece(self):
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square_knight = Square.at(3, 3)
        board.set_piece(square_knight, knight)

        pawn = Pawn(Player.BLACK)
        square_pawn = Square.at(4, 1)
        board.set_piece(square_pawn, pawn)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 7
        assert Square.at(5, 2) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 1) in moves

    def test_white_knight_can_capture_black_piece(self):
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square_knight = Square.at(3, 3)
        board.set_piece(square_knight, knight)

        pawn = Pawn(Player.BLACK)
        square_pawn = Square.at(4, 1)
        board.set_piece(square_pawn, pawn)

        # Act
        moves = knight.get_available_moves(board)

        assert len(moves) == 8
        assert Square.at(4, 1) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 1) in moves

    def test_black_knight_can_capture_white_piece(self):
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square_knight = Square.at(3, 3)
        board.set_piece(square_knight, knight)

        pawn = Pawn(Player.WHITE)
        square_pawn = Square.at(4, 1)
        board.set_piece(square_pawn, pawn)

        # Act
        moves = knight.get_available_moves(board)

        assert len(moves) == 8
        assert Square.at(4, 1) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 1) in moves

    def test_white_knight_cannot_capture_black_king(self):
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square_knight = Square.at(3, 3)
        board.set_piece(square_knight, knight)

        king = King(Player.BLACK)
        square_king = Square.at(4, 1)
        board.set_piece(square_king, king)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 7
        assert Square.at(5, 2) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 1) in moves

    def test_black_knight_cannot_capture_white_king(self):
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square_knight = Square.at(3, 3)
        board.set_piece(square_knight, knight)

        king = King(Player.WHITE)
        square_king = Square.at(4, 1)
        board.set_piece(square_king, king)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 7
        assert Square.at(5, 2) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(2, 1) in moves

    def test_white_knight_cannot_go_outside_of_board(self):
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square_knight = Square.at(1, 1)
        board.set_piece(square_knight, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 4
        assert Square.at(3, 0) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(2, 3) in moves
        assert Square.at(0, 3) in moves

    def test_black_knight_cannot_go_outside_of_board(self):
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square_knight = Square.at(1, 1)
        board.set_piece(square_knight, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 4
        assert Square.at(3, 0) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(2, 3) in moves
        assert Square.at(0, 3) in moves