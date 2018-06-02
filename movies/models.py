from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    This is a abstract model class to add
    is_deleted, created_at and modified at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self,*args,**kwargs):
        """Soft Delete"""
        self.is_deleted = True
        self.save()


class Genre(BaseModel):
    """
    Model that stores information about Genre
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(BaseModel):
    """
    Model that stores information about Movie
    """
    name = models.CharField(max_length=250)
    popularity = models.FloatField(default=0)
    imdb_score = models.FloatField(default=0)
    director_name = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre) # One Movie can have many genre and one genre can be in many movies
    is_released = models.BooleanField(default=False)

    def __str__(self):
        return self.name