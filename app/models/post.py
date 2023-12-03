class Post:
    def __init__(self,postDescription,postFilePathPhotos) -> None:
        self.postDescription=postDescription
        self.postPhotos=postFilePathPhotos


    def to_dict(self) :
        return {

            "postDescription":self.postDescription,
            "postPhotos":self.postPhotos

        }



    