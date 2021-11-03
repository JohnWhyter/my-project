from flask import Flask, request, render_template

app = Flask(__name__)

def int_to_rome(number): 
           
        n = int(number)
        b = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        c = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        d= []
        for i in range(len(b)):
            count = int((n/b[i]))
            d.append(count*c[i])
            n -= count * b[i]
        return "".join(d)


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        number = None             
        try:
            number = float(request.form["number"])
        except:
            errors += " ".format(request.form["number"])
                        
        if number is not None and 0 < number < 4000:
            number_roman = int_to_rome(number)
            number_decimal = number
            return render_template ("result.html", number_roman=number_roman, number_decimal=number, developer_name = "John")    
        else:
            errors += " {!r} Not Valid! Please enter a number between 1 and 3999, inclusively..\n".format(request.form["number"])


    return render_template ("index.html", errors=errors, developer_name = "John")
    
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)