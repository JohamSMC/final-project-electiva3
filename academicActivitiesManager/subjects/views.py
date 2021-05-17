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
    percentage = request.POST['percentage']
    state = request.POST['state']

    activity = Activity.objects.get(id_activity=id_activity)
    activity.grade = name_grade
    activity.date_finished = name_date_finished
    activity.state = state
    activity.percentage = percentage
    activity.save()
    # print('ID_ACTIVITY', id_activity)
    # print('NAME_GRADE', name_grade)
    # print('name_date_finished', name_date_finished)

    return redirect("index")


def add_activity(request):
    if request.method == 'POST':
        name_subject = request.POST["nameSubject"]
        subject = Subject.objects.get(name=name_subject)

        name_activity = request.POST["nameActivity"]
        description_activity = request.POST["descriptionActivity"]
        type_activity = TypeActivity.objects.get(id_activity=request.POST["typeActivity"])
        date_finished = request.POST["activityDateFinished"]
        percentage_activity = request.POST["percentageActivity"]

        new_activity = Activity(
            name=name_activity, description=description_activity, type_activity=type_activity,
            subject=subject, date_created=date.today(),
            date_finished=date_finished, percentage=percentage_activity)
        new_activity.save()

    return redirect('index')
