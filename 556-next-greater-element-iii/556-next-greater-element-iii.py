class Solution:
    def nextGreaterElement(self, n):
        
        n=list(str(n))
        N=len(n)
        i=None
        
        for x in range(N-1,0,-1):
            if n[x]>n[x-1]:
                i=x-1
                break
        else:
            return -1
        
        swap=i+1
        pos=i
        
        for x in range(swap,N):
            if n[pos]<n[x]<n[swap]:
                swap=x
                
        n[pos],n[swap]=n[swap],n[pos]
                 
        ans=int(''.join(n[:pos+1])+''.join(sorted(n[pos+1:])))
        
        return ans if len(bin(ans)[2:])<32 else -1