class AlbumTranform:
    def __init__(self,conn,query):
        self.conn = conn
        self.query = query
        # self.table = table
        self.fetch = {}
    
    
    def fetchData(self):
        self.fetch = f"""
        {self.query}
        """
        
    def showResult(self):
        return self.fetch