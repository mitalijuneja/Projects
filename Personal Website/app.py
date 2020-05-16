

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")



#start the server
if __name__ == "__main__":
    app.run()
    
    
    
"""
   #b1ded6 (light blue)
   #99d1ab (light green)
   #87c4b6 (dark blue)
   #e8a692 (orange)
   #eba7b0 (light pink)
   #de7896 (dark pink) 

"""
    
   