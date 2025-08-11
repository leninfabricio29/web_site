from django.contrib import admin
from .models import App, AppVersion

class AppVersionInline(admin.TabularInline):
    model = AppVersion
    extra = 0
    fields = ("platform", "version", "is_prerelease", "file", "external_link", "created_at")
    readonly_fields = ("created_at",)

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [AppVersionInline]

@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = ("app", "platform", "version", "is_prerelease", "created_at")
    list_filter = ("platform", "is_prerelease", "app")
    search_fields = ("version", "release_notes", "app__name")
    date_hierarchy = "created_at"
