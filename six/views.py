from django.shortcuts import render, get_object_or_404, redirect
from .models import Six
from django.urls import reverse
from .forms import createForm

# Create your views here.
def main(request):
    sixs = Six.objects.all
    return render(request, 'main.html', {'six':sixs})

def update(request, change_id):
    change_obj = get_object_or_404(Six, pk=change_id)
    if request.method == "POST":
        change_obj.imagename = request.POST['imagename']
        change_obj.imageinfo = request.POST['imageinfo']
        change_obj.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request,'update.html',{'change_key':change_obj})


def new(request):
    global Channel 
    return render(request, '.html')
    Six = Six()
    Six.photo = request.POST['photo']
    Six.imagename = request.POST['imagename']
    Six.imageinfo = request.POST['imageinfo']
    Six.save()
    return redirect('main')

def new(request) : 
    form = createForm()
    if request.method == 'POST':
        pass
    elif request.method =='GET':
        form = createForm()
        return render(request, 'new.html', {'form':form})
    else:
        pass


def delete(request, delete_id):
    delete_obj = get_object_or_404(Six, pk=delete_id)
    delete_obj.delete()
    return redirect('main')