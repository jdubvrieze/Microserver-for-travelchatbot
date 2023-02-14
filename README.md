# Microserver-for-travelchatbot
This is a microserver for my partner's travelchatbot software.
The microserver takes a request for a random city and state and returns a random city state as a list as a json file from the list of the top 5 metro areas in 
each state. so overall a list of 250 city/state.  It accomplishes this by randomly choosing a state then randomly choosing one of the 5 cities in that 
state.

The microserver is using ZeroMQ to coommunicate through Sockets using Request-Reply pattern with a REQ socket

How to Request data from Microserver and Recieve a response
1. Settup a socket to the endpoint (the host of the microserver) based on your programming language according to zermMQ documentations found at:\
https://zeromq.org/get-started/?language=cpp&library=zmqpp# \ 
For this Project partner and I are both programming in python and I am hosting the microserver locally so example below is in in python with a localhost\
Example:\
context = zmq.Context()\
socket = context.socket(zmq.REQ)\
socket.connect("tcp://localhost:5555")

2. To request data by sending a String to microserver\
To use the microserver you need to send a string containing "1" to the microserver. If you send a string that is not the string "1" it will return an 
erro message. If you try to send something besides a string it will error on the client side.\
Example:\
socket.send_string("1") - Valid\
socket.send_string("kk") -Invalid string will get a Error Message back\
socket.send("kk") - Will error on client side since did not send correct type of data

3. To recieve data by recieving a json file back from the microserver\
The microserver will send a json file back that contains a list of the city and state as the two entries in the list and using socket recieve json function of receieving json in the language of choose.  This method will reconstruct the object as the type it was before being seterizlied into a json.\
Example:\
messageback = socket.recv_json()\
(this makes messageback the correct type of object)\

4. You can then do what you want with that list of city and state. 

5. Disconnect from Server

![Untitled Workspace](https://user-images.githubusercontent.com/97073281/218671461-6e3084c2-d27f-427f-bdd1-88c814aea940.png)

