from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse

from .models import Note

listOfItems = {
    'edit': 'Επεξεργασία',
    'delete': 'Διαγραφή'

}


# Start


def delete(request, id):
    instance = get_object_or_404(Note, id=id)
    instance.delete()


    q = Note.objects.all()

    context = {
        'txt': q,
    }

    return render(request, 'dashboard.html', context)


def edit(request, id):
    instance = get_object_or_404(Note, id=id)

    context = {
        'instance': instance
    }

    return render(request, 'edit.html', context)


def add(request):
    if request.method == 'POST':
        note = Note(
            note_text=request.POST['note_input']
        )
        note.save()

        q = Note.objects.all()

        context = {
            'txt': q,
        }

        return render(request, 'dashboard.html', context)


def dashboard(request):
    q = Note.objects.all()

    context = {
        'txt': q,
    }

    return render(request, 'dashboard.html', context)


def save_edit(request, id):
    query = Note.objects.get(id=id)
    query.note_text = request.POST['note_input']
    query.save()

    q = Note.objects.all()

    context = {
        'txt': q,
    }

    return render(request, 'dashboard.html', context)
