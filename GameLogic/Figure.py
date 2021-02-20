

class Figure:
    type = 1
    turnmatrix = []
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
