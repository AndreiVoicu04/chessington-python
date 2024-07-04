from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

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


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        possible_moves = []
        if self.player == Player.BLACK:
            # black pawn reached the bottom of the board, no more legal moves
            if current_square.row == 0:
                return []

            square_1_in_front = Square.at(current_square.row - 1, current_square.col)
            piece_1_in_front = board.get_piece(square_1_in_front)
            if piece_1_in_front is None:
                possible_moves.append(square_1_in_front)

            # pawn did not move yet, it can jump 2 squares
            if current_square.row == 6:
                square_2_in_front = Square.at(current_square.row - 2, current_square.col)
                piece_2_in_front = board.get_piece(square_2_in_front)
                if piece_1_in_front is None and piece_2_in_front is None:
                    possible_moves.append(square_2_in_front)
        else:
            # white pawn reached the bottom of the board, no more legal moves
            if current_square.row == 7:
                return []

            square_1_in_front = Square.at(current_square.row + 1, current_square.col)
            piece_1_in_front = board.get_piece(square_1_in_front)

            if piece_1_in_front is None:
                possible_moves.append(square_1_in_front)

            if current_square.row == 1:
                square_2_in_front = Square.at(current_square.row + 2, current_square.col)
                piece_2_in_front = board.get_piece(square_2_in_front)
                if piece_1_in_front is None and piece_2_in_front is None:
                    possible_moves.append(square_2_in_front)

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