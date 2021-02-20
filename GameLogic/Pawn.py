from GameLogic.Figure import Figure
class Pawn(Figure):
    def turns(self,field,pos):
        i,j = pos
        turns =[]
        for k in range(1):
            if not i+k >7:
                if field[i+k][j]==0:
                    turns.append((i,j))
        return turns