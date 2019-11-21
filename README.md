# Djikstra-PyGame
A simple application using PyGame and Python 3.3 that finds the shortest path between selected points on a small preset map of Bangalore.

Overview:

line 1 - 94     : main function

line 95 - 114   : dijkstra function

line 115 - 123  : distance covered function

line 124 - 2065 : pygame event loop

Event loop : Each event made by the user is captured and stored. An event is any way of interacting with the application. 
For example, a mouse click, key press, mouse cursor movement, etc. The event loop updates the screen with every single event that it captures.
The function that updates the screen is pygame.display.flip(). Flip means update.
We do all our function calling and screen creating processes in the event loop. When a certain button is clicked, the event is captured and the screen is updated.


line 130 - 166   : Home screen code

if f = 1 then it goes to next screen.



line 167 - 261   : Place selection screen

if f1 = 1: Hebbal

if f1 = 1: Banashankari

if f1==3: MG Road

if f1==4: Rajajinagar

if f1==5: Majestic



line 262 - 479   : Places to visit in Hebbal selection screen

If go button is clicked, it goes to result screen. The result screen is where we call the dijkstra and distance                       functions.

All the place selection screens run the same way.



line 480 - 696   : Places to visit in Banashankari selection screen

line 697 - 914   : Places to visit in MG Road selection screen

line 915 - 1131  : Places to visit in Rajajinagar selection screen

line 1132 - 1357 : Places to visit in Majestic selection screen

line 1358 - 2062 : Results screen for respective places:

In the result screen, we call the dijkstra and distance covered functions. We print the chosen places, starting point, shortest path and distance covered in this screen. Next button on being clicked takes the user to the original place 
selection screen where user can select another place or exit the application.
