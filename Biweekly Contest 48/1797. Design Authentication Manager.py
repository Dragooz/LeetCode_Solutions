class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.token_dict = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_dict[tokenId] = currentTime+self.time_to_live #id, cur, expired.

    def renew(self, tokenId: str, currentTime: int) -> None:
        get_val = self.token_dict.get(tokenId, 'notexist')
        if get_val != 'notexist':
            if currentTime >= get_val: #expired
                del self.token_dict[tokenId]
            else:
                self.token_dict[tokenId] = currentTime + self.time_to_live
            
    def countUnexpiredTokens(self, currentTime: int) -> int:
        
        temp = self.token_dict.copy()
        for key, val in self.token_dict.items():
            if val <= currentTime:
                del temp[key]
        self.token_dict = temp.copy()
        return len(self.token_dict)
    

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)