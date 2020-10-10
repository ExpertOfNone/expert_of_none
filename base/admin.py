from django.contrib import admin

from base.models import Topic, Photo


class EONBaseAdmin(admin.ModelAdmin):

    def get_changeform_initial_data(self, request):

        initial = super().get_changeform_initial_data(request)

        if 'add' in request.META['PATH_INFO']:
            initial['created_by'] = request.user

        initial['modified_by'] = request.user

        return initial

    def save_model(self, request, obj, form, change):

        if not obj.created_by:
            obj.created_by = request.user

        return super().save_model(request, obj, form, change)


class TopicAdmin(EONBaseAdmin):

    list_display = [
        'name', 'parent_topic', 'top_level', 'modified_by', 'modified', 'created_by', 'created',
    ]


class PhotoAdmin(EONBaseAdmin):

    # TODO Add Proper List Display

    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(Photo, PhotoAdmin)
