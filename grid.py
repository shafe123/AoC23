from typing import Any
from copy import deepcopy


class Grid[T]:
    def __init__(
        self,
        matrix: list[list[T]],
        headers: list[str] = [],
        prepad: T = None,
        postpad: T = None,
    ) -> None:
        if prepad and postpad:
            raise ValueError("Cannot both prepad and postpad")

        self.grid = deepcopy(matrix)
        self.headers = headers

        if prepad or postpad:
            max_row = max([len(row) for row in self.grid])
            if prepad:
                for row in self.grid:
                    while len(row) < max_row:
                        row.insert(0, prepad)
            else:
                for row in self.grid:
                    while len(row) < max_row:
                        row.append(postpad)

    def num_rows(self):
        return len(self.grid)

    def num_cols(self):
        return len(self.grid[0])

    def extend_rows(self, new_rows: list[list[T]]):
        self.grid.extend(new_rows)

    def extend_cols(self, new_cols: list[list[T]]):
        assert len(new_cols) == len(self.grid)

        for index, row in enumerate(self.grid):
            row.extend(new_cols[index])

    def __getitem__(self, indices: Any | tuple | slice):
        if isinstance(indices, tuple):
            if len(indices) == 1 and isinstance(indices[0], tuple):
                indices = indices[0]
                return self.grid[indices[0]][indices[1]]
            else:
                raise IndexError(f"{indices} is not a valid index.")
        elif isinstance(indices, slice):
            start = indices.start
            stop = indices.stop
            step = indices.step
            # check start
            if not start:
                start = (0, 0)

            if not (isinstance(start, tuple) and len(start) == 2):
                raise IndexError(f"Error with slice start")

            # check stop
            if not stop:
                stop = (len(self.grid), len(self.grid[0]))

            if not (isinstance(stop, tuple) and len(stop) == 2):
                raise IndexError(f"Error with slice stop")

            # check step
            if not step:
                step = (1, 1)

            if not (isinstance(step, tuple) and len(step) == 2):
                raise IndexError(f"Error with slice step")

            result = []
            for row in range(start[0], stop[0], step[0]):
                new_row = []
                for col in range(start[1], stop[1], step[1]):
                    new_row.append(self.grid[row][col])
                result.append(new_row)
            return result
        else:
            raise TypeError(f"Type {type(indices)} is not supported for indexing.")

    def __setitem__(self, indices: Any | tuple, value: T | list[list[T]]):
        if isinstance(indices, tuple):
            if len(indices) == 2:
                self.grid[indices[0]][indices[1]] = value
            else:
                raise IndexError(f"{indices} is not a valid index.")
        elif isinstance(indices, slice) and isinstance(value, list):
            start = indices.start
            stop = indices.stop
            step = indices.step
            # check start
            if not start:
                start = (0, 0)

            if not (isinstance(start, tuple) and len(start) == 2):
                raise IndexError(f"Error with slice start")

            # check stop
            if not stop:
                stop = (len(self.grid), len(self.grid[0]))

            if not (isinstance(stop, tuple) and len(stop) == 2):
                raise IndexError(f"Error with slice stop")

            # check step
            if not step:
                step = (1, 1)

            if not (isinstance(step, tuple) and len(step) == 2):
                raise IndexError(f"Error with slice step")
            
            assert 0 < start[0] < stop[0] < len(self.grid)
            assert 0 < start[1] < stop[1] < len(self.grid[0])
            assert len(value) == (stop[0] - start[0]) // step[0]
            assert len(value[0]) == (stop[1] - start[1]) // step[1]

            for row in range(start[0], stop[0], step[0]):
                for col in range(start[1], stop[1], step[1]):
                    self.grid[row][col] = value[row - start[0]][col - start[1]]
        else:
            raise ValueError(f"Type {type(indices)} is not supported for setting.")
