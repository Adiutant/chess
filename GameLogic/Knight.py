from GameLogic.Figure import Figure


class Knight(Figure):
    def turns(self, field, pos):
        i, j = pos
        turns = []
        for k in range(1):
            if not i + 2 > 7 and not j+1>7:
                if field[i + 2][j+1] == 0:
                    turns.append((i, j))
            if not i + 2 > 7 and not j-1<0:
                if field[i + 2][j-1] == 0:
                    turns.append((i, j))
            if not i - 2 <0 and not j+1>7:
                if field[i - 2][j+1] == 0:
                    turns.append((i, j))
            if not i - 2 <0 and not j-1<0:
                if field[i - 2][j-1] == 0:
                    turns.append((i, j))
            if not i - 1 <0 and not j+2>7:
                if field[i - 1][j+2] == 0:
                    turns.append((i, j))
            if not i + 1 >7 and not j+2>7:
                if field[i +1][j+2] == 0:
                    turns.append((i, j))
            if not i +1 >7 and not j-2<0:
                if field[i +1][j-2] == 0:
                    turns.append((i, j))
            if not i -1 <0 and not j-2<0:
                if field[i - 1][j-2] == 0:
                    turns.append((i, j))


        return turns
