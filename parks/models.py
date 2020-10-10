from django.db import models
from base.models import EONBaseModel

# TODO Add Django Local Flavor
# TODO Add Django Countries - Use according to instructions (settings) not your hack


class Amenity(EONBaseModel):
    """Common amenities, i.e. Pool, Lake, Hiking Trail, Primitive Camping, etc."""

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Park(EONBaseModel):

    PARK_TYPE_STATE = 'state'
    PARK_TYPE_NATIONAL = 'national'
    PARK_TYPE_CITY = 'city'
    PARK_TYPE_OTHER = 'other'
    PARK_TYPE_CHOICES = (
        (PARK_TYPE_STATE, 'State'),
        (PARK_TYPE_NATIONAL, 'National'),
        (PARK_TYPE_CITY, 'City'),
        (PARK_TYPE_OTHER, 'Other')
    )

    park_type = models.CharField(max_length=20, choices=PARK_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    photos = models.ManyToManyField('base.Photo', through='ParkPhoto')

    address_one = models.CharField(max_length=50)
    address_two = models.CharField(max_length=50, null=True, blank=True)

    city = models.CharField(max_length=50)
    # State - optional
    # Country
    # Postal Code - Set up for International, not required
    # international phone number field

    amenities = models.ManyToManyField(Amenity, through='ParkAmenity')

    topic = models.ForeignKey('base.Topic', on_delete=models.SET_NULL, null=True)


class ParkAmenity(models.Model):

    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)
    additional_info = models.TextField(blank=True)


class ParkPhoto(EONBaseModel):

    photo = models.ForeignKey('base.Photo', on_delete=models.CASCADE, related_name='park_photos')
    park = models.ForeignKey(Park, on_delete=models.DO_NOTHING, related_name='photos')

    def __str__(self):
        return '{park_name} - Photo:{photo_name}'.format(park_name=self.park.name, photo_name=self.photo.name)