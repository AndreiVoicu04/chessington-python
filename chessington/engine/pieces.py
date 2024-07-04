from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

BOARD_SIZE = 8

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

        self.BLACK_PAWNS_STARTING_ROW = 6
        self.WHITE_PAWNS_STARTING_ROW = 1

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)

    @staticmethod
    def is_in_bounds(square: Square) -> bool:
        return BOARD_SIZE > square.row >= 0 and BOARD_SIZE > square.col >= 0


class Pawn(Piece):
    def get_available_moves_single_color(self, board: Board, square_1_in_front, square_2_in_front) -> List[Square]:
        possible_moves = []
        diagonal_capture_squares = []
        current_square = board.find_piece(self)

        piece_1_in_front = board.get_piece(square_1_in_front)
        if piece_1_in_front is None:
            possible_moves.append(square_1_in_front)

        # pawn did not move yet, it can jump 2 squares
        if (current_square.row == self.BLACK_PAWNS_STARTING_ROW and self.player == Player.BLACK
                or current_square.row == self.WHITE_PAWNS_STARTING_ROW and self.player == Player.WHITE):
            piece_2_in_front = board.get_piece(square_2_in_front)
            if piece_1_in_front is None and piece_2_in_front is None:
                possible_moves.append(square_2_in_front)

        diagonal_capture_squares.append(Square.at(square_1_in_front.row, current_square.col - 1))
        diagonal_capture_squares.append(Square.at(square_1_in_front.row, current_square.col + 1))

        for square in diagonal_capture_squares:
            if not Piece.is_in_bounds(square):
                continue

            diagonal_piece = board.get_piece(square)
            if diagonal_piece is None:
                continue

            if self.player == diagonal_piece.player:
                continue

            if isinstance(diagonal_piece, King):
                continue

            possible_moves.append(square)

        return possible_moves

    def is_pawn_on_last_row(self, current_square: Square) -> bool:
        current_row = current_square.row
        match self.player:
            case Player.BLACK:
                return current_row == self.WHITE_PAWNS_STARTING_ROW - 1
            case Player.WHITE:
                return current_row == self.BLACK_PAWNS_STARTING_ROW + 1

    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        possible_moves = []

        # black pawn reached the bottom of the board, no more legal moves
        if self.is_pawn_on_last_row(current_square):
            return []

        if self.player == Player.BLACK:
            square_1_in_front = Square.at(current_square.row - 1, current_square.col)
            square_2_in_front = Square.at(current_square.row - 2, current_square.col)

            possible_moves = self.get_available_moves_single_color(board, square_1_in_front, square_2_in_front)

        else:
            square_1_in_front = Square.at(current_square.row + 1, current_square.col)
            square_2_in_front = Square.at(current_square.row + 2, current_square.col)

            possible_moves = self.get_available_moves_single_color(board, square_1_in_front, square_2_in_front)

        return possible_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []