# from django.contrib import admin
# from .models import Author

# admin.site.register(Author)


from django.contrib import admin

# Register your models here.
from .models import Comment


admin.site.register(Comment)