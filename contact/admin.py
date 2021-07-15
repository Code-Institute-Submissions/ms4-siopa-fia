from django.contrib import admin
from .models import Contact
from .models import NewsletterSubscribe


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)


admin.site.register(NewsletterSubscribe, NewsletterAdmin)
admin.site.register(Contact)
