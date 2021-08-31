from django.contrib import admin
from .models import Project, Finished, Future

admin.site.register(Project)
admin.site.register(Finished)
admin.site.register(Future)
