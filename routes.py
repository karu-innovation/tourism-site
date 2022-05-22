from flask import render_template,request
from models import *
from main import app

@app.route('/')
def home():
    sites=Site.query.all()
   
    

    return render_template("index.html",sites=sites)


@app.route("/add/<type>",methods=['POST','GET'])
def add(type):
    if request.method == 'POST':
        name=request.form['name']
        location=request.form['location']
        site=request.form['site']
        price=request.form['price']
        description=request.form['description']

        if type=="site":
            site=Site(name,location,description,float(price))
            db.session.add(site)
            db.session.commit()

        elif type=="travel":
            travel=Travel(name,location,site,description,price)
            db.session.add(travel)
            db.session.commit()

        elif type=="hotel":
            hotel=Hotel(name,location,site,description,price)
            db.session.add(hotel)
            db.session.commit()



        return render_template('add.html',message=f"successfully added {type}")

    return render_template('add.html')

@app.route("/login")
def login():

    return render_template("login.html")

@app.route("/site/<id>")
def sitePage(id):
    site=Site.query.filter_by(id=id).first()
    hotels=Hotel.query.filter_by(site=site.name).all()
    travels=Travel.query.filter_by(site=site.name).all()

    return render_template("site.html",site=site, hotels=hotels,travels=travels)