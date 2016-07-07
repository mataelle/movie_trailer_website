import media
import fresh_tomatoes

real_steel = media.Movie("Real Steel",
                         "In the near future, robot boxing is a top sport. \
                         A struggling promoter feels he's found a champion \
                         in a discarded robot.",
                         "http://www.impawards.com/2011/posters/real_steel_ver4.jpg",  # noqa
                         "https://www.youtube.com/watch?v=3S8a180uYBM")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use \
                        of dream-sharing technology, is given the inverse \
                        task of planting an idea into the mind of a CEO.",
                        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg",  # noqa
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

finding_nemo = media.Movie("Finding Nemo",
                           "After his son is captured in the Great \
                           Barrier Reef and taken to Sydney, a timid \
                           clownfish sets out on a journey \
                           to bring him home.",
                           "http://vignette1.wikia.nocookie.net/disney/images/8/89/Finding_Nemo_-_Poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

ip_man = media.Movie("Ip Man",
                     "During the Japanese invasion of 1937, when a wealthy \
                     martial artist is forced to leave his home and work \
                     to support his family, he reluctantly agrees to train \
                     others in the art of Wing Chun for self-defense.",
                     "http://img.goldposter.com/2015/05/Yip-Man_poster_goldposter_com_16.jpg",  # noqa
                     "https://www.youtube.com/watch?v=1AJxXQ7xojE")

devil_wears_prada = media.Movie("The Devil Wears Prada",
                                "A smart but sensible new graduate lands a \
                                job as an assistant to Miranda Priestly, \
                                the demanding editor-in-chief of \
                                a high fashion magazine.",
                                "http://www.impawards.com/2006/posters/devil_wears_prada.jpg",  # noqa
                                "https://www.youtube.com/watch?v=XTDSwAxlNhc")

pirates = media.Movie("Pirates of the Carribean",
                      "Blacksmith Will Turner teams up with eccentric \
                      pirate 'Captain' Jack Sparrow to save his love, \
                      the governor's daughter, from Jack's former \
                      pirate allies, who are now undead.",
                      "http://cdn.traileraddict.com/content/walt-disney-pictures/pirates.jpg",  # noqa
                      "https://www.youtube.com/watch?v=0Z1XpfbuZOA")


movies = [real_steel, inception, finding_nemo,
          ip_man, devil_wears_prada, pirates]
fresh_tomatoes.open_movies_page(movies)
