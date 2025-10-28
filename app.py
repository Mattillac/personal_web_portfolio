from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')


@app.route('/touppercase', methods=['GET', 'POST'])
def uppercut():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/areaofcircle', methods=['GET', 'POST'])
def area_circ():
    result = None
    if request.method == 'POST':
        radius = float(request.form.get('Radius', ''))
        result = math.pi * (radius ** 2)
    return render_template('areaofcircle.html', result=result)


@app.route('/areaoftriangle', methods=['GET', 'POST'])
def area_tri():
    result = None
    if request.method == 'POST':
        base = float(request.form.get('Base', ''))
        height = float(request.form.get('Height', ''))
        result = 1/2 * base * height
    return render_template('areaoftriangle.html', result=result)


@app.route('/contact')
def contact():
    return render_template('contacts.html')

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def is_operand(ch):
    return ch.isalpha() or ch.isdigit()

def infix_to_postfix(expression):
    stack = []  
    output = ''

    for ch in expression:
        if is_operand(ch):
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else: 
            while stack and precedence(stack[-1]) >= precedence(ch):
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output


@app.route('/finixtopostfix', methods=['GET', 'POST'])
def count():
    result = ""
    if request.method == 'POST':
        infix_exp = request.form['expression']
        result = infix_to_postfix(infix_exp)
    return render_template('finixtopostfix.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
