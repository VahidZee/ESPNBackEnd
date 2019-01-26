from django.db import models
from django.utils.html import format_html


# Create your models here.

def image_path(instance, filename: str):
    return 'news/' + str(instance.news.id) + '/' + filename.strip().replace(' ', '')


def thumbnail_image_path(instance, filename: str):
    return 'news/' + str(instance.id) + '/tn' + filename[filename.rfind('.'):]


def background_image_path(instance, filename: str):
    return 'news/' + str(instance.id) + '/bg' + filename[filename.rfind('.'):]


class News(models.Model):
    news_title = models.CharField(max_length=500)
    news_text = models.TextField()

    SPORT_TYPE_BASKETBALL = 'B'
    SPORT_TYPE_FOOTBALL = 'F'
    SPORT_TYPE_CHOICES = (
        (SPORT_TYPE_BASKETBALL, 'Basketball'),
        (SPORT_TYPE_FOOTBALL, 'Football')
    )
    sport_type = models.CharField(
        choices=SPORT_TYPE_CHOICES,
        max_length=1
    )
    uploaded_at = models.DateTimeField(auto_now=True)

    thumbnail_image = models.ImageField(upload_to=thumbnail_image_path, blank=True)
    background_image = models.ImageField(upload_to=background_image_path, blank=True)

    def news_text_summery(self):
        return self.news_text[:512]

    def news_text_admin_view(self):
        return self.news_text[:40] + ' . . .'

    def images_count(self):
        return self.newsimage_set.all().count()

    def images(self):
        res = ''
        for image in self.newsimage_set.all():
            res += '<img src="{}" width="20vw">'.format('http://127.0.0.1:8000/' + str(image.image.url))

        return format_html(res)

    def thumbnail(self):
        if self.thumbnail_image:
            return format_html(
                '<img src="{}" width="80vw">'.format('http://127.0.0.1:8000/' + str(self.thumbnail_image.url))
            )
        return ''

    def background(self):
        if self.background_image:
            return format_html(
                '<img src="{}" width="80vw">'.format('http://127.0.0.1:8000/' + str(self.background_image.url))
            )
        return ''

    def resources_count(self):
        return self.newsresource_set.all().count()

    def tags_count(self):
        return self.newstag_set.all().count()

    def json_dict(self):
        images = list()
        for image in self.newsimage_set.all():
            images.append(
                {
                    'image': 'http://localhost:8000/' + str(image.image.url),
                    'caption': str(image.image_title),
                    'text': str(image.image_description)
                }
            )

        tags = list()
        for tag in self.newstag_set.all():
            tags.append(
                {
                    'type': tag.tag_type,
                    'id': tag.tagged_id,
                    'title': tag.tag_title
                }
            )

        resources = list()
        for resource in self.newsresource_set.all():
            resources.append(
                {
                    'title': resource.resource_title,
                    'link': resource.resource_url
                }
            )

        json_dict = {
            'id': self.id,
            'backgroundImage': 'http://localhost:8000/' + str(self.background_image.url),
            'title': self.news_title,
            'paragraphs': self.news_text.split('\n'),

            'images': images,
            'resources': resources,
            'tags': tags,

            'publishDate': self.uploaded_at.isoformat()
        }

        return json_dict

    def summery_json_dict(self):
        json_dict = {
            'id': self.id,
            'title': self.news_title,
            'description': self.news_text[:700],
            'publishDate': self.uploaded_at.isoformat(),
            'sportType': self.sport_type,
        }

        if self.thumbnail_image:
            json_dict['image'] = (str('http://localhost:8000/'.__add__(str(self.thumbnail_image.url)))),
            json_dict['image'] = json_dict['image'][0]
        return json_dict

    def __str__(self):
        return self.news_title + ' -> ' + self.news_text_admin_view()

    class Meta:
        verbose_name = 'All News'
        verbose_name_plural = 'News'


class NewsResource(models.Model):
    news = models.ForeignKey(to=News, on_delete=models.CASCADE)
    resource_title = models.CharField(max_length=100)
    resource_url = models.URLField()

    def __str__(self):
        return self.resource_title[:30]


class NewsTag(models.Model):
    news = models.ForeignKey(to=News, on_delete=models.CASCADE)

    GAME_TAG = 'G'
    TEAM_TAG = 'T'
    PLAYER_TAG = 'P'
    LEAGUE_TAG = 'L'
    TAG_CHOICES = (
        (GAME_TAG, 'Game'),
        (TEAM_TAG, 'Team'),
        (PLAYER_TAG, 'Player'),
        (LEAGUE_TAG, 'League'),
    )
    tag_type = models.CharField(
        choices=TAG_CHOICES,
        blank=False,
        max_length=1
    )

    tagged_id = models.IntegerField(blank=False)
    tag_title = models.CharField(max_length=40, blank=False)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class NewsImage(models.Model):
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    news = models.ForeignKey(to=News, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to=image_path, blank=False)
    image_description = models.CharField(max_length=500, blank=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def image_thumbnail(self):
        return format_html('<img src="{}" height="200px">', 'http://127.0.0.1:8000/' + str(self.image.url))

    def __str__(self):
        return self.image_title
