from functools import cache
from typing import Dict, List, NamedTuple, Optional, Tuple

import numpy as np
from typing_extensions import Literal


class TileConfig(NamedTuple):
    idx: int
    rotation: int  # 0, 1, 2, 3
    flipped: bool


Tile = np.ndarray
Direction = Literal["L", "R", "U", "D"]

op_dir: Dict[Direction, Direction] = {
    "L": "R",
    "R": "L",
    "U": "D",
    "D": "U",
}

tiles: Dict[int, Tile] = {}


@cache
def get_tile(config: TileConfig) -> Tile:
    tile = tiles[config.idx]
    for _ in range(config.rotation):
        tile = np.rot90(tile)
    if config.flipped:
        tile = np.flip(tile, axis=0)
    return tile


@cache
def get_edge(config: TileConfig, edge: Direction) -> int:
    tile = get_tile(config)
    if edge == "L":
        line = tile[:, 0]
    elif edge == "R":
        line = tile[:, -1]
    elif edge == "U":
        line = tile[0]
    else:
        line = tile[-1]
    ret = 0
    for x in line:
        ret = ret * 2 + int(x)
    return ret


pattern = r"""
..................#.
#....##....##....###
.#..#..#..#..#..#...
"""
pattern = np.array([[ch == "#" for ch in row] for row in pattern.strip().split("\n")])


def find_monster(tile: Tile) -> Tuple[Tile, int]:
    n, m = pattern.shape
    cnt = 0
    marks = tile.copy()
    for x in range(tile.shape[0] - n):
        for y in range(tile.shape[1] - m):
            if np.equal(tile[x : (x + n), y : (y + m)] & pattern, pattern).all():
                cnt += 1
                marks[x : (x + n), y : (y + m)] &= ~pattern
    return marks, cnt


content = open(0).read().strip()

tiles_str = content.split("\n\n")
for s in tiles_str:
    lines = s.split("\n")
    idx = int(lines[0].split()[1].rstrip(":"))
    tiles[idx] = np.array([[ch == "#" for ch in line] for line in lines[1:]])

length = int(np.sqrt(len(tiles)))
board: List[List[Optional[TileConfig]]] = [[None] * length for _ in range(length)]
chosen: Dict[int, bool] = {idx: False for idx in tiles.keys()}


def dfs(x: int, y: int) -> bool:
    if y == length:
        return dfs(x + 1, 0)
    if x == length:
        return True
    for idx in chosen.keys():
        if chosen[idx]:
            continue
        for rotation in range(4):
            for flip in [False, True]:
                config = TileConfig(idx, rotation, flip)
                ok = True
                if x > 0:
                    ok &= get_edge(config, "U") == get_edge(board[x - 1][y], "D")
                if y > 0:
                    ok &= get_edge(config, "L") == get_edge(board[x][y - 1], "R")
                if not ok:
                    continue
                board[x][y] = config
                chosen[idx] = True
                if dfs(x, y + 1):
                    return True
                chosen[idx] = False
    return False


dfs(0, 0)
indices = np.empty((length, length))
for x in range(length):
    for y in range(length):
        indices[x, y] = board[x][y].idx

# part 1
print(int(indices[0, 0] * indices[0, -1] * indices[-1, 0] * indices[-1, -1]))

pic = [[get_tile(config)[1:-1, 1:-1] for config in row] for row in board]
pic = np.vstack([np.hstack(row) for row in pic])

tiles[-1] = pic

for rotation in range(4):
    for flip in [False, True]:
        marks, cnt = find_monster(get_tile(TileConfig(-1, rotation, flip)))
        if cnt > 0:
            # part 2
            print(marks.sum())
