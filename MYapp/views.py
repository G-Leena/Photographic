from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .utils import image_saver 


from MYapp.models import Contact, Image, UpperSlider, MiddleSlider

def renderPage(req):
    image_qs = Image.objects.all()
    memory_img = image_qs.filter(image_category="memory")
    wedding_img = image_qs.filter(image_category="wedding") 
    travel_img = image_qs.filter(image_category="travel") 
    portrait_img = image_qs.filter(image_category="portrait") 
    fashion_img = image_qs.filter(image_category="fashion") 
    up_sl_img_qs = UpperSlider.objects.all() 
    mid_sl_img_qs = MiddleSlider.objects.all()
    return render(req,"index.html",
                 {"up_sl_imgs": up_sl_img_qs,
                 "mid_sl_imgs": mid_sl_img_qs,
                 "memory_img": memory_img,
                 "wedding_img": wedding_img,
                 "travel_img": travel_img,
                 "portrait_img": portrait_img,
                 "fashion_img": fashion_img,
                 "images": image_qs,})

# -----------------------------------------------------
# Contact us SECTION
# -----------------------------------------------------


def contactus(req):
	return render(req,"contactcp.html")
	
def contact_form(request):
    if request.method == 'POST':
        obj = Contact()
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.subject = request.POST.get('subject')
        
        obj.save()

        # Display a success message
        messages.success(request, 'Your message has been sent. Thank you!')

        # Redirect to the contactus page after successful form submission
        return redirect('/contactus')
    else:
        return render(request, "/contactus")

# def contact_form(req):
# 	if req.method=='POST' :
# 		obj=Contact()
# 		obj.name=req.POST.get('name')
# 		obj.email=req.POST.get('email')
# 		obj.phone=req.POST.get('phone')
# 		obj.subject=req.POST.get('subject')
		
# 		obj.save()
# 		return HttpResponse(req,message='TRUE')
# 		# return HttpResponseRedirect('/contactus?submitted=True')
# 	else:
# 		return render(req,"contactus")
	
def enquiry(req):
	return render(req,"course.html")

def admin_login(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print(user, "8888888888888")
        if user and user.is_superuser:
            login(request, user)
            print(user)
            return redirect("admin_home")
        else:
            data["error"] = "Please provide valid admin username and password"
    return render(request, "admin/admin_login.html", {"data":data})

def admin_logout(request):
    logout(request)
    return redirect("admin_login")

def admin_home(request):
    if request.user.is_superuser:
        image_qs = Image.objects.all().order_by("-created_at")
        return render(request, "admin/admin_home.html", {"images":image_qs})
    else:
        return redirect("admin_login")

def add_or_update_img(request, id=None):
    if request.user.is_superuser:
        if request.method == "GET" and id:
            slider = request.GET.get("slider", None)
            if slider == "upper":
                image = UpperSlider.objects.filter(id=id).first()
            elif slider == "middle":
                image = MiddleSlider.objects.filter(id=id).first()
            else:
                image = Image.objects.filter(id=id).first()
            if image:
                return render(request, "admin/add_update_image.html", {"image": image})

        if request.method == "POST":
            # import pdb; pdb.set_trace()
            image = request.FILES.get("image")
            category = request.POST.get("category")
            slider = request.GET.get("slider", None)
            if id:
                if slider == "upper":
                    image_obj = UpperSlider.objects.filter(id=id).first()
                    image_saver(image_obj, image, category)
                    return redirect("upper_slider")

                elif slider == "middle":
                    image_obj = MiddleSlider.objects.filter(id=id).first()
                    image_saver(image_obj, image, category)
                    return redirect("middle_slider")
                else:
                    image_obj = Image.objects.filter(id=id).first()                
                    image_saver(image_obj, image, category)
                
                # if  image_obj:
                #     if image:
                #         image_obj.image = image
                #     if category:
                #         image_obj.image_category = category
                #     image_obj.save()
            else:
                if slider == "upper":
                    UpperSlider.objects.create(image_category=category, image=image)
                    return redirect("upper_slider")
                elif slider == "middle":
                    MiddleSlider.objects.create(image_category=category, image=image)
                    return redirect("middle_slider")
                else:    
                    Image.objects.create(image_category=category, image=image)
            
            return redirect("admin_home")
        
        return render(request, "admin/add_update_image.html")
    else:
        return redirect("admin_login")        


def delete_image(request, id):
    slider = request.GET.get("slider", None)
    if slider == "upper":
        UpperSlider.objects.filter(id=id).delete()
        return redirect("upper_slider")
    elif slider == "middle":
        MiddleSlider.objects.filter(id=id).delete()
        return redirect("middle_slider")
    else:
        Image.objects.filter(id=id).delete()
                       
    return redirect("admin_home")

def image_view(request, category):
    image_qs = Image.objects.filter(image_category=category)
    # image_qs = Image.objects.all()
    print(image_qs.count())
    return render(request, "admin/image_view.html", {"images": image_qs})


def upper_slider(request):
    image_qs = UpperSlider.objects.all().order_by("-created_at")
    return render(request, "admin/admin_home.html", {"images":image_qs, "slider": "upper"})


def middle_slider(request):
    image_qs = MiddleSlider.objects.all().order_by("-created_at")
    return render(request, "admin/admin_home.html", {"images":image_qs, "slider":"middle"})







 
