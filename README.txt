####################################################################################################
#        Project - Movie Trailer Website                                                           #
#        Files - entertainment_center.py                                                           #
#                fresh_tomatoes.py                                                                 #
#                media.py                                                                          #
#        Author - Harinder Sharma                                                                  #
#        Course - Full Stack Web Developer Nanodegree at UDACITY                                   #
####################################################################################################

Objective
---------
To showcase my favourite movies on a webpage and allow the visiter to view their trailers.

Usage steps
-----------
1. Execute entertainment_center.py which will open the web page for movie trailer website in viewer's 
default web browser.
2. Click on the movie posters to view trailers.

Code details
-----------------------
entertainment_center.py - This file contains the data for each movie intended to be displayed on web page.
                          This is also the main file and uses services define in fresh_tomatoes.py and media.py.

fresh_tomatoes.py - This code is responsible for reading the movie information from entertainment_center.py and 
                    generating and launching the web page. This contains all the css and script required for the web page.

media.py - This contains class defintion and constructor for a movie object. Objects are created in entertainment_center.py.
