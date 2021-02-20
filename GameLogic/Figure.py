class Figure:
    type = 1
    turnmatrix = []
    ally = []
    figures = {
        "1": "wP.png", "2": "bP.png", "3": "wK.png", "4": "bK.png", "5": "wQ.png",
        "6": "bQ.png",
        "7": "wN.png", "8": "bN.png", "9": "wR.png", "10": "bR.png", "11": "wB.png",
        "12": "bB.png"
    }

    def retDrawingSignature(self):
        if self.type == 0:
            return 0
        return self.figures[str(self.type)]

    def __init__(self, typ):
        self.type = typ
        if self.type % 2 != 0:
            self.white = 1
            self.ally = [1, 3, 5, 7, 9, 11]
        else:
            self.ally = [2, 4, 6, 8, 10, 12]
