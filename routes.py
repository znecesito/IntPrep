from flask import Flask
from flask import render_template, url_for, redirect
from linkedlist import Node, SLinkedList
from forms import AppendLinkedListForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '06f14846c771c66206878b8ed8bc9348'

# list.AtEnd("Monday")
# list.AtEnd("Tuesday")
# list.AtEnd("Wednesday")
list = SLinkedList()
@app.route("/", methods=['GET', 'POST'])
def home():
    append_form = AppendLinkedListForm()
    if append_form.validate_on_submit():
        dataval = append_form.data_val.data
        list.AtEnd(dataval)
        return redirect(url_for('home'))
    list.ListPrint()

    return render_template('index.html', append_form=append_form)

# @app.route("/append_node", methods=['POST'])
# def append_node():
#     return render_template('index.html', list=list)

if __name__ == '__main__':
    app.run(debug=True)
