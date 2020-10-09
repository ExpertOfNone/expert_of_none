from django.contrib.auth import get_user_model
from django.db import models


user_model = get_user_model()


class EONBaseModel(models.Model):
    """User and Time Stamps - Abstract"""

    created = models.DateTimeField(auto_now_add=True, editable=False)
    # Required on save, but in case User gets deleted Null is valid
    created_by = models.ForeignKey(user_model, on_delete=models.SET_NULL, editable=False, related_name='+', null=True)

    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(user_model, on_delete=models.SET_NULL, related_name='+', null=True)

    class Meta:

        abstract = True


class Topic(EONBaseModel):
    """Areas of content for Blogs, utilized for sorting"""

    name = models.CharField(max_length=50,)
    code = models.CharField(max_length=5)
    description = models.TextField(null=True)
    parent_topic = models.ForeignKey('self', blank=True, on_delete=models.SET_NULL, null=True)
    top_level = models.BooleanField(default=False, choices=((False, 'No'), (True, 'Yes')))  # TODO is there a Django Yes No

    class Meta:
        ordering = ['name']
        unique_together = 'name', 'parent_topic'

    def __str__(self):
        return self.name

    # TODO add clean method that doesnt allow a parent topic when top level is selected

