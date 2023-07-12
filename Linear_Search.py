class Solution:
    def Linear_search(self,array,B):
        count=0
        for element in array:
            if element==B:
                count+=1
        return count
"""
Given an array A and an integer B, find the number of occurrences of B in A.
"""
if __name__ == "__main__":
    ob=Solution()
    array=list(map(int,input().split()))
    B=int(input())
    print(ob.Linear_search(array,B))