from django.contrib import admin
from .models import (
    PerfilUsuario, EspecieMarina, EspecieEnPeligro, HabitatMarino,
    EspecieHabitat, AmenazaMarina, Contaminante, AmenazaContaminante,
    RecursoEducativo, CentroInvestigacion, OrganizacionProteccion,
    ProyectoOrganizacion, AreaProtegida, Nivel, PuntajeJuego, Logro,
    UsuarioLogro, EventoMarino, Amigos, Chat
)

admin.site.register(PerfilUsuario)
admin.site.register(EspecieMarina)
admin.site.register(EspecieEnPeligro)
admin.site.register(HabitatMarino)
admin.site.register(EspecieHabitat)
admin.site.register(AmenazaMarina)
admin.site.register(Contaminante)
admin.site.register(AmenazaContaminante)
admin.site.register(RecursoEducativo)
admin.site.register(CentroInvestigacion)
admin.site.register(OrganizacionProteccion)
admin.site.register(ProyectoOrganizacion)
admin.site.register(AreaProtegida)
admin.site.register(Nivel)
admin.site.register(PuntajeJuego)
admin.site.register(Logro)
admin.site.register(UsuarioLogro)
admin.site.register(EventoMarino)
admin.site.register(Amigos)
admin.site.register(Chat)
