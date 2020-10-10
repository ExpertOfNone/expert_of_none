from django.contrib import admin
from base.admin import EONBaseAdmin
from parks.models import Park, ParkAmenity, ParkPhoto


class ParkAdmin(EONBaseAdmin):
    pass


class ParkPhotoAdmin(EONBaseAdmin):
    pass


class ParkAmenityAdmin(EONBaseAdmin):
    pass


admin.site.register(Park, ParkAdmin)
admin.site.register(ParkAmenity, ParkAmenityAdmin)
admin.site.register(ParkPhoto, ParkPhotoAdmin)
