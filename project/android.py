import os
from flask import *
from werkzeug.utils import secure_filename
from src.dbconnector import *

app=Flask(__name__)

@app.route("/loginnew",methods=['post'])
def loginnew():
    username=request.form['Username']
    password=request.form['Password']
    qry="select * from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return jsonify({"task":"invalid"})
    else:
        return jsonify({'task': "valid", 'id': res[0]})

@app.route("/register",methods=['post'])
def register():
    firstname=request.form['First Name']
    lastname=request.form['Last Name']
    dob=request.form['Date of Birth']
    place=request.form['Place']
    post=request.form['Post']
    pin=request.form['Pin']
    gender=request.form['Gender']
    phone=request.form['Phone']
    email=request.form['email']
    username=request.form['Username']
    password=request.form['Password']
    qry="insert into login values(NULL,%s,%s,'user')"
    val=(username,password)
    print(val)
    id=iud(qry,val)
    qry1="insert into user values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),firstname,lastname,dob,place,post,pin,gender,phone,email)
    iud(qry1,val1)
    return jsonify({"task":"success"})

@app.route('/Add_and_manage_playlist',methods=['post'])
def Add_and_manage_playlist():
    type=request.form['type']
    print(type)
    qry="select * from playlist where music = %s"
    val=type
    res=androidselectall(qry,val)
    print(res)
    return jsonify(res)





@app.route('/search',methods=['post'])
def search():
    type=request.form['select']

    qry="select * from playlist where `user_id`=%s and type=%s"
    res=androidselectall(qry,type)
    return jsonify(res)



@app.route('/edit_playlist')
def edit_playlist():
    id=request.args.get("id")
    qry="SELECT * FROM `playlist` WHERE `pid`=%s"
    val=(id)
    session['id']=id
    res=selectone(qry,val)
    return jsonify(res)

@app.route('/update',methods=['post'])
def update():
    try:
        type=request.form['type']
        song=request.files['file']
        fname=secure_filename(song.filename)
        song.save(os.path.join('static/song/',fname))
        des=request.form['des']
        qry="update playlist set music=%s,type%s,description=%s where pid=%s"
        val=(fname,type,des,session['id'])
        iud(qry,val)
        return '''<script> alert("Updated");window.location="/Add_and_manage_playlist" </script>'''
    except:
        type = request.form['type']

        des = request.form['des']
        qry = "update playlist set type=%s,description=%s where pid=%s"
        val = ( type, des,session['id'])
        iud(qry, val)
        return jsonify({"task":"success"})



@app.route('/most_played_song',methods=['post'])
def most_played_song():
    qry = "SELECT music.singer,year,sname,file,count(*) as mp FROM music JOIN most_played ON music.m_id = most_played.music_id group by most_played.music_id order by mp desc limit 10"


    res=androidselectallnew(qry)
    print(res)
    return jsonify(res)

@app.route('/Feedback',methods=['post'])
def Feedback():
    userid=request.form['lid']
    feedback=request.form['Feedback']
    qry="insert into feedback values(null,%s,%s,curdate())"
    val=(userid,feedback)
    iud(qry,val)
    return jsonify({"task":"success"})

@app.route('/Select_Emotions',methods=['post'])
def Select_Emotions():
    qry="SELECT DISTINCT type FROM playlist"
    res = androidselectallnew(qry)
    print(res)
    return jsonify(res)




@app.route('/cosine_similarity',methods = ['post'])
# @login_required
def cosine_similarity():
    print(request.form)
    lid=request.form['lid']
    lang=request.form['lang']
    print(lang)

    res = androidselectallnew("select * from music where language = '"+lang+"' and  m_id not in (select music_id from most_played WHERE `user_id`="+str(lid)+")")
    # res = select("select * from music where language = '"+lang+"' ")

    print(res,"+++++++++++++++++++++++++++")
    res1 = androidselectallnew("select count(*)as e,music_id  from most_played  where user_id = '"+lid+"' and   music_id in(select m_id from music where language='"+lang+"')")
    print(res,res1)

    print('llllllllllllllllll',lid,'rrrrrrrrrrrrrrrrr',res1)
    if len(res1)>0:
        print(res1[0]['music_id'])
        # qry="select type from mtype where muid=%s"
        # res=selectone(qry,res1[0]['music_id'])
        # qry = "select * from mfcc where music_id in (select m_id from music where language = '"+lang+"' and  m_id not in (select music_id from most_played)) and m_id in(select muid from mtype where type="+str(res[0])+")"
        qry = "select * from mfcc where music_id in (select m_id from music where language = '"+lang+"' and  m_id not in (select music_id from most_played WHERE `user_id`="+str(lid)+") )"
        res = select(qry)

        lst1 = []

        for i in res:
            # print(i)
            lst = []
            lst.append(float(i[2]))
            lst.append(float(i[3]))
            lst.append(float(i[4]))
            lst.append(float(i[5]))
            lst.append(float(i[6]))
            # print(lst)
            # lstt = ("[{0}]".format(', '.join(map(str, lst))))
            row=[]
            row.append(lst)
            row.append(i[1])
            lst1.append(row)
        lstt1 =lst1# ("[{0}]".format(', '.join(map(str, lst1))))
        print(lstt1)
        print(res)
        qry = "select * from mfcc where music_id=%s"
        print(qry,res1[0]['music_id'])
        res = selectall(qry,res1[0]['music_id'])
        print(qry,res1[0]['music_id'])
        print(res1,"=====================+++++++++")
        lstt1 = lst1  # ("[{0}]".format(', '.join(map(str, lst1))))
        print(lstt1)
        lst2 = []

        for i in res:
            # print(i)
            lst = []
            lst.append(float(i[2]))
            lst.append(float(i[3]))
            lst.append(float(i[4]))
            lst.append(float(i[5]))
            lst.append(float(i[6]))
            # print(lst)
            # lstt = ("[{0}]".format(', '.join(map(str, lst))))

            lst2.append(lst)

        # # Example of getting neighbors for an instance
        from math import sqrt

        # calculate the Euclidean distance between two vectors
        def euclidean_distance(row1, row2):
            distance = 0.0
            for i in range(len(row1) - 1):
                distance += (row1[i] - row2[i]) ** 2
            return sqrt(distance)

        # Locate the most similar neighbors
        def get_neighbors(train, test_row, num_neighbors):
            distances = list()
            print(train)
            for train_row in train:
                print(train_row,"=======================")
                dist = euclidean_distance(train_row[0], test_row)
                distances.append((train_row[1], dist))
            print(distances)
            print("++++++++++++++++++++++++++++++++++++++++")
            distances.sort(key=lambda tup: tup[1])
            # results = [i[1] for i in sorted(distances)[:num_neighbors]]
            neighbors = list()
            for i in range(num_neighbors):
                try:
                    neighbors.append(distances[i][0])
                except:
                    pass
            return neighbors

        # Test distance function
        dataset = lstt1
        print(type(dataset))
        print(lst2,"++++++++++++++++=")
        neighbors = get_neighbors(dataset, lst2[0], 3)

        row=[]
        for neighbor in neighbors:
            row.append(str(neighbor))
            print(neighbor)
        rr=','.join(row)
        print(rr,"+++++++++++")
        qry="select * from music where m_id in("+rr+")"
        res=androidselectallnew(qry)
        print("qqqqqqqqqqqqqqqqqqqqqqqqq",res)
        return jsonify(res)
    else:
        return jsonify([])
#
#

@app.route('/search_by_year',methods=['post'])
def search_by_year():
    year = request.form['year']
    qry="select * from music where year = '"+year+"'"
    res=androidselectallnew(qry)
    print(res)
    return jsonify(res)


@app.route('/search_by_language',methods=['post'])
def search_by_language():
    year = request.form['year']
    qry="select * from music where language = '"+year+"'"
    res=androidselectallnew(qry)
    print(res)
    return jsonify(res)


@app.route('/search_by_artist',methods=['post'])
def search_by_artist():
    year = request.form['year']
    qry="select * from music where singer = '"+year+"'"
    res=androidselectallnew(qry)
    print(res)
    return jsonify(res)




@app.route('/Add_mp',methods=['post'])
def Add_mp():

    mid=request.form['mid']
    lid=request.form['lid']
    qry="insert into most_played values(null,%s,%s)"
    val=(mid,lid)
    iud(qry,val)
    return jsonify({"task": "success"})

#adding songs to most played table

app.run(host="0.0.0.0",port=5000)
