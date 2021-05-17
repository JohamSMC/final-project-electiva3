from datetime import date, datetime

from django.http.response import JsonResponse
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
    activity = Activity.objects.get(id_activity=id_activity)
    activity.grade = name_grade
    activity.date_finished = name_date_finished
    activity.state = True
    activity.save()
    # print('ID_ACTIVITY', id_activity)
    # print('NAME_GRADE', name_grade)
    print('name_date_finished', name_date_finished)

    return redirect("index")


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
