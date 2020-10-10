from django.db import models
from base.models import EONBaseModel


class BlogManager(models.Manager):
    """Create descriptive filter names for easier to read view"""

    def published(self):
        return self.filter(published=True)


class Blog(EONBaseModel):

    title = models.CharField(max_length=100)
    content = models.TextField()
    topics = models.ManyToManyField('base.Topic', related_name='blogs')
    date = models.DateField()
    published = models.BooleanField(default=False) # TODO Choices Yes No

    objects = BlogManager()

    class Meta:
        ordering = ['date']
        unique_together = 'title', 'date'

    def __str__(self):
        return '{date} - {title}; Published: {published}'.format(
            date=self.date.strftime('%m/%d/%Y'),
            title=self.title,
            published=self.published,
        )
