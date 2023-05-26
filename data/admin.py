from django.contrib import admin
from .models import Drugs
from .models import Hospital
from .models import Pharmacy
from .models import Store


admin.site.register(Store)
admin.site.register(Drugs)
admin.site.register(Hospital)
admin.site.register(Pharmacy)



