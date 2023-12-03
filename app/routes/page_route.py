from flask import Blueprint

from app.controllers.page import createPage

from app.controllers.post import createPost

from app.controllers.imageComparison import compareTwoImages


page_bp =Blueprint('page',__name__)

@page_bp.route('/createNewPage',methods=['GET'])
def createNewPage():
      if  createPage(2)==-1:
            return "page exist change creadantials to create new one",401
      else:
            return "page created !",200

@page_bp.route('/createPost/<pageId>',methods=['POST'])
def createOnePost(pageId):
      return  createPost(pageId)


@page_bp.route('/compareImages/<pageId>',methods=['GET'])

def compareImages(pageId):
      return compareTwoImages(pageId)







    