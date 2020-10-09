from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Blog


class BlogModelTest(TestCase):

    def setUp(self) -> None:

        user_model = get_user_model()

        user = user_model.objects.create(first_name='Test', last_name='Test')

        blog_creations = [{
                'title': 'FIRST',
                'created_by': user,
                'modified_by': user,
                'content': 'Entry To Be First',
                'date': date(year=2020, month=8, day=31),
                'published': True,

            },
                {
                'title': 'SECOND',
                'created_by': user,
                'modified_by': user,
                'content': 'Entry To Be Second',
                'date': date(year=2020, month=9, day=30),
                'published': True,

            },
                    {
                'title': 'THIRD',
                'created_by': user,
                'modified_by': user,
                'content': 'Entry To Be Third',
                'date': date(year=2020, month=10, day=31),
                'published': True,

            },
                    {
                'title': 'UNPUBLISHED',
                'created_by': user,
                'modified_by': user,
                'content': 'Entry not To Be shown',
                'date': date(year=2020, month=8, day=31),
                'published': False,
            },
        ]

        for blog_creation in blog_creations:

            Blog.objects.create(**blog_creation)

    def test_first_ordering(self):

        self.assertEqual('FIRST', Blog.objects.first().title)

    def test_published(self):

        self.assertEqual(3, Blog.objects.published().count())