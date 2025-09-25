class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        if not matrix: return []
        res=[]
        while top<=bottom and left<=right:
            #traverse the first row
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            #last column
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            if top <=bottom:
            #lastrow in reverse
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            #column form bottom to top
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res
            
