from django.contrib import admin

# Register your models here.
from .models import Professor,Course,PReview,CReview 

admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(PReview)
admin.site.register(CReview)