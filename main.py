import pandas as pd


df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        """Booking the hotel and make the availability as no"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False) # index = false doesnt adds new row

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object.name

    def generate_ticket(self):
        content = f"""
        Thank you for the reservation.
        Here are your booking data:
        Name: {self.customer_name}
        Hotel Name: {self.hotel_object}
"""
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, cvc, holder):
        card_data = {'number':self.number, 'expiration': expiration,
                     'holder':holder, 'cvc': cvc}
        if card_data in df_cards:
            return True
        else:
            return False




print(df)
hotel_ID = input('Enter the hotel id:')
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = CreditCard(number='1234')
    if credit_card.validate(expiration='12/26', cvc='123',
                            holder='JOHN SMITH'):
        hotel.book()
        name = input('Enter your name:')
        reserve_ticket = ReservationTicket(name, hotel)
        print(reserve_ticket.generate_ticket())
else:
    print("Hotel not available")
