from django.shortcuts import render

from users.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect, reverse

from complaints.models import Complaint, Feedback
from complaints.forms import FeedbackForm, ComplaintForm, ComplaintFeedbackForm
from users.models import Staff

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
                    return redirect(reverse('home'))
                messages.error(request,"Sorry! You do not have an admin privileges. Login as a staff.")
                return render(request, 'administrator/login.html', context={"form":form})
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    
        
    return render(request, 'administrator/login.html', context={"form":form})






def staff_dashboard(request):
    all_complaints = Complaint.objects.filter().count()
    solved = Complaint.objects.filter(status='Solved').count()
    pending = Complaint.objects.filter(status='Pending').count()
    in_progress = Complaint.objects.filter(status='In Progress').count()
    
    staff_name = Staff.objects.filter(employee=request.user).first().department
    
    unsolved = pending+in_progress
    
    context = {'all_complaints': all_complaints, 'solved':solved, 'unsolved':unsolved, 'staff_name':staff_name}
    
    return render(request, 'dashboard/home.html', context)





@login_required
def staff_solved_compliants(request):
    
    staff = Staff.objects.filter(employee=request.user).first()
    
    complaints = Complaint.objects.filter(status='Solved', department=staff.department)
    staff_name = Staff.objects.filter(employee=request.user).first().department
    print(staff.department)
    print(complaints)
    
    context = {'complaints':complaints, 'staff_name':staff_name}
    
    return render(request, 'dashboard/solved_compliants.html', context)




@login_required
def staff_unsolved_compliants(request):
    #ComplaintFeedbackForm
    staff = Staff.objects.filter(employee=request.user).first()
    
    complaints = Complaint.objects.filter(department=staff.department)
    staff_name = Staff.objects.filter(employee=request.user).first().department
    context = {'complaints':complaints, 'staff_name':staff_name}
    
    
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
    
    return render(request, 'dashboard/unsolved_compliants.html', context)





@login_required
def dashboard(request):
    all_complaints = Complaint.objects.filter(user=request.user).count()
    solved = Complaint.objects.filter(user=request.user, status='Solved').count()
    pending = Complaint.objects.filter(user=request.user, status='Pending').count()
    in_progress = Complaint.objects.filter(user=request.user, status='In Progress').count()
    
    unsolved = pending+in_progress
    
    context = {'all_complaints': all_complaints, 'solved':solved, 'unsolved':unsolved}
    
    return render(request, 'dashboard/home.html', context)





@login_required
def make_complain(request):
    
    form = ComplaintForm()
    complaints = Complaint.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        #print(form)
        if form.is_valid():
            
            user_id = form.save(commit=False)
            user_id.user = request.user
            user_id.save()
            
            #print('Company profile created successfully')
            messages.success(request, 'Compliant created successfully')
            return redirect(reverse('make_complain'))
        else:
            messages.error(request, 'Compliant not created')
            #print
    
    context = {'complaints':complaints, 'form':form}
    return render(request, 'dashboard/complain.html', context)




@login_required
def solved_compliants(request):
    
    complaints = Complaint.objects.filter(user=request.user, status='Solved')
    
    context = {'complaints':complaints}
    
    return render(request, 'dashboard/solved_compliants.html', context)


@login_required
def unsolved_compliants(request):
    
    complaints = Complaint.objects.filter(user=request.user)
    context = {'complaints':complaints}
    
    return render(request, 'dashboard/unsolved_compliants.html', context)



def update_compliant(request):
    
    if request.method == "POST":
        id = request.POST.get('id')
        
        compliant = Complaint.objects.filter(id=id).last()
        
        form = ComplaintForm(request.POST, instance=compliant)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Compliant updated successfully')
        else:
            messages.error(request, 'Compliant not updated')
    
    return redirect(reverse('make_complain'))




def delete_compliant(request):
    
    if request.method == "POST":
        id = request.POST.get('id')
        
        compliant = Complaint.objects.filter(id=id).last()
        
        if compliant:
            compliant.delete()
            
            messages.success(request, 'Compliant updated successfully')
        else:
            messages.error(request, 'Compliant not updated')
    
    return redirect(reverse('make_complain'))






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