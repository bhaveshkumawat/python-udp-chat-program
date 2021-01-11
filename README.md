# python-udp-chat-program
This is a basic chat program developed with the help udp protocol.


First the program asks for its own system ip and port number to bind the socket to receive any data.
Then it asks for the other system ip and port on which the same service is running to send any data.



This application is capable of simultaneously reading or sending data , this feature is achieved through the concept of multi-threading . One thread is receiving while the other thread is sending data.
The application automatically stops when both the sides write or send an exit message.
