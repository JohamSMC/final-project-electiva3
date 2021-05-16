from django.shortcuts import render

from .models import Activity, Subject, TypeActivity


def index(request):
    all_subjects = Subject.objects.all()
    all_activities = Activity.objects.all()
    all_type_activities = TypeActivity.objects.all()
    context = {
        'subjects': all_subjects,
        'activities': all_activities,
        'type_activities': all_type_activities
    }
    return render(request, 'subjects/index.html', context)
