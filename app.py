# # from crypt import methods
# from flask import Flask,render_template,request
# # from flask_sqlalchemy import SQLAlchemy




# app=Flask(__name__)
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# # app.config['SQLALCHEMY_DATABASW_URI']='postgres://ofkemipb:96vmMSmLRYKooViMoAiphJQi3kyhm_JA@satao.db.elephantsql.com/ofkemipb'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
# # # app.debug=True
# # db=SQLAlchemy(app)

# # class user(db.Model):
# #     # __tablename__='user'
# #     id=db.Column(db.Integer,primary_key=True)
# #     name=db.Column(db.String(80))

#     # def __init__(self,username):
#     #     self.username=username

#     # def __repr__(self):
#     #     return '<User %r>' % self.username


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/freeplan")
# def freeplan():
#     return render_template("freeplan.html")

# # @app.route("/form")
# # def register():
# #     if(request.method=='POST'):
# #         name = request.form.get('name')
# #         # email = request.form.get('email')
# #         entry = user(name=name)
# #         db.session.add(entry)
# #         db.session.commit()

# #     return render_template("form.html")


# @app.route('/hello')
# def hello():
#     return '<h2>Hello, World</h2>'

# if __name__=="__main__":
#     app.run(debug=True)












# from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,render_template,request



app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
# app.config['SECRET_KEY']='demokey'
# db=SQLAlchemy(app)

# class user(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/newsletter')
def newsletter():
    return render_template("newsletter.html")

@app.route('/freeplan.html')
def hello():
    return render_template("freeplan.html")

@app.route('/premiumworkoutstwo.html')
def premiumworkoutstwo():
    return render_template("premiumworkoutstwo.html")

@app.route('/secretpage')
def secretpage():
    return render_template("secretpage.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")



@app.route('/form', methods = ['GET', 'POST'])
def form():
    return render_template("form.html")



@app.route('/beginnerworkout')
def beginnerworkout():
    return render_template("BeginnerWorkout.html")


@app.route('/bmi')
def bmi():
    return render_template("bmi.html")




@app.route('/intermediate')
def intermediate():
    return render_template("IntermediateWorkout.html")



@app.route('/advanceworkout')
def advanceworkout():
    return render_template("advanceWorkout.html")



if __name__=="__main__":
    app.run(debug=True)























# from crypt import methods
# from flask import Flask ,render_template,request
# from flask_sqlalchemy import SQLAlchemy

# # from flask_sqlalchemy import SQLAlchemy

# app=Flask(__name__)
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['SQLALCHEMY_DATABASW_URI']='postgres://ofkemipb:96vmMSmLRYKooViMoAiphJQi3kyhm_JA@satao.db.elephantsql.com/ofkemipb'
# app.debug=True

# db=SQLAlchemy(app)

# class user(db.Model):
#     __tablename__='user'
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(80))

#     def __init__(self,username):
#         self.username=username

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/freeplan.html')
# def hello():
#     return render_template("freeplan.html")

# @app.route('/form.html', methods = ['GET', 'POST'])
# def form():
#     if(request.method=='POST'):
#         '''Add entry to the database'''
#         username = request.form.get('name')
#         entry = user(username=username)
#         db.session.add(entry)
#         db.session.commit()
#     return render_template("form.html")

# if __name__=="__main__":
#     app.run(debug=True)