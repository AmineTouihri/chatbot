from flask import Flask,render_template,request

# from db.mongodb_connection import pages_collection

from app.routes.page_route import page_bp

from datetime import datetime
# from models.post import Post

# from controllers.page import createPage

# from controllers.imageComparison import compareTwoImages 
import cv2
import os   



app=Flask(__name__)




UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

userId=2

app.register_blueprint(page_bp)


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)




@app.route("/")
def landPage():   
    return render_template('./index.html',userId=userId)


@app.route("/webhook", methods=['GET'])
def fbverify():
    print(request)
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")=="anystring":
            return "Verification token missmatch", 403

        print(request.args.get("hub.challenge"))
        return request.args.get("hub.challenge"),200
    return "Hello world", 200


@app.route("/webhook",methods=['POST'])
def webhook_handle():
    output = request.get_json()
    print(output)
    return 'ok'




if __name__== '__main__':
    app.run()


PAGE_ACCESS_TOKEN="EAAMfE8HUFEUBO4txJA9MYXrZAZCthffZAIZBFxckQ8aUIz66H4skDBc5bW2wrqOLhHxZBdcH26hguzakwqk04Skh4OabZAZCksew3GVrlvFJNrhvrC7jgHOeSqbEVrCrX45RRcwZB6Kjg9VH90Xg14IfdZCxNzrO3NLHfzW9W7QOfgEjGYsZAZB5PZAPFmZChvUJaPLgP"

API= "https://graph.facebook.com/LATEST-API-VERSION/me/messages?access_token="+PAGE_ACCESS_TOKEN


CONNECTION_STRING="mongodb+srv://mohamedaminetouihri9:OUGCjVq1Kg6OAfrM@cluster0.iym5nvs.mongodb.net/?retryWrites=true&w=majority"



