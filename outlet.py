from flask import render_template, session, flash, request, redirect, url_for, Blueprint

outlet = Blueprint('outlet', __name__)

from app import mysql
@outlet.route('/outletdetail', methods=['GET','POST'])
def outletdetail():
    outlet_id = session['outlet_id']
    cur = mysql.connection.cursor()
    output = cur.execute("select token_no, placed_time, order_status from orders where (outlet_id=%s and order_status = %s) order by placed_time asc;", (outlet_id, "queued",))
    output = cur.fetchall()
    tokens = []
    for token_detail in output:
        temp = {
            'token_no': token_detail[0],
            'placed_time': token_detail[1],
            'order_status': token_detail[2]
        }
        tokens.append(temp)
    output = cur.execute("select token_no, placed_time, order_status from orders where (outlet_id=%s and order_status = %s) order by placed_time asc;", (outlet_id, "prepared",))
    output = cur.fetchall()
    for token_detail in output:
        temp = {
            'token_no': token_detail[0],
            'placed_time': token_detail[1],
            'order_status': token_detail[2]
        }
        tokens.append(temp)
    return render_template('outlets/outletdetail.html', tokens=tokens)