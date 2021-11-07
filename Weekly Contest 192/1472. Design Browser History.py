class BrowserHistory:

    def __init__(self, homepage: str):
        self.b_history = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        if self.cur == len(self.b_history) -1:
            pass
        else:
            self.b_history = self.b_history[:self.cur+1]
            
        self.b_history.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur -= steps
        self.cur = max(0, self.cur)
        return self.b_history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur += steps
        self.cur = min(self.cur, len(self.b_history) - 1)
        return self.b_history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)