import psycopg2
from dateparser import parse
from datetime import date, datetime, timedelta


def __next_weekday(weekday):
    today = date.today()
    days_diff = (weekday - today.weekday()) % 7
    return today + timedelta(days_diff)

def CreateBooking(location, phone_number, date, details):
    connection = None
    date = date.lower()
    weekdayDict = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    if 'next' in date or 'this' in date:
        weekday = date.split()[1]
        date = __next_weekday(weekdayDict[weekday])
    else:
        date = parse(date).date()

    try:
        connection = psycopg2.connect(host="localhost", database="corona_help", user="postgres", password="password")
        cursor = connection.cursor()
        sql_parameterized_query =\
            "insert into bookings (c_location, c_phone_number, b_date, details) values(%s, %s, %s, %s )"
        values = (location, phone_number, date, details)
        cursor.execute(sql_parameterized_query, values)
        connection.commit()
    except Exception as e:
        print("exception raised", e)
    finally:
        if connection is not None:
            connection.close()

    return "True"

def ListActiveBookings(phone_number):
    bookings_list = []
    connection = None
    today = date.today()
    try:
        connection = psycopg2.connect(host="localhost", database="corona_help", user="postgres", password="password")
        cursor = connection.cursor()
        sql_parameterized_query =\
            "select b_date from bookings where c_phone_number = %s and b_date >= %s"
        cursor.execute(sql_parameterized_query, (phone_number, today))
        # for row in cursor:
        #     bookings_list.append(row)

        bookings_list = [row[0] for row in cursor.fetchall()]
    except Exception as ex:
        print("Exception Occurred", ex)
    finally:
        if connection is not None:
            connection.close()

    return bookings_list
