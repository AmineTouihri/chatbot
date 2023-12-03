class Page :
    Posts=[]
    def __init__(self,page_id) -> None:
        
        self.page_id=page_id



    def to_dict(self):

        return {
                "page_id":str(self.page_id),
                "posts":self.Posts
        }