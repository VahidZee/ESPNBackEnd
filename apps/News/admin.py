from django.contrib import admin
from . import models as news_models


# Register your models here.
class NewsImageInline(admin.TabularInline):
    model = news_models.NewsImage
    fields = [
        'image_title',
        'image_description',
        'image'

    ]
    readonly_fields = [
        'image_thumbnail'
    ]
    classes = (
        'extrapretty',
    )
    extra = 0


class NewsResourceInline(admin.TabularInline):
    model = news_models.NewsResource
    extra = 1
    fields = [
        'resource_title',
        'resource_url'
    ]


@admin.register(news_models.NewsTag)
class NewsTag(admin.ModelAdmin):
    list_display = [
        'tag_type', 'tag_title'
    ]
    list_display_links = [
        'tag_title'
    ]
    search_fields = [
        'tag_title'
    ]
    list_filter = [
        'tag_type'
    ]


class NewsTagInline(admin.TabularInline):
    model = news_models.NewsTag.news.through
    extra = 1


@admin.register(news_models.News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('News', {
            'fields': [
                'news_title',
                'news_text',
                'sport_type'
            ]
        }),
        ('Thumbnail & Background', {
            'fields': [
                'thumbnail_image',
                'background_image',
            ],
        })
    ]
    inlines = [
        NewsImageInline,
        NewsResourceInline,
        NewsTagInline,
    ]
    list_display = [
        'id',
        'uploaded_at',
        'sport_type',
        'news_title',
        'news_text_admin_view',
        'thumbnail',
        'background',
        'images',
        'resources_count',
        'tags_count'
    ]
    list_filter = [
        'uploaded_at',
        'sport_type',
    ]
    search_fields = [
        'news_title',
        'news_text'
    ]
    list_display_links = [
        'news_title',
    ]


@admin.register(news_models.NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'image_thumbnail',
        'image_title',
        'image_description',
    ]
