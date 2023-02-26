class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        flatBoard = "".join(board)
        flatBoard.replace(" ", '')
        
        counted = Counter(flatBoard)
        rowCount = Counter(board)
        diagonal1 = board[0][0] + board[1][1] + board[2][2]
        diagonal2 = board[2][0] + board[1][1] + board[0][2]
        diagonal = {diagonal1, diagonal2}
        
        columnCount = {}
        
        for col in range(3):
            temp = ""
            for row in range(3):
                temp += board[row][col]
            if not columnCount.get(temp):
                columnCount[temp] = 1
            else:
                columnCount[temp] += 1
        if rowCount.get("XXX") and (rowCount.get("OOO") or columnCount.get("OOO")):
            return False
        if columnCount.get("OOO") and (rowCount.get("XXX") or columnCount.get("XXX")):
            return False
        if rowCount.get('XXX')  or columnCount.get('XXX') or "XXX" in diagonal :
            return counted['X'] == counted["O"] + 1
        if rowCount.get('OOO') or columnCount.get("OOO") or "OOO" in diagonal:
            return counted['X'] == counted['O']
       
        
        if counted['X'] == counted["O"] or counted["X"] == counted["O"] + 1: 
            return True
        else:
            return False