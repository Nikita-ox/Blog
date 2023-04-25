from django.contrib.auth.models import User
from django.db import models as m
from django.utils import timezone
from django.urls import reverse


class PublishedManager(m.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Post.Status.PUBLISHED)


class Post(m.Model):
    class Status(m.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = m.CharField(max_length=250)
    slug = m.SlugField(max_length=250, unique_for_date='publish')
    author = m.ForeignKey(User, on_delete=m.CASCADE,
                          related_name="blog_posts")
    body = m.TextField()
    publish = m.DateTimeField(default=timezone.now)
    created = m.DateTimeField(auto_now_add=True)
    update = m.DateTimeField(auto_now=True)
    status = m.CharField(max_length=2,
                         choices=Status.choices,
                         default=Status.DRAFT)

    objects = m.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ["-publish"]
        indexes = [
            m.Index(fields=["-publish"])
        ]

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

