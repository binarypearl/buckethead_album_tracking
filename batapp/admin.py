from django.contrib import admin
from batapp.models import Album

class AlbumAdmin(admin.ModelAdmin):
  list_display = ('album_name', 'pike_number')

admin.site.register(Album, AlbumAdmin)
