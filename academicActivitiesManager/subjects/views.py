from datetime import date

from django.shortcuts import redirect, render

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


def addsubject(request):
    if request.method == 'POST':
        subject_name = request.POST["subjectName"]
        teacher_name = request.POST["teacherName"]
        new_subjects = Subject(name=subject_name, teacher=teacher_name, date_created=date.today())
        new_subjects.save()
        return redirect('index')
    return render(request, 'subjects/add.html')


def update_activity(request, id_activity):
    name_grade = request.POST['grade']
    name_date_finished = request.POST['date_finished']
    print('ID_ACTIVITY', id_activity)
    print('NAME_GRADE', name_grade)
    print('name_date_finished', name_date_finished)

    return redirect("index")
