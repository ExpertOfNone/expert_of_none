from django.contrib import admin

from base.admin import EONBaseAdmin
from parks.models import Park, ParkAmenity, ParkPhoto


class ParkPhotoInline(admin.TabularInline):

    model = ParkPhoto


class ParkAmenityInline(admin.TabularInline):

    model = ParkAmenity


class ParkAdmin(EONBaseAdmin):

    inlines = [
        ParkPhotoInline, ParkAmenityInline
    ]


admin.site.register(Park, ParkAdmin)
