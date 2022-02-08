class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total
        
    def __str__(self):
        return f'Invoice from {self.cilent} for {self.total}'
    
inv = Invoice('Google', 100)
print(str(inv))