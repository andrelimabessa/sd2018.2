from django.contrib import admin


from .models import Jogada


class JogadaAdmin(admin.ModelAdmin):
    list_display=('autor', 'oponente', 'linha', 'coluna', 'created_date')
    list_filter=['autor']
    search_fields=['autor']
    class Meta:
        model = Jogada

admin.site.register(Jogada,JogadaAdmin)
