import cv2

from app.db.mongodb_connection import pages_collection

from app.controllers.page import getPageByPageId

def compareTwoImages(pageId):

    orb=cv2.ORB.create()

    imagesPath=[]

    page=getPageByPageId(pageId)

    img1=cv2.imread('img3.jpg')
    kp_b,desc_b=orb.detectAndCompute(img1,None)

    if (page==-1):
        return "page not found",404 
    else:

        pagePosts=page['posts']
        for post in reversed(pagePosts):
            imagesPath=post['postPhotos']
            for image in imagesPath :
                img=cv2.imread('images/{}'.format(image))
                kp_a,desc_a=orb.detectAndCompute(img,None)
                bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
                matches=bf.match(desc_a,desc_b)
                similar_regions=[i for i in matches if i.distance < 50 ]
                print(image)
                print(len(similar_regions)/len(matches))
                if len(matches)==0:
                    continue
                elif len(similar_regions)/len(matches)==0 :
                    continue
                elif len(similar_regions)/len(matches)>0.01 :
                    print(len(similar_regions)/len(matches))
                    return (post['postDescription'])


       
        return "not muches no status for this image",404