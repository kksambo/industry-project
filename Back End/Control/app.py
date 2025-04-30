from flask import Flask, request, render_template
from datetime import datetime
from BookingForm import BookingForm
from place import Place
from Traveller import Traveller
from TripInformation import TripInformation

app = Flask(__name__)


@app.route('/createTravellers' ,methods=['POST'])
def createTravellers():
    traveller=Traveller('Asimbonge','Mzizi','asimbongenhlakanipho@gmail.com','Computer@25')

    return traveller.__repr__()

@app.route('/getTravellers',methods=['GET'])
def getTravellers():
        return 'lisfOfTravellers'


@app.route('/createTripInformation',methods={'POST'})
def createTripInformation():
     tripInformation=TripInformation('buses','B&Bs','26','do not drink and drive')
     
     
     return tripInformation.__repr__()

@app.route('/getTripInformation',methods={'GET'})
def getTripInformation():
     
     return 'fcf'

     
     

if __name__ == '__main__':
    app.run(debug=True)



