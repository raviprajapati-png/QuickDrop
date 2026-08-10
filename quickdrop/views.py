from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
from .models import TempNote
from .forms import NoteForm

def note_list(request):
    active_notes = TempNote.objects.filter(expires_at__gt=timezone.now()).order_by('-created_at')
    return render(request, 'quickdrop/note_list.html', {'notes': active_notes})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            
            # Extract duration inputs (defaulting to 0 if left blank)
            days = form.cleaned_data.get('days') or 0
            hours = form.cleaned_data.get('hours') or 0
            minutes = form.cleaned_data.get('minutes') or 0
            
            # Fallback to 1 minute minimum if everything is 0
            if days == 0 and hours == 0 and minutes == 0:
                minutes = 1

            # Add total calculated timedelta to current time
            note.expires_at = timezone.now() + datetime.timedelta(
                days=days, 
                hours=hours, 
                minutes=minutes
            )
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    
    return render(request, 'quickdrop/add_note.html', {'form': form})