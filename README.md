# Covid Volunteer Chatbot
Rasa chatbot that can help you book a volunteer during pandemia.

Installation:
1) Rasa version 1.10.16
`pip install rasa=1.10.16`
2) Dateparser `pip install dateparser`
3) Postgresql https://www.postgresql.org/download/ used to write bookings data in `bookings` table (create_bookings_table.sql). Specify your database name/user/password in database_connectivity.

Run chatbot:
`rasa shell`

