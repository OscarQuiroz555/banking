from django.contrib import admin
<<<<<<< HEAD
from .models import Country, Department, City, User

# Customización del admin para Country
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abrev', 'get_status')  # <--- aquí va list_display

    def get_status(self, obj):
        return "Activo ✅" if obj.status else "Inactivo ❌"
    get_status.short_description = 'Estado'  # Nombre de la columna en la tabla

# Registro de modelos en el admin
admin.site.register(Country, CountryAdmin)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(User)
=======
from .models import Country, Department, City, User    
# Register your models here. modelo que quiero que salga por interfaz grafica

admin.site.register(Country)
admin.site .register(Department)
admin.site.register(City)
admin.site.register(User)

class CountryAdmin(admin.ModelAdmin):
    display_data = ('name', 'abrev', 'get_status')

    def get_status(self, obj):
        return "active" if obj.status else "Inactive"
        get_status.short_description = 'Status' #Table Model
>>>>>>> amigo/main
