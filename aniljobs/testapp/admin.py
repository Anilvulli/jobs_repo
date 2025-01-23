from django.contrib import admin

# Register your models here.
from testapp.models import HydJobs
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)



from testapp.models import PuneJobs
class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(PuneJobs,PuneJobsAdmin)


from testapp.models import BangaloreJobs
class BangaloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(BangaloreJobs,BangaloreJobsAdmin)