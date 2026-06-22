class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        a=0
        le=0
        br=0
        while(l<r):
            br=r-l
            if heights[l]>heights[r]:
                le=heights[r]
                r=r-1
            elif heights[l]==heights[r]:
                le=heights[r]
                r=r-1
            elif heights[l]<heights[r]:
                le=heights[l]
                l=l+1
            
            if (le*br)>a:
                a=le*br
        return(a)

        