from django.contrib import admin
from .models import Project, Finished, Future, Recording

admin.site.register(Project)
admin.site.register(Finished)
admin.site.register(Future)
admin.site.register(Recording)
