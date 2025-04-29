from flask import Flask, request, render_template
from datetime import datetime
from BookingForm import BookingForm
from place import Place

app = Flask(__name__)

@app.route('/')
def index():
    place=Place('mbuzini','this is a description')
    return place.lse()


def tumi():
    return 'tumi'


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        check_in_date = datetime.strptime(request.form['check_in_date'], '%Y-%m-%d').date()
        check_out_date = datetime.strptime(request.form['check_out_date'], '%Y-%m-%d').date()
        number_of_guests = int(request.form['number_of_guests'])

        # Create a BookingForm instance
        booking_form = BookingForm(name, email, check_in_date, check_out_date, number_of_guests)

        # For now, just print the booking form
        print(booking_form)

        

        return "Booking submitted successfully!"

    return "printing the else part"

if __name__ == '__main__':
    app.run(debug=True)



