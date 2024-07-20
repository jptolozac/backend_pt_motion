from django.contrib import admin
from .models import Dealer, Applicant, Branch, Brand

# Register your models here.
admin.site.register(Dealer)
admin.site.register(Applicant)
admin.site.register(Branch)
admin.site.register(Brand)