from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging
import pymongo

logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

    
@app.route("/",methods = ['GET' , 'POST'])
def home_page():
    return render_template('index.html') 

@app.route("/review", methods =['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            #extracting flipkart search url
            searchstring = request.form['content'].replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q="+ searchstring
            

            urlclient = uReq(flipkart_url)
            flipkart_page = urlclient.read()
            urlclient.close()
                
            #extracting html code
            flipkart_html = bs(flipkart_page,'html.parser')
            

            #extracting 1st product
            bigbox = flipkart_html.findAll("div",{"class" : "_1AtVbE col-12-12"})
            del bigbox[0:3]
            box = bigbox[0]
            
            #product link
            product_link = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodReq = requests.get(product_link)
            prodReq.encoding = 'utf-8'
            product_html = bs(prodReq.text,"html.parser")
            

            #extracting product reviews
            comment_box = product_html.find_all("div",{"class" : "_16PBlm"})
            

            #creating csv file to store reviews
            filename = searchstring + ".csv"
            fw = open(filename, "w")
            headers = "Product , Customer Name , Rating , Heading, Comment \n"
            fw.write(headers)
            

            #storing reviews
            reviews = [] 

            for i in comment_box:
                name = "Verified CUSTOMER"
                try:
                    #name.encode(encoding="utf-8")
                    name = i.div.div.find_all("p" , {"class" : "_2sc7ZR _2V5EHH"})[0].text
                    
                except:
                    logging.info("name")


                try:
                    rating = i.div.div.div.div.text
                    
                except:
                    rating = "No Rating"
                    logging.info(rating)


                try :
                    #commentHead . encode(encoding= ' utf-8 ' )
                    comment_head = i.div.div.div.p.text
                    
                except:
                    comment_head = 'No Comment Heading'
                    logging.info(comment_head)


                try :
                    com_tag = i.div.div.find_all( "div" ,{'class': ""})
                    #custComment . encode(encoding= ' utf-8 ' )
                    custComment = com_tag[0].div.text
                    
                except Exception as e:
                    logging.info(e)
                
                
                mydict = {"Product" : searchstring, "Name" : name , "Rating" : rating, "Heading" : comment_head, "Comment" : custComment}

                reviews.append(mydict)

                print("REVIEWS APPENDED done")

            logging.info("Log my final result {}".format(reviews))
            return render_template("result.html",reviews = reviews[0:(len(reviews)-1)])

        except Exception as e:
            logging.info(e)
            return "something is wrong"
    #render_templat('result.html')
    
    else:
        return render_template("index.html")    


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port="5000")