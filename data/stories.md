## happy path
* greet
    - utter_greet
* affirm
    - utter_when
* when{"date": "next friday"}
    - slot{"date": "next friday"}
    - utter_what
* what{"products": "food"}
    - slot{"products": "food"}
    - utter_location
* location{"location":"Moscow, Pushkina 30, 47"}
    - slot{"location":"Moscow, Pushkina 30, 47"}
    - utter_phone_number
* phone_number{"phone_number":"88005553535"}
    - slot{"phone_number":"88005553535"}
    - action_submit_booking
* affirm
    - action_make_booking
    - utter_thank_you
## sad path
* greet
  - utter_greet
* deny
  - utter_sorry

## list bookings path
* list_bookings
  - utter_find_booking
* phone_number{"phone_number":"88005553535"}
  - slot{"phone_number":"88005553535"}
  - action_list_active_bookings

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
