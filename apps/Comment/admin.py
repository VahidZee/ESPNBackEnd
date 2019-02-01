# General imports
from django.contrib import admin

# Models import
from . import models as comment_models


class CommentInline(admin.TabularInline):
    model = comment_models.Comment
    extra = 1


@admin.register(comment_models.CommentField)
class CommentFieldAdmin(admin.ModelAdmin):
    list_display = [
        'field_type',
        'commented_id',
    ]
    list_filter = [
        'field_type',
    ]
    inlines = [
        CommentInline
    ]
