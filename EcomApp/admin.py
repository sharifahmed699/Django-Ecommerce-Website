from django.contrib import admin
from EcomApp.models import Setting,ContactMessage,FAQ

# Register your models here.
admin.site.register(Setting)
admin.site.register(ContactMessage)


class FAQAdmin(admin.ModelAdmin):
    list_display=['question','ordernumber','status','created_at']

admin.site.register(FAQ,FAQAdmin)