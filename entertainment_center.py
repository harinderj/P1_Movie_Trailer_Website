import media
import fresh_tomatoes

# Store movies information in their respective media objects
#   - Movie name
#   - Release date
#   - Storyline
#   - Poster image
#   - Youtube trailer url

pk = media.Movie("pk",
                 2014,
                 "A man from mars learns to leave on earth",
                 "http://upload.wikimedia.org/wikipedia/en/2/2d/PK_Theatrical_Poster.jpg",
                 "www.youtube.com/watch?v=82ZEDGPCkT8")

munna_bhai = media.Movie("Munna Bhai MBBS",
                         2003,
                        "A don teaches how to live life",
                        "http://upload.wikimedia.org/wikipedia/en/1/19/Munna_Bhai_M.B.B.S.%2C_2003_Hindi_film_poster.jpg",
                        "www.youtube.com/watch?v=6lCGvu-hwX4")

cars = media.Movie("Cars",
                   2006,
                        "Talking cars in lead role, first time in a movie",
                        "http://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
                        "www.youtube.com/watch?v=JzwWqkxBb5I")

ice_age = media.Movie("Ice Age 2 - The Meltdown",
                      2006,
                     "With global warming threatening their once-icy domain with widespread flooding, Manny (Ray Romano), Sid (John Leguizamo) and Diego (Denis Leary) set out to find a safe haven. Along the way, another mammoth (Queen Latifah), who thinks she is an opossum, joins the travelers on their perilous quest.",
                     "http://upload.wikimedia.org/wikipedia/en/f/f1/Ice_Age_2_poster.jpg",
                     "www.youtube.com/watch?v=M8bRIAPOVtA")

mother_india = media.Movie("Mother India",
                           1957,
                             "The wedding of Radha (Nargis) and Shamu (Rajendra Kumar) is at hand, but the loan they take out to pay for the ceremony ends up leading to their ruin. Unable to pay the mounting interest rates, the couple is forced to give up three quarters of their crop to the moneylenders. Shamu works the fields in an attempt to alleviate their poverty, but a loose boulder crushes his arm, rendering him incapable of work and humiliated at his sudden inability to provide for his family.",
                             "http://upload.wikimedia.org/wikipedia/en/2/20/Mother_India_poster.jpg",
                             "www.youtube.com/watch?v=HuUiiEv6YSY")

stuart_little = media.Movie("Stuart Little",
                            1999,
                          "A little moouse who can speak gets adopted to a human family which also keeps a pet cat",
                          "http://upload.wikimedia.org/wikipedia/en/9/96/Stuart_Little.jpg",
                          "www.youtube.com/watch?v=Rpl4NI5GT-c")


# Create movies list to be presented on web page
movies = [pk, munna_bhai, cars, ice_age, mother_india, stuart_little]

# Launch movies page
fresh_tomatoes.open_movies_page(movies)
