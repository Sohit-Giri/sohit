from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Use 'created_at' if it exists in the model

admin.site.register(Contact, ContactAdmin)
