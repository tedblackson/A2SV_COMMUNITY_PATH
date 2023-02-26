class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        ans = defaultdict(int)
        
        for domain in cpdomains:
            domain = domain.replace('.', ' ')
            temp = domain.split(' ')
            
            if len(temp) == 4:
                ans[temp[3]] += int(temp[0])

            ans['.'.join(temp[1:])] += int(temp[0])
            ans['.'.join(temp[2:])] += int(temp[0])
        
        
        res = [str(value)+ ' ' + key for key, value in ans.items()]
        return res
        
        
        
        
        
            
            
            
            
        