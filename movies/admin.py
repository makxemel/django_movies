from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма в админке"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres', ), )
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': (('description', 'poster'),)
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'),)
        }),
        ('Actors', {
            'classes': (('collapse'),),
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft',),)
        }),
    )


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ('star', 'ip')


@admin.register(MovieShot)
class MovieShotAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie')


admin.site.register(RaitingStar)


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Actor)
# admin.site.register(Genre)
# admin.site.register(Movie)
# admin.site.register(MovieShot)
# admin.site.register(Raiting)
# admin.site.register(Reviews)
