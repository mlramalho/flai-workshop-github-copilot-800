from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
from bson import ObjectId


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write('Creating teams...')
        
        # Create Team Marvel
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes',
            captain_id='',  # Will update after creating users
        )
        
        # Create Team DC
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League of America',
            captain_id='',  # Will update after creating users
        )
        
        self.stdout.write('Creating users...')
        
        # Team Marvel members
        iron_man = User.objects.create(
            name='Tony Stark',
            email='ironman@marvel.com',
            password='stark123',
            team_id=str(team_marvel._id)
        )
        
        captain_america = User.objects.create(
            name='Steve Rogers',
            email='captainamerica@marvel.com',
            password='rogers123',
            team_id=str(team_marvel._id)
        )
        
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@marvel.com',
            password='thor123',
            team_id=str(team_marvel._id)
        )
        
        black_widow = User.objects.create(
            name='Natasha Romanoff',
            email='blackwidow@marvel.com',
            password='natasha123',
            team_id=str(team_marvel._id)
        )
        
        hulk = User.objects.create(
            name='Bruce Banner',
            email='hulk@marvel.com',
            password='banner123',
            team_id=str(team_marvel._id)
        )
        
        # Team DC members
        superman = User.objects.create(
            name='Clark Kent',
            email='superman@dc.com',
            password='clark123',
            team_id=str(team_dc._id)
        )
        
        batman = User.objects.create(
            name='Bruce Wayne',
            email='batman@dc.com',
            password='wayne123',
            team_id=str(team_dc._id)
        )
        
        wonder_woman = User.objects.create(
            name='Diana Prince',
            email='wonderwoman@dc.com',
            password='diana123',
            team_id=str(team_dc._id)
        )
        
        flash = User.objects.create(
            name='Barry Allen',
            email='flash@dc.com',
            password='barry123',
            team_id=str(team_dc._id)
        )
        
        aquaman = User.objects.create(
            name='Arthur Curry',
            email='aquaman@dc.com',
            password='arthur123',
            team_id=str(team_dc._id)
        )
        
        # Update team captains and members
        team_marvel.captain_id = str(iron_man._id)
        team_marvel.members = [
            str(iron_man._id),
            str(captain_america._id),
            str(thor._id),
            str(black_widow._id),
            str(hulk._id)
        ]
        team_marvel.save()
        
        team_dc.captain_id = str(superman._id)
        team_dc.members = [
            str(superman._id),
            str(batman._id),
            str(wonder_woman._id),
            str(flash._id),
            str(aquaman._id)
        ]
        team_dc.save()
        
        self.stdout.write('Creating activities...')
        
        # Create activities for the past 7 days
        base_date = datetime.now()
        
        # Team Marvel activities
        activities_data = [
            # Iron Man - Tech-focused workouts
            (iron_man, 'Running', 45, 8.5, 450, base_date - timedelta(days=1), 'Morning run in the city'),
            (iron_man, 'Cycling', 60, 25.0, 600, base_date - timedelta(days=2), 'Bike ride to Stark Tower'),
            (iron_man, 'Gym', 90, None, 700, base_date - timedelta(days=3), 'Heavy lifting session'),
            
            # Captain America - All-around fitness
            (captain_america, 'Running', 60, 12.0, 600, base_date - timedelta(days=1), 'Super soldier training'),
            (captain_america, 'Gym', 120, None, 900, base_date - timedelta(days=2), 'Full body workout'),
            (captain_america, 'Cycling', 45, 20.0, 500, base_date - timedelta(days=4), 'Recovery ride'),
            
            # Thor - Godly strength training
            (thor, 'Gym', 150, None, 1200, base_date - timedelta(days=1), 'Hammer training'),
            (thor, 'Running', 30, 6.0, 400, base_date - timedelta(days=3), 'Sprint training'),
            
            # Black Widow - Agility and endurance
            (black_widow, 'Running', 50, 10.0, 500, base_date - timedelta(days=1), 'Stealth run'),
            (black_widow, 'Gym', 75, None, 600, base_date - timedelta(days=2), 'Combat training'),
            (black_widow, 'Yoga', 60, None, 200, base_date - timedelta(days=3), 'Flexibility work'),
            
            # Hulk - Smash workouts
            (hulk, 'Gym', 180, None, 1500, base_date - timedelta(days=1), 'Hulk smash!'),
            (hulk, 'Running', 40, 8.0, 500, base_date - timedelta(days=2), 'Anger management jog'),
            
            # Superman - Superhuman training
            (superman, 'Flying', 90, 100.0, 800, base_date - timedelta(days=1), 'Morning patrol'),
            (superman, 'Gym', 120, None, 1000, base_date - timedelta(days=2), 'Kryptonian workout'),
            (superman, 'Running', 30, 50.0, 400, base_date - timedelta(days=3), 'Speed training'),
            
            # Batman - Peak human conditioning
            (batman, 'Running', 60, 12.0, 600, base_date - timedelta(days=1), 'Gotham patrol'),
            (batman, 'Gym', 150, None, 1100, base_date - timedelta(days=2), 'Fighting crime workout'),
            (batman, 'Cycling', 45, 22.0, 500, base_date - timedelta(days=3), 'Batmobile maintenance ride'),
            
            # Wonder Woman - Amazonian training
            (wonder_woman, 'Running', 55, 11.0, 550, base_date - timedelta(days=1), 'Amazon warrior run'),
            (wonder_woman, 'Gym', 100, None, 800, base_date - timedelta(days=2), 'Sword training'),
            (wonder_woman, 'Yoga', 45, None, 180, base_date - timedelta(days=4), 'Themyscira meditation'),
            
            # Flash - Speed force training
            (flash, 'Running', 20, 100.0, 300, base_date - timedelta(days=1), 'Speed force practice'),
            (flash, 'Running', 15, 80.0, 250, base_date - timedelta(days=2), 'Time travel warmup'),
            (flash, 'Gym', 60, None, 600, base_date - timedelta(days=3), 'Speedster strength'),
            
            # Aquaman - Ocean training
            (aquaman, 'Swimming', 90, 15.0, 700, base_date - timedelta(days=1), 'Ocean patrol'),
            (aquaman, 'Gym', 100, None, 850, base_date - timedelta(days=2), 'Trident training'),
            (aquaman, 'Swimming', 60, 10.0, 500, base_date - timedelta(days=3), 'Underwater sprint'),
        ]
        
        for user, activity_type, duration, distance, calories, date, notes in activities_data:
            Activity.objects.create(
                user_id=str(user._id),
                activity_type=activity_type,
                duration=duration,
                distance=distance,
                calories=calories,
                date=date,
                notes=notes
            )
        
        self.stdout.write('Creating leaderboard entries...')
        
        # Calculate leaderboard stats for each user
        users = [iron_man, captain_america, thor, black_widow, hulk, 
                 superman, batman, wonder_woman, flash, aquaman]
        
        leaderboard_entries = []
        for user in users:
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_activities = user_activities.count()
            total_duration = sum(a.duration for a in user_activities)
            total_calories = sum(a.calories for a in user_activities)
            total_distance = sum(a.distance or 0 for a in user_activities)
            
            team = Team.objects.get(_id=ObjectId(user.team_id))
            
            leaderboard_entries.append({
                'user': user,
                'team': team,
                'total_activities': total_activities,
                'total_duration': total_duration,
                'total_calories': total_calories,
                'total_distance': total_distance
            })
        
        # Sort by total_calories (descending) and assign ranks
        leaderboard_entries.sort(key=lambda x: x['total_calories'], reverse=True)
        
        for rank, entry in enumerate(leaderboard_entries, start=1):
            Leaderboard.objects.create(
                user_id=str(entry['user']._id),
                username=entry['user'].name,
                team_id=str(entry['team']._id),
                team_name=entry['team'].name,
                total_activities=entry['total_activities'],
                total_duration=entry['total_duration'],
                total_calories=entry['total_calories'],
                total_distance=entry['total_distance'],
                rank=rank
            )
        
        self.stdout.write('Creating workout suggestions...')
        
        workouts = [
            {
                'name': 'Iron Man Cardio Blast',
                'description': 'High-intensity cardio workout inspired by Tony Stark',
                'activity_type': 'Running',
                'difficulty': 'Advanced',
                'duration': 45,
                'calories_estimate': 500,
                'instructions': [
                    'Warm up with 5 minutes of light jogging',
                    'Run at 80% max speed for 2 minutes',
                    'Walk for 1 minute to recover',
                    'Repeat intervals 8 times',
                    'Cool down with 5 minutes of walking'
                ]
            },
            {
                'name': 'Captain America Strength Training',
                'description': 'Full-body strength workout for super soldiers',
                'activity_type': 'Gym',
                'difficulty': 'Intermediate',
                'duration': 60,
                'calories_estimate': 600,
                'instructions': [
                    '3 sets of 15 push-ups',
                    '3 sets of 12 squats',
                    '3 sets of 10 pull-ups',
                    '3 sets of 20 sit-ups',
                    '3 sets of 15 lunges per leg',
                    'Stretch for 10 minutes'
                ]
            },
            {
                'name': 'Thor Hammer Slam',
                'description': 'Godly hammer training workout',
                'activity_type': 'Gym',
                'difficulty': 'Advanced',
                'duration': 90,
                'calories_estimate': 900,
                'instructions': [
                    'Heavy deadlifts - 5 sets of 5 reps',
                    'Overhead press - 4 sets of 8 reps',
                    'Battle rope slams - 4 sets of 30 seconds',
                    'Sledgehammer swings - 3 sets of 20 reps',
                    'Core work - 3 sets of planks (1 min each)'
                ]
            },
            {
                'name': 'Black Widow Agility Circuit',
                'description': 'Spy-level agility and flexibility training',
                'activity_type': 'Gym',
                'difficulty': 'Intermediate',
                'duration': 45,
                'calories_estimate': 450,
                'instructions': [
                    'Jump rope - 3 minutes',
                    'Box jumps - 3 sets of 15',
                    'Burpees - 3 sets of 12',
                    'Mountain climbers - 3 sets of 30 seconds',
                    'Yoga flow - 10 minutes'
                ]
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Speed force-inspired sprint workout',
                'activity_type': 'Running',
                'difficulty': 'Advanced',
                'duration': 30,
                'calories_estimate': 400,
                'instructions': [
                    'Dynamic warmup - 5 minutes',
                    '100m sprint at max speed',
                    'Rest for 2 minutes',
                    'Repeat sprints 10 times',
                    'Cool down jog - 5 minutes'
                ]
            },
            {
                'name': 'Aquaman Ocean Endurance',
                'description': 'Swimming workout for Atlantean stamina',
                'activity_type': 'Swimming',
                'difficulty': 'Intermediate',
                'duration': 60,
                'calories_estimate': 550,
                'instructions': [
                    'Warm up with 200m easy swim',
                    '400m freestyle at moderate pace',
                    '200m backstroke',
                    '200m breaststroke',
                    '4 x 50m sprint with 1 min rest',
                    'Cool down with 200m easy swim'
                ]
            },
            {
                'name': 'Hulk Smash Power',
                'description': 'Maximum strength and power workout',
                'activity_type': 'Gym',
                'difficulty': 'Advanced',
                'duration': 120,
                'calories_estimate': 1000,
                'instructions': [
                    'Heavy squats - 5 sets of 3 reps',
                    'Bench press - 5 sets of 3 reps',
                    'Deadlifts - 5 sets of 3 reps',
                    'Tire flips - 3 sets of 10',
                    'Farmer walks - 3 sets of 50m',
                    'Cool down stretching'
                ]
            },
            {
                'name': 'Wonder Woman Warrior Training',
                'description': 'Amazonian warrior conditioning',
                'activity_type': 'Gym',
                'difficulty': 'Intermediate',
                'duration': 75,
                'calories_estimate': 700,
                'instructions': [
                    'Kettlebell swings - 4 sets of 15',
                    'Turkish get-ups - 3 sets of 5 per side',
                    'Weighted lunges - 3 sets of 12 per leg',
                    'Push-ups - 3 sets to failure',
                    'Core circuit - 15 minutes',
                    'Stretching - 10 minutes'
                ]
            },
            {
                'name': 'Batman Night Patrol',
                'description': 'Detective endurance training',
                'activity_type': 'Running',
                'difficulty': 'Intermediate',
                'duration': 60,
                'calories_estimate': 600,
                'instructions': [
                    'Easy paced run - 10 minutes',
                    'Tempo run at 75% effort - 30 minutes',
                    'Hill sprints - 5 x 30 seconds',
                    'Recovery jog - 10 minutes',
                    'Stretching - 10 minutes'
                ]
            },
            {
                'name': 'Superhero Recovery Yoga',
                'description': 'Gentle yoga for active recovery',
                'activity_type': 'Yoga',
                'difficulty': 'Beginner',
                'duration': 45,
                'calories_estimate': 150,
                'instructions': [
                    'Child pose - 3 minutes',
                    'Cat-cow stretches - 5 minutes',
                    'Downward dog - 2 minutes',
                    'Warrior poses - 10 minutes',
                    'Pigeon pose - 5 minutes per side',
                    'Savasana - 10 minutes'
                ]
            }
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workout suggestions')
