from chess_engine import game_state
from Piece import Knight, Player, Pawn

gstate = game_state()


def test_knight_center_on_empty_board():

    gstate.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight("white_n", 4, 4, Player.PLAYER_1)
    expected_moves = [
        (2, 3), (2, 5),
        (3, 2), (3, 6),
        (5, 2), (5, 6),
        (6, 3), (6, 5)
    ]

    assert set(knight.get_valid_peaceful_moves(gstate)) == set(expected_moves)


def test_knight_cannot_jump_to_pawns_starting_position():

    gstate.__init__()
    knight = Knight("white_n", 7, 1, Player.PLAYER_1)

    expected_moves = [
        (5, 0), (5, 2)
    ]

    assert knight.get_valid_peaceful_moves(gstate) == expected_moves


def test_knight_after_some_moves_mixed_board():

    from Piece import Knight, Player
    board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight("white_n", 3, 3, Player.PLAYER_1)
    board[1][2] = 'white_p'
    board[1][4] = Player.EMPTY
    board[2][1] = 'black_p'
    board[4][1] = Player.EMPTY
    board[5][2] = 'white_n'
    board[4][5] = Player.EMPTY
    gstate.board = board
    assert set(knight.get_valid_peaceful_moves(gstate)) == {(1, 4), (2, 5), (4, 1), (4, 5), (5, 4)}




def test_knight_takes_single_opponent():
    board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight("white_n", 3, 3, Player.PLAYER_1)
    board[1][2] = Pawn("black_p", 1, 2, Player.PLAYER_2)
    gstate.board = board
    expected_takes = [(1, 2)]
    assert set(knight.get_valid_piece_takes(gstate)) == set(expected_takes)


def test_knight_takes_multiple_opponents():
    board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight("white_n", 3, 3, Player.PLAYER_1)
    board[1][2] = Pawn("black_p", 1, 2, Player.PLAYER_2)
    board[5][4] = Pawn("black_p", 5, 4, Player.PLAYER_2)
    board[2][5] = Pawn("black_p", 2, 5, Player.PLAYER_2)
    gstate.board = board
    expected_takes = [(1, 2), (5, 4), (2, 5)]
    assert set(knight.get_valid_piece_takes(gstate)) == set(expected_takes)


def test_knight_does_not_take_friendly_pieces():
    board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight("white_n", 3, 3, Player.PLAYER_1)
    board[1][2] = Pawn("white_p", 1, 2, Player.PLAYER_1)
    board[5][4] = Knight("white_n", 5, 4, Player.PLAYER_1)
    gstate.board = board
    expected_takes = []
    assert set(knight.get_valid_piece_takes(gstate)) == set(expected_takes)


def test_knight_takes_opponent_and_ignores_empty():
    board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight("white_n", 3, 3, Player.PLAYER_1)
    board[1][2] = Pawn("black_p", 1, 2, Player.PLAYER_2)
    board[5][4] = Player.EMPTY
    board[2][5] = Pawn("black_p", 2, 5, Player.PLAYER_2)
    board[4][1] = Player.EMPTY
    gstate.board = board
    expected_takes = [(1, 2), (2, 5)]
    assert set(knight.get_valid_piece_takes(gstate)) == set(expected_takes)


def test_knight_at_edge_takes_opponent():
    board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
    knight = Knight("white_n", 0, 0, Player.PLAYER_1)
    board[2][1] = Pawn("black_p", 2, 1, Player.PLAYER_2)
    board[1][2] = Pawn("black_p", 1, 2, Player.PLAYER_2)
    gstate.board = board
    expected_takes = [(2, 1), (1, 2)]
    assert set(knight.get_valid_piece_takes(gstate)) == set(expected_takes)
