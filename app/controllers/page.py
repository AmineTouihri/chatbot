from app.db.mongodb_connection import pages_collection

from app.models.page import Page

def pageExists(id):

    page=pages_collection.find_one({"page_id":id})

    if page :
        return -1
        
    return page

def getPageByPageId(id):
    page=pages_collection.find_one({"page_id":id})
    if page :
        return page 
    return -1



def createPage(id): 
    if(pageExists(id)):
        return -1
    else:
        page=Page(id)
        return pages_collection.insert_one(page.to_dict())