class Solution(object):
    def gameOfLife(self, board):
        #we will change states such that it conveys current as well as previos state
        # eg if <2 ,1->0 = 2
        # .     2,3 1->1 = 1
        # .     >3, 1->0 = 2
        # .      3, 0->1 = 3
        # so 2 denotes dead now, alive before and 3 denotes alive now dead before
        if not board:
            return
        m=len(board)     #rows
        n=len(board[0])  #columns
        for i,row in enumerate(board):
            for j,ele in enumerate(row):
                count=0
                for r in range(max(0,i-1),min(i+2,m)):
                    for c in range(max(0,j-1),min(j+2,n)):
                        if (i,j)!=(r,c) and  1<=board[r][c]<=2:
                            count+=1
                if ele==0:
                    if count==3:
                        board[i][j]=3
                else:
                    if count>3 or count<2:
                        board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j]==2:
                    board[i][j]=0
                if board[i][j]==3:
                    board[i][j]=1        
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """