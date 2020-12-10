from flask import Flask
from flask import render_template, url_for, redirect, session
from linkedlist import Node, SLinkedList
from forms import AppendLinkedListForm
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = '06f14846c771c66206878b8ed8bc9348'
dict={}

@app.route("/")
def home():
    dict_key = ''
    if (session.get("demo") == None):
        session["demo"] = "value"
        dict_key = str(random.random())
        list_value = SLinkedList()
        dict[dict_key] = list_value
        print(dict)

    return render_template('index.html', dict_key=dict_key)

@app.route("/linked-list/<unique_list_key>", methods=['GET', 'POST'])
def linked_list(unique_list_key):
    list = dict[unique_list_key]
    append_form = AppendLinkedListForm()
    if append_form.validate_on_submit():
        dataval = append_form.data_val.data
        list.AtEnd(dataval)
        dict[unique_list_key] = list
        list.ListPrint()
        return redirect(url_for('linked_list', unique_list_key=unique_list_key))

    return render_template('linkedlist.html', append_form=append_form)

if __name__ == '__main__':
    app.run(debug=True)
