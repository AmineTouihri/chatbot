class Post:
    def __init__(self,postDescription,postFilePathPhotos,postUrl="") -> None:
        self.postDescription=postDescription
        self.postPhotos=postFilePathPhotos
        self.postUrl=postUrl


    def to_dict(self) :
        return {

            "postDescription":self.postDescription,
            "postPhotos":self.postPhotos,
            "postUrl":self.postUrl

        }



    