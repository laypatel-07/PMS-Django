from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import ProjectForm, UserRegistrationForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


from django.db.models import Count, Q
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'index.html')

def project_list(request):
    projects = Project.objects.all().order_by('-create_at') 
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm() 

    return render(request, 'project_form.html', {'form': form})

@login_required
def project_edit(request, project_id):
    project_obj = get_object_or_404(Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project_obj)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_list')  
    else:
        form = ProjectForm(instance=project_obj)

    return render(request, 'project_form.html', {'form': form})

@login_required
def project_delete(request, project_id):
    project_obj = get_object_or_404(Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        project_obj.delete()
        return redirect('project_list')
    return render(request, 'project_confirm_delete.html', {'project': project_obj})

def register(request):
      if request.method == 'POST':
       form =  UserRegistrationForm(request.POST)
       if form.is_valid():
           user = form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(request, user)
           return redirect('project_list')
      else:
       form = UserRegistrationForm()

      return render(request, 'registration/register.html', {'form': form})




# Add these view functions to your views.py

@login_required
def task_list(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project).order_by('status', '-priority', 'due_date')
    
    # Group tasks by status
    todo_tasks = tasks.filter(status='todo')
    in_progress_tasks = tasks.filter(status='in_progress')
    done_tasks = tasks.filter(status='done')
    
    context = {
        'project': project,
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks
    }
    
    return render(request, 'task_list.html', context)

@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    # Check if the user owns the project
    if project.user != request.user:
        return redirect('project_list')
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_list', project_id=project.id)
    else:
        form = TaskForm()
    
    return render(request, 'task_form.html', {'form': form, 'project': project})

@login_required
def task_edit(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id, user=request.user)
    task = get_object_or_404(Task, pk=task_id, project=project)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list', project_id=project.id)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'task_form.html', {'form': form, 'project': project, 'task': task})

@login_required
def task_delete(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id, user=request.user)
    task = get_object_or_404(Task, pk=task_id, project=project)
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_list', project_id=project.id)
    
    return render(request, 'task_confirm_delete.html', {'task': task, 'project': project})





@login_required
def dashboard(request):
    # Get user's projects
    user_projects = Project.objects.filter(user=request.user)
    
    # Get user's assigned tasks
    assigned_tasks = Task.objects.filter(assigned_to=request.user)
    
    # Calculate task statistics
    total_tasks = assigned_tasks.count()
    todo_tasks = assigned_tasks.filter(status='todo').count()
    in_progress_tasks = assigned_tasks.filter(status='in_progress').count()
    completed_tasks = assigned_tasks.filter(status='done').count()
    
    # Calculate completion percentage
    completion_percentage = 0
    if total_tasks > 0:
        completion_percentage = int((completed_tasks / total_tasks) * 100)
    
    # Get upcoming due tasks (due in the next 7 days)
    today = timezone.now().date()
    upcoming_tasks = assigned_tasks.filter(
        due_date__gte=today,
        due_date__lte=today + timezone.timedelta(days=7)
    ).order_by('due_date')
    
    # Get overdue tasks
    overdue_tasks = assigned_tasks.filter(
        due_date__lt=today,
        status__in=['todo', 'in_progress']
    ).order_by('due_date')
    
    # Get recent projects
    recent_projects = user_projects.order_by('-create_at')[:5]
    
    # Get high priority tasks
    high_priority_tasks = assigned_tasks.filter(priority='high').order_by('due_date')
    
    context = {
        'user_projects_count': user_projects.count(),
        'assigned_tasks_count': total_tasks,
        'todo_tasks_count': todo_tasks,
        'in_progress_tasks_count': in_progress_tasks,
        'completed_tasks_count': completed_tasks,
        'completion_percentage': completion_percentage,
        'upcoming_tasks': upcoming_tasks,
        'overdue_tasks': overdue_tasks,
        'recent_projects': recent_projects,
        'high_priority_tasks': high_priority_tasks,
    }
    
    return render(request, 'dashboard.html', context)


from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to dashboard instead of project_list
        else:
            # Handle invalid login
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            auth_login(request, user)  # Using auth_login to avoid confusion with the function name
            return redirect('dashboard')  # Changed from project_list to dashboard
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def task_menu(request):
    """
    View function for the task menu page.
    Shows all tasks with filtering options.
    """
    # Get all projects accessible to this user
    user_projects = Project.objects.filter(user=request.user)
    
    # Get filter parameters
    project_id = request.GET.get('project')
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    search = request.GET.get('search')
    
    # Base queryset - get tasks from user's projects or assigned to user
    tasks = Task.objects.filter(
        Q(project__user=request.user) | Q(assigned_to=request.user)
    ).distinct()
    
    # Apply filters
    if project_id:
        tasks = tasks.filter(project_id=project_id)
    
    if status:
        tasks = tasks.filter(status=status)
    
    if priority:
        tasks = tasks.filter(priority=priority)
    
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search)
        )
    
    # Group tasks by status
    todo_tasks = tasks.filter(status='todo').order_by('-priority', 'due_date')
    in_progress_tasks = tasks.filter(status='in_progress').order_by('-priority', 'due_date')
    done_tasks = tasks.filter(status='done').order_by('-updated_at')
    
    context = {
        'projects': user_projects,
        'selected_project_id': int(project_id) if project_id else None,
        'status': status,
        'priority': priority,
        'search': search,
        'todo_tasks': todo_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks,
    }
    
    return render(request, 'task_menu.html', context)

def home(request):

    return render(request, 'home.html')