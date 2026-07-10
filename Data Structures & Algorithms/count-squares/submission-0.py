class CountSquares:

    def __init__(self):
        self.points = {}
    
    def add(self, point: list[int]) -> None:
        x, y = point
        self.points[(x, y)] = self.points.get((x, y), 0) + 1
    
    def count(self, point: list[int]) -> int:
        px, py = point
        result = 0
        
        for (x, y), count in self.points.items():
            if abs(px - x) == abs(py - y) and px != x:
                count1 = self.points.get((px, y), 0)
                count2 = self.points.get((x, py), 0)
                
                result += count * count1 * count2
        
        return result