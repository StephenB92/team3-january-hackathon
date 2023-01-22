from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import MyGoal
from .forms import MyGoalsForm


def all_goals(request):
    goals = MyGoal.objects.all()

    return render(request, 'goals/all_goals.html', {'goals': goals})


def goal_detail(request, goal_id):
    goal = get_object_or_404(MyGoal, pk=goal_id)

    return render(request, 'goals/goal_detail.html', {'goal': goal})



def add_goal(request):
    """ Add a goal """
    if request.method == 'POST':
        form = MyGoalsForm(request.POST)
        if form.is_valid():
            goal = form.save()
            messages.success(request, 'Successfully added goal!')
            print(goal.id)
            return redirect(reverse('goal_detail', args=[goal.id]))
        else:
            messages.error(request, 'Failed to add goal. Please ensure the form is valid.')
    form = MyGoalsForm()

    template = 'goals/add_goal.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



def edit_goal(request, goal_id):
    """ Edit a goal  """
    goal = get_object_or_404(MyGoal, pk=goal_id)
    if request.method == 'POST':
        form = MyGoalsForm(request.POST, request.FILES, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated goal!')
            return redirect(reverse('goal_detail', args=[goal.id]))
        else:
            messages.error(request, 'Failed to update goal. Please ensure the form is valid.')
    else:
        form = MyGoalsForm(instance=goal)
        messages.info(request, f'You are editing {goal.goal_name}')

    template = 'goals/edit_goal.html'
    context = {
        'form': form,
        'goal': goal,
    }

    return render(request, template, context)


@login_required
def delete_goal(request, goal_id):
    """ Delete a goal from the store """
    goal = get_object_or_404(Goal, pk=goal_id)
    goal.delete()
    messages.success(request, 'Goal deleted!')
    return redirect(reverse('goals'))

