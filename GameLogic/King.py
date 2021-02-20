from GameLogic.Figure import Figure


class King(Figure):
    def turns(self, field, pos):
        i, j = pos
        turns = []
        for k in range(1):
            if not i + k > 7:
                if field[i + k][j] == 0:
                    turns.append((i, j))
            if not i - k < 0:
                if field[i - k][j] == 0:
                    turns.append((i, j))
            if not i + k > 7 and not j - k < 0:
                if field[i + k][j - k] == 0:
                    turns.append((i, j))
            if not i + k > 7 and not j + k > 7:
                if field[i + k][j + k] == 0:
                    turns.append((i, j))
            if not i - k < 0 and not j - k < 0:
                if field[i - k][j - k] == 0:
                    turns.append((i, j))
            if not i - k < 0 and not j + k > 7:
                if field[i - k][j + k] == 0:
                    turns.append((i, j))
            if not j + k > 7:
                if field[i][j + k] == 0:
                    turns.append((i, j))
            if not j - k < 0:
                if field[i][j - k] == 0:
                    turns.append((i, j))
        return turns
