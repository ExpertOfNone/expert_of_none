from django.contrib import admin
from base.admin import EONBaseAdmin
from parks.models import Park, ParkAmenity, ParkPhoto


# TODO make Photo and Park Amenity Inline with Photo upload in the same page
class ParkAdmin(EONBaseAdmin):
    pass


class ParkPhotoAdmin(EONBaseAdmin):
    pass


class ParkAmenityAdmin(EONBaseAdmin):
    pass


admin.site.register(Park, ParkAdmin)
admin.site.register(ParkAmenity, ParkAmenityAdmin)
admin.site.register(ParkPhoto, ParkPhotoAdmin)
