from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,profileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):  #ye request first time me get ki hi rhegi to get a form bad me post ki rhegi to jb post ki rhe to save krlo data
	if request.method=='POST':
		form=UserRegistrationForm(request.POST)  #whi post request jaegi is form me shyd esa kuch
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username} now you can login')
			return redirect('login')
	else:
		form=UserRegistrationForm()
	return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Account info updated')
			return redirect('profile')
		
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=profileUpdateForm(instance=request.user.profile)
		
	context={
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request,'users/profile.html',context)