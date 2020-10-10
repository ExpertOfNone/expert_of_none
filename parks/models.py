from django.db import models
from django_countries.fields import CountryField
from localflavor.us.models import USStateField

from base.models import EONBaseModel


class Amenity(EONBaseModel):
    """Common amenities, i.e. Pool, Lake, Hiking Trail, Primitive Camping, etc."""

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Park(EONBaseModel):
    """General Park Information Utilized for Reference"""

    PARK_TYPE_STATE = 'state'
    PARK_TYPE_NATIONAL = 'national'
    PARK_TYPE_CITY = 'city'
    PARK_TYPE_OTHER = 'other'
    PARK_TYPE_CHOICES = (
        (PARK_TYPE_STATE, 'State'),
        (PARK_TYPE_NATIONAL, 'National'),
        (PARK_TYPE_CITY, 'City'),
        (PARK_TYPE_OTHER, 'Other'),
    )

    park_type = models.CharField(max_length=20, choices=PARK_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    photos = models.ManyToManyField('base.Photo', through='ParkPhoto')

    address_one = models.CharField(max_length=50)
    address_two = models.CharField(max_length=50, null=True, blank=True)

    city = models.CharField(max_length=50)
    state = USStateField(blank=True, null=True)
    country = CountryField()
    postal_code = models.CharField(blank=True, null=True, max_length=20)

    amenities = models.ManyToManyField('Amenity', through='ParkAmenity')

    topic = models.ForeignKey('base.Topic', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{name} - {park_type}'.format(
            name=self.name,
            park_type=self.get_park_type_display(),
        )


class ParkAmenity(EONBaseModel):

    park = models.ForeignKey('Park', on_delete=models.CASCADE)
    amenity = models.ForeignKey('Amenity', on_delete=models.CASCADE)
    additional_info = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Park Amenities'

    def __str__(self):
        return '{park_name} - {amenity}'.format(
            park_name=self.park.name,
            amenity=self.amenity.name,
        )


class ParkPhoto(EONBaseModel):
    """Photos taken of parks. Pass through model for Parks and Photos."""

    photo = models.ForeignKey('base.Photo', on_delete=models.CASCADE, related_name='park_photos')
    park = models.ForeignKey('Park', on_delete=models.DO_NOTHING, related_name='park_photos')

    def __str__(self):
        return '{park_name} - Photo:{photo_name}'.format(
            park_name=self.park.name,
            photo_name=self.photo.name,
        )
