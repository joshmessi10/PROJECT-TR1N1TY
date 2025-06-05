class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        end = 0
        i=0
        k=1
        arr = []
        letter = ""
        while i < len(s):
            letter = s[i]
            while k < len(s):
                #print(f"Comparison: {s[k]} and {s[i]}")
                if s[k] == s[i]:
                    end = max(k, end)
                    #print("New End: ", end)
                k+=1
            if i==end:
                #print("Check")
                arr.append(len(s[start:end+1]))
                start=i+1
                end=i+1
            i+=1
            k=start
        return arr
            
