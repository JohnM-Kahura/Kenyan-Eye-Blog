from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Blog 
# class UserAdminConfig(UserAdmin):
#     search_fields=('title','category',)
#     list_filter=('title','category',)
#     ordering=('title',)
#     list_display=('title','category','comments','views',)
#     fieldsets = (
#         (None, {'fields': ('title','category',)}),
#     )

#     # formfield_overrides = {
#     #     CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     # } 


#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('title','category','preview')}
#          ),
#     )   

admin.site.register(Blog,)
