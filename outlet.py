from flask import flash, render_template, session, flash, request, redirect, url_for, Blueprint
import datetime
outlet = Blueprint('outlet', __name__)

from app import mysql
@outlet.route('/outletdetail', methods=['GET','POST'])
def outletdetail():
    if request.method == "POST" and 'neworder' in request.form:
        date = datetime.date.today()
        cur = mysql.connection.cursor()
        cur.execute("select token_no from orders where placed_time>=%s order by placed_time desc;", (date,))
        token_no = cur.fetchone()
        if token_no:
            token = token_no[0] + 1
        else:
            token = 1
        placed_time = datetime.datetime.today()
        outlet_id = session['outlet_id']
        cur.execute("insert into food_token.orders(order_status, token_no, outlet_id, placed_time) values (%s, %s, %s, %s)", ("queued", token, outlet_id, placed_time,))
        mysql.connection.commit()
        cur.close()

    elif request.method == "POST":
        prepare_id = request.form.get("prepare_id")
        collect_id = request.form.get("collect_id")
        date = datetime.datetime.today()
        cur = mysql.connection.cursor()
        if prepare_id:
            order_id = prepare_id
            order_status = "prepared"
            cur.execute("update orders set prepared_time=%s where order_id=%s", (date, prepare_id,))
            
        elif collect_id:
            order_id = collect_id
            order_status = "collected"
            cur.execute("update orders set collected_time=%s where order_id=%s", (date, collect_id,))
        try:
            cur.execute("update orders set order_status=%s where order_id=%s", (order_status, order_id,))
            mysql.connection.commit()
            cur.close()
        except:
            flash("update failed of order")
    
    outlet_id = session['outlet_id']
    cur = mysql.connection.cursor()
    output = cur.execute("select token_no, placed_time, order_status, order_id, prepared_time from orders where (outlet_id=%s and order_status = %s) order by placed_time asc;", (outlet_id, "queued",))
    output = cur.fetchall()
    tokens = []
    for token_detail in output:
        temp = {
            'token_no': token_detail[0],
            'placed_time': token_detail[1],
            'order_status': token_detail[2],
            'id': token_detail[3], 
            'prepared_time': token_detail[4],
        }
        tokens.append(temp)
    output = cur.execute("select token_no, placed_time, order_status, order_id, prepared_time from orders where (outlet_id=%s and order_status = %s) order by placed_time asc;", (outlet_id, "prepared",))
    output = cur.fetchall()
    for token_detail in output:
        temp = {
            'token_no': token_detail[0],
            'placed_time': token_detail[1],
            'order_status': token_detail[2],
            'id': token_detail[3],
            'prepared_time': token_detail[4]
        }
        tokens.append(temp)
    return render_template('outlets/outletdetail.html', tokens=tokens)