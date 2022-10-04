from django.db import models


class Film(models.Model):
    HORROR = "HOR"
    DOCUMENTARY = "DOC"
    COMEDY = "COM"
    GENRES = [
        (None, ""),
        (HORROR, "Horror"),
        (DOCUMENTARY, "Documentary"),
        (COMEDY, "Comedy")
    ]

    film_title = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    blurb = models.TextField()
    genre = models.CharField(max_length=3, choices=GENRES, default=None)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.film_title
