from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Crime_Rate_Map2.html")
    
@app.route("/Map2")
def Map2():
    return render_template("Crime_Rate_Map.html")

@app.route("/Map3")
def Map3():
    return render_template("Los_angeles_HousePrices_map.html")
    
if __name__ == "__main__":
    app.run(debug=True)