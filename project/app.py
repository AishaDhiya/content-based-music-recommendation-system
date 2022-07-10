from flask import *
from werkzeug.utils import secure_filename
import os

from _thread import start_new_thread

import librosa
import pandas
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import csv
import os
from datetime import datetime
app=Flask(__name__)
app.secret_key="aaa"
from src.dbconnector import *

import functools
def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return redirect ("/")
        return func()
    return secure_function

@app.route("/logout")
# @login_required

def logout():
    session.clear()
    return render_template("login.html")

@app.route('/')
def Login():
    return render_template('Login.html')

@app.route("/loginnew",methods=['post'])
def loginnew():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script> alert("Invalid");window.location="/" </script>'''
    elif res[3]=="admin":
        session['lid']=res[0]
        return '''<script> alert("Success");window.location="/Homepage" </script>'''
    else:
        return '''<script> alert("Unknown user");window.location="/" </script>'''







@app.route('/Homepage')
def Homepage():
    return render_template('Homepage.html')


@app.route('/Add_playlist',methods=['post'])
@login_required
def Add_playlist():
    return redirect('/admin_add__song')

@app.route('/edit_playlist')
def edit_playlist():
    id=request.args.get("id")
    qry="SELECT * FROM `playlist` WHERE `pid`=%s"
    val=(id)
    session['id']=id
    res=selectone(qry,val)
    return render_template('edit playlist.html',data=res)

@app.route('/update',methods=['post'])
def update():
    try:
        type=request.form['select']
        song=request.files['file']
        fname=secure_filename(song.filename)
        song.save(os.path.join('static/song/',fname))
        des=request.form['textarea']
        qry="update playlist set music=%s,type%s,description=%s where pid=%s"
        val=(fname,type,des,session['id'])
        iud(qry,val)
        return '''<script> alert("Updated");window.location="/Add_and_manage_playlist" </script>'''
    except:
        type = request.form['select']

        des = request.form['textarea']
        qry = "update playlist set type=%s,description=%s where pid=%s"
        val = ( type, des,session['id'])
        iud(qry, val)
        return '''<script> alert("Updated");window.location="/Add_and_manage_playlist"</script>'''




@app.route('/Add_playlist1',methods=['post'])
def Add_playlist1():
    type=request.form['select']
    song=request.files['file']
    fname=secure_filename(song.filename)
    song.save(os.path.join('static/song/',fname))
    des=request.form['textarea']
    qry="insert into playlist values(NULL,0,%s,%s,%s,curdate())"
    val=(fname,type,des)
    iud(qry,val)
    return redirect('/Add_and_manage_playlist')



@app.route('/search',methods=['post'])
def search():
    type=request.form['select']
    # qry="select * from playlist where `user_id`=0 and type=%s"
    qry="select * from music where language=%s"
    res=selectall(qry,type)
    print(res,"========")
    return render_template('Add and manage playlist.html',val=res)

@app.route('/delete')
def delete():
    id=request.args.get('id')
    qry = "delete from music where m_id=%s"
    val=str(id)
    iud(qry,val)
    return  '''<script>alert("deleted");window.location="/Add_and_manage_playlist" </script>'''


@app.route('/Add_and_manage_playlist')
def Add_and_manage_playlist():
    return render_template('Add and manage playlist.html')

@app.route('/Feedback')
@login_required
def Fedback():
    qry="SELECT user.fname,user.lname,feedback.* FROM USER JOIN feedback ON user.lid=feedback.user_id"
    res=select(qry)
    return render_template('Feedback.html',val=res)

@app.route('/most_played_song')
@login_required
def most_played_song():
    qry="SELECT music.singer,year,sname,count(*) as mp FROM music JOIN most_played ON music.m_id = most_played.music_id group by most_played.music_id order by mp desc limit 10"
    res=select(qry)
    return render_template('most played song.html',val=res)

@app.route('/view_users')
@login_required
def view_users():
    qry="select * from user"
    res=select(qry)
    return render_template('view users.html',val=res)




@app.route('/admin_add__song',methods = ['get','post'])
@login_required
def admin_add__song():
    if request.method == "POST":
        lag = request.form['select']
        singer = request.form['singer']
        year = request.form['year']
        music = request.files['file']

        ff = secure_filename(music.filename)


        music.save(os.path.join('static\\music\\', ff))


        fn=datetime.now().strftime("%Y%m%d%H%M%S")+".wav"

        os.system('ffmpeg -i static\\music\\' + ff + ' static\\music\\' + fn )
        path = r'static/music/'+fn

        # tyid=predict(r'static/music/'+fn)
        aa = []
        y, sr = librosa.load(path, mono=True)
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)



        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        # mfcc = librosa.feature.mfcc(y=y, sr=sr)
        # to_append = str(np.mean(chroma_stft)) + " " + str(np.mean(spec_cent)) + " " + str(np.mean(spec_bw)) + " " + str(
        #     np.mean(rolloff)) + " " + str(np.mean(zcr))

        aa.append(np.mean(chroma_stft))
        aa.append(np.mean(spec_cent))
        aa.append(np.mean(spec_bw))
        aa.append(np.mean(rolloff))
        aa.append(np.mean(zcr))

        print(aa)
        #
        # music.save(r"C:\Users\TOSHIBA\Desktop\Music Bee\Music player\src\static\music\\"+music.filename)
        # path = '/static/music/'+music.filename
        #
        #
        #
        n = music.filename
        n=n.split(".")
        print("wwwwwwwwwwwwwwwwwwwwwwwwwww",n[0])

        qry = "insert into music values(NULL,%s,%s,%s,%s,%s)"
        val = (lag, singer, year,path,n[0])
        res = iud(qry, val)

        qry1 = "insert into mfcc values(NULL,%s,%s,%s,%s,%s,%s)"
        val1 = (str(res), str(np.mean(chroma_stft)), str(np.mean(spec_cent)), str(np.mean(spec_bw)),str(np.mean(rolloff)),str(np.mean(zcr)))
        iud(qry1, val1)


        # return "OK"
    return render_template('add_song.html')



#
#
# @app.route('/cosine_similarity')
# # @login_required
# def cosine_similarity():
#     qry = "select * from mfcc"
#     res = select(qry)
#
#     lst1 = []
#
#     for i in res:
#         # print(i)
#         lst = []
#         lst.append(float(i[2]))
#         lst.append(float(i[3]))
#         lst.append(float(i[4]))
#         lst.append(float(i[5]))
#         lst.append(float(i[6]))
#         # print(lst)
#         # lstt = ("[{0}]".format(', '.join(map(str, lst))))
#         row=[]
#         row.append(lst)
#         row.append(i[1])
#         lst1.append(row)
#     lstt1 =lst1# ("[{0}]".format(', '.join(map(str, lst1))))
#     print(lstt1)
#
#
#
#     # # Example of getting neighbors for an instance
#     from math import sqrt
#
#     # calculate the Euclidean distance between two vectors
#     def euclidean_distance(row1, row2):
#         distance = 0.0
#         for i in range(len(row1) - 1):
#             distance += (row1[i] - row2[i]) ** 2
#         return sqrt(distance)
#
#     # Locate the most similar neighbors
#     def get_neighbors(train, test_row, num_neighbors):
#         distances = list()
#         print(train)
#         for train_row in train:
#             print(train_row,"=======================")
#             dist = euclidean_distance(train_row[0], test_row)
#             distances.append((train_row[1], dist))
#         print(distances)
#         print("++++++++++++++++++++++++++++++++++++++++")
#         distances.sort(key=lambda tup: tup[1])
#         # results = [i[1] for i in sorted(distances)[:num_neighbors]]
#         neighbors = list()
#         for i in range(num_neighbors):
#             neighbors.append(distances[i][0])
#         return neighbors
#
#     # Test distance function
#     dataset = lstt1
#     print(type(dataset))
#     neighbors = get_neighbors(dataset, dataset[0][0], 3)
#     for neighbor in neighbors:
#         print(neighbor)
#     #
#
#     return "OK"
#
#
#
#






app.run(debug=False)
