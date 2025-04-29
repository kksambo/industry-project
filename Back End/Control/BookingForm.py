from datetime import date

class BookingForm:
    def __init__(self, name: str, email: str, check_in_date: date, check_out_date: date, number_of_guests: int):
        self.name = name
        self.email = email
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.number_of_guests = number_of_guests

    def __repr__(self):
        return (f"BookingForm(name={self.name}, email={self.email}, "
                f"check_in_date={self.check_in_date}, check_out_date={self.check_out_date}, "
                f"number_of_guests={self.number_of_guests})")