#server.py

from flask import Flask
import medicine

app=Flask(__name__)

@app.route('/yak',methods=['GET'])
def yak():
 medicine.movemotor()
 return 'WEK!' 

if __name__=='__main__':
 app.run(host='192.168.137.91',port=5000,debug=True)

