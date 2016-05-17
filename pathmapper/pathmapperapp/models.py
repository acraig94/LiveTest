from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return "Lat: " + str(self.lat) + " Lng: " + str(self.lng)

class Plant(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=500)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return str(self.name)


class PlantCollection(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.collection) + " " + str(self.plant)


class Track(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=500)
    estimatedTime = models.IntegerField()
    difficulty = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])  # scale of 0-10 for difficulty
    wheelchairAccess = models.BooleanField()  # change to accessability with choices ??
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class TrackPoint(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.track) + " - " + str(self.location)


class UpdateManager(models.Model):
    locationLastUpdate = models.DateTimeField(auto_now_add=True)
    plantLastUpdate = models.DateTimeField(auto_now_add=True)
    collectionLastUpdate = models.DateTimeField(auto_now_add=True)
    plantCollectionLastUpdate = models.DateTimeField(auto_now_add=True)
    trackLastUpdate = models.DateTimeField(auto_now_add=True)
    trackPointLastUpdate = models.DateTimeField(auto_now_add=True)
