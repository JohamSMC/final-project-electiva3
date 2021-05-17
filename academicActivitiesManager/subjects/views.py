from datetime import date, datetime

from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from .models import Activity, Subject, TypeActivity


def index(request):
    all_subjects = Subject.objects.all()
    all_activities = Activity.objects.all()
    all_type_activities = TypeActivity.objects.all()

    for subject in all_subjects:
        total_completed = 0
        for activity in all_activities:
            if (activity.subject_id == subject.id_subject) and (activity.state):
                total_completed = total_completed + activity.percentage
        subject.total_completed = total_completed
        subject.save()

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
    print("//////////////")
    print(id_activity)
    print("//////////////")
    activity = Activity.objects.get(id_activity=id_activity)
    subject = Subject.objects.get(id_subject=activity.subject_id)
    name_grade = request.POST['grade']
    name_date_finished = request.POST['date_finished']
    new_percentage = request.POST['percentage']
    state = request.POST['state']
    print("//////////////")
    print(new_percentage)
    print("//////////////")
    type_activity = TypeActivity.objects.get(id_activity=request.POST["typeActivity"])

    all_activities = Activity.objects.all()

    new_total_percentage = int(new_percentage) + subject.total_completed - activity.percentage
    if new_total_percentage > 100:
        all_subjects = Subject.objects.all()
        all_type_activities = TypeActivity.objects.all()
        context = {
            'subjects': all_subjects,
            'activities': all_activities,
            'type_activities': all_type_activities,
            "error_update_activity": True
        }
        return render(request, 'subjects/index.html', context)
    else:
        subject.total_completed = new_total_percentage
        subject.save()
        activity.grade = name_grade
        activity.date_finished = name_date_finished
        activity.state = state
        activity.percentage = new_percentage
        activity.type_activity = type_activity
        activity.save()

        return redirect("index")


def add_activity(request):
    if request.method == 'POST':
        name_subject = request.POST["nameSubject"]
        subject = Subject.objects.get(name=name_subject)
        all_activities = Activity.objects.all()
        name_activity = request.POST["nameActivity"]
        description_activity = request.POST["descriptionActivity"]
        type_activity = TypeActivity.objects.get(id_activity=request.POST["typeActivity"])
        date_finished = request.POST["activityDateFinished"]
        percentage_activity = request.POST["percentageActivity"]

        total_percent = 0

        for activity in all_activities:
            if activity.subject_id == subject.id_subject:
                total_percent = total_percent + activity.percentage
        print("//////////////")
        print(total_percent)
        print("//////////////")
        if total_percent + int(percentage_activity) > 100:
            all_subjects = Subject.objects.all()
            all_activities = Activity.objects.all()
            all_type_activities = TypeActivity.objects.all()
            context = {
                'subjects': all_subjects,
                'activities': all_activities,
                'type_activities': all_type_activities,
                "error_add_activity": True
            }
            return render(request, 'subjects/index.html', context)
        else:

            new_activity = Activity(
                name=name_activity, description=description_activity, type_activity=type_activity,
                subject=subject, date_created=date.today(),
                date_finished=date_finished, percentage=percentage_activity)
            new_activity.save()

            return redirect('index')


def notification_task(request):
    all_tasks = Activity.objects.filter(state=False)
    tasks = []
    print("----------------")
    time_now_str = datetime.utcnow().strftime('%Y-%m-%d %H:%M')
    # time_now_str = datetime.utcnow()

    for task in all_tasks:
        time_finish_str = task.date_finished.strftime('%Y-%m-%d %H:%M')
        # time_now = datetime.strptime('%Y-%m-%d %H:%M', time_now_str)
        time_now = datetime.strptime(time_now_str, '%Y-%m-%d %H:%M')
        time_finish = datetime.strptime(time_finish_str, '%Y-%m-%d %H:%M')
        time_rest = time_finish - time_now
        time_rest = time_rest.days
        print(time_rest)
        if time_rest <= 5:
            tasks.append({"name": task.name,
                         "date_finished": task.date_finished.strftime('%Y-%m-%d'),
                          "time_rest": time_rest})
    print("----------------")
    response = {"tasks": tasks}
    return JsonResponse(response)
