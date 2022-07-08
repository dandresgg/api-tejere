''' Machines admin panel '''
from django.contrib import admin

from machines.models import Machine, Part, Sector

admin.site.register(Machine)
admin.site.register(Sector)


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    ''' Custom part's admin panel '''
    list_display = ('id', 'description', 'code', 'reference', 'price', 'stock')
    list_filter = ('reference', 'code', 'sector__kind')
