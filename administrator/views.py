from django.http import JsonResponse
from django.shortcuts import render

from users.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect, reverse

from complaints.models import Complaint, Feedback, Notification
from complaints.forms import FeedbackForm, ComplaintForm, ComplaintFeedbackForm
from users.models import Staff
from django.contrib.auth.decorators import login_required

# Create your views here.
def admin_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect(reverse('admin_dashboard'))
                messages.error(request,"Sorry! You do not have an admin privileges. Login as a staff.")
                return render(request, 'administrator/login.html', context={"form":form})
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    
        
    return render(request, 'administrator/login.html', context={"form":form})





@login_required
def admin_dashboard(request):
    all_complaints = Complaint.objects.filter().count()
    solved = Complaint.objects.filter(status='Solved').count()
    pending = Complaint.objects.filter(status='Pending').count()
    in_progress = Complaint.objects.filter(status='In Progress').count()
    
    staff_name = Staff.objects.filter(employee=request.user).first().department
    
    unsolved = pending+in_progress
    notification_count = Notification.objects.filter(is_read=False).count()
    
    context = {'all_complaints': all_complaints, 'solved':solved, 'unsolved':unsolved, 'staff_name':staff_name, 'notification_count':notification_count}
    
    return render(request, 'administrator/home.html', context)





@login_required
def admin_solved_compliants(request):
    
    complaints = Complaint.objects.filter(status='Solved')
    notification_count = Notification.objects.filter(is_read=False).count()
    context = {'complaints':complaints, 'notification_count':notification_count}
    
    return render(request, 'administrator/solved_compliants.html', context)




@login_required
def admin_unsolved_compliants(request):
    #ComplaintFeedbackForm
    
    complaints = Complaint.objects.filter(status='Pending')
    notification_count = Notification.objects.filter(is_read=False).count()
    context = {'complaints':complaints, 'notification_count':notification_count}
    
    
    if request.method == "POST":
        id = request.POST.get('id')
        
        compliant = Complaint.objects.filter(id=id).last()
        print(complaints)
        form = ComplaintFeedbackForm(request.POST, instance=compliant)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Compliant updated successfully')
        else:
            print(form.errors.as_text())
            messages.error(request, 'Compliant not updated')
    
    return render(request, 'administrator/unsolved_compliants.html', context)





@login_required
def admin_dashboard(request):
    all_complaints = Complaint.objects.count()
    solved = Complaint.objects.filter(status='Solved').count()
    pending = Complaint.objects.filter(status='Pending').count()
    in_progress = Complaint.objects.filter(status='In Progress').count()
    notification_count = Notification.objects.filter(is_read=False).count()
    unsolved = pending+in_progress
    
    context = {'all_complaints': all_complaints, 'solved':solved, 'unsolved':unsolved, 'notification_count':notification_count, 'in_progress':in_progress}
    
    return render(request, 'administrator/home.html', context)



@login_required
def all_complaints(request):
    
    form = ComplaintForm()
    complaints = Complaint.objects.all()
    notification_count = Notification.objects.filter(is_read=False).count()
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        #print(form)
        if form.is_valid():
            
            user_id = form.save(commit=False)
            user_id.user = request.user
            user_id.save()
            
            #print('Company profile created successfully')
            messages.success(request, 'Compliant created successfully')
            return redirect(reverse('all_complaints'))
        else:
            messages.error(request, 'Compliant not created')
            #print
    
    context = {'complaints':complaints, 'form':form, 'notification_count':notification_count}
    return render(request, 'administrator/complaints.html', context)




@login_required
def inProgress(request):
    
    form = ComplaintForm()
    complaints = Complaint.objects.filter(status="In Progress")
    notification_count = Notification.objects.filter(is_read=False).count()
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        #print(form)
        if form.is_valid():
            
            user_id = form.save(commit=False)
            user_id.user = request.user
            user_id.save()
            
            #print('Company profile created successfully')
            messages.success(request, 'Compliant created successfully')
            return redirect(reverse('all_complaints'))
        else:
            messages.error(request, 'Compliant not created')
            #print
    
    context = {'complaints':complaints, 'form':form, 'notification_count':notification_count}
    return render(request, 'administrator/in_progress.html', context)





def update_compliant(request):
    
    if request.method == "POST":
        id = request.POST.get('id')
        
        compliant = Complaint.objects.filter(id=id).last()
        comment = request.POST.get('comment')
        status = request.POST.get('status')
        
        form = ComplaintForm(request.POST, instance=compliant)
        
        if form.is_valid():
            print(comment)
            new_comment = form.save(commit=False)
            new_comment.comment = comment
            new_comment.status = status
            new_comment.save()
            
            messages.success(request, 'Compliant updated successfully')
        else:
            messages.error(request, 'Compliant not updated')
    
    return redirect(reverse('all_complaints'))




def delete_compliant(request):
    
    if request.method == "POST":
        id = request.POST.get('id')
        
        compliant = Complaint.objects.filter(id=id).last()
        
        if compliant:
            compliant.delete()
            
            messages.success(request, 'Compliant updated successfully')
        else:
            messages.error(request, 'Compliant not updated')
    
    return redirect(reverse('all_complaints'))






def viewCompliant(request):
    id = request.GET.get('id', None)
    compliant = Complaint.objects.filter(id=id).first()
    context = {}
    
    if not compliant:
        context["code"] = 404
    else:
        context["code"] = 200
        context["id"] = compliant.id
        context["type"] = compliant.type
        context["details"] = compliant.details
        context["title"] = compliant.title
        context["status"] = compliant.status
        context["comment"] = compliant.comment
    print(context)
    return JsonResponse(context)



def view_notifications(request):
    notifications = Notification.objects.filter(is_read=False)
    notification_count = Notification.objects.filter(is_read=False).count()
    
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        notification = Notification.objects.get(id=notification_id)
        notification.is_read = True
        notification.save()
        return redirect('view_notifications')
    
    return render(request, 'administrator/notifications.html', {'notifications': notifications, 'notification_count': notification_count})