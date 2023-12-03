from app.controllers.page import pageExists,getPageByPageId

from datetime import datetime
import os

from flask import request,current_app

from app.models.post import Post

from app.db.mongodb_connection import pages_collection


def createPost(pageId):

    upload_files=request.files.getlist('photos')
    description=request.form.get('description')
    
    
    filePaths=[]
    for file in upload_files:
        if file.filename!='':
            filePath=pageId+'_'+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+file.filename
            
            filePaths.append(filePath)
            
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filePath))
    
    newPost=Post(description,filePaths)

            # next error to solve is that the new posts doesent insert into the table but is saved into the server



    if (getPageByPageId(pageId)!=-1):

        page= pages_collection.update_one({
            "page_id":pageId},{
            "$push":{"posts":newPost.to_dict()}
            })
        return 'files saved',200
    else:
        return "cant save files pages doesent exist",404


    
        
        

