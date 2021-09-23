from django.contrib import admin
from QTapp.models import Contact

# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'email', 'name', 'date', 'phone', 'desc') #list to display the contents
    list_filter=('date',)                                 #list to filter in admin page
    list_per_page=15                                      #list of contents to display in one page
    search_fields= ('email', 'phone', 'name', 'date')     #search in list of contents
    ordering=('date',)
    
    


admin.site.register(Contact,ContactAdmin)