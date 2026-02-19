from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team_id', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain_id', 'created_at')
    search_fields = ('name', 'captain_id')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'activity_type', 'duration', 'distance', 'calories', 'date')
    search_fields = ('user_id', 'activity_type')
    list_filter = ('activity_type', 'date')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('username', 'team_name', 'rank', 'total_activities', 'total_duration', 'total_calories', 'total_distance')
    search_fields = ('username', 'team_name')
    list_filter = ('rank', 'updated_at')
    readonly_fields = ('updated_at',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_type', 'difficulty', 'duration', 'calories_estimate', 'created_at')
    search_fields = ('name', 'activity_type', 'difficulty')
    list_filter = ('activity_type', 'difficulty', 'created_at')
    readonly_fields = ('created_at',)
