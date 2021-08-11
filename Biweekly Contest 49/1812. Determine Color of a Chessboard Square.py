class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0]) - ord('a')+1) % 2 == int(coordinates[1]) % 2: #same odd or same even
            return False
        else:
            return True