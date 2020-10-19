# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from database_connectivity import CreateBooking, ListActiveBookings

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class SubmitBooking(Action):
    def name(self) -> Text:
        return "action_submit_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's check the booking details."
                                      "\nVolunteer visit date - {0},"
                                      " products you need - '{1}'\n"
                                      "Your details: address - {2},"
                                      " phone number - {3}.\nIs that correct?"
                                 .format(tracker.get_slot("date"),
                                         tracker.get_slot("products"),
                                         tracker.get_slot("location"),
                                         tracker.get_slot("phone_number")))

        return []


class MakeBooking(Action):
    def name(self) -> Text:
        return "action_make_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        CreateBooking(tracker.get_slot("location"),
                      tracker.get_slot("phone_number"),
                      tracker.get_slot("date"),
                      tracker.get_slot("products"))
        dispatcher.utter_message(text="Your booking has succesfully added!"
                                      " Our volunteer will contact you before his visit.")

        return []


class ListBookings(Action):
    def name(self) -> Text:
        return "action_list_active_bookings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        bookings = ListActiveBookings(tracker.get_slot("phone_number"))
        if len(bookings) != 0:
            dispatcher.utter_message(text="You have {0} active bookings: ".format(len(bookings)))
            for b in bookings:
                dispatcher.utter_message(text="Date: {0}".format(b))
        else:
            dispatcher.utter_message(text="You don't have any upcoming volunteer visits.")

        return []
