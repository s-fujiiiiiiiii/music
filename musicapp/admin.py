from django.contrib import admin

# Register your models here.
from .models import User
from .models import Artist
from .models import Song

admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Song)
