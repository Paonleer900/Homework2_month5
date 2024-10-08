from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])  # Рейтинг от 1 до 5

    def __str__(self):
        return f"Review for {self.movie.title} - {self.stars} stars"
