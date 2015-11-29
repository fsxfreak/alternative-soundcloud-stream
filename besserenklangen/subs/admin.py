from django.contrib import admin

# Register your models here.
from .models import Track
from .models import Feed

admin.site.register(Track)
admin.site.register(Feed)