# views.py
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import TextTransformation

from .utils import transform_text
from .forms import TransformPhonetiqueForm


def text_transform_view(request):
    form = TransformPhonetiqueForm()
    transform = TextTransformation.objects.all().order_by('pk')
    context = {
                'transform':transform,
                'form':form
                }
    if request.method == 'POST':
        form = TransformPhonetiqueForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            fonctions = [key for key, value in cleaned_data.items() if value and key != 'text']
            original_text = cleaned_data['text'] 
            print(fonctions)
            transformed_text = transform_text(original_text,fonctions)
            TextTransformation.objects.create(original_text=original_text, transformed_text=transformed_text)
            
            # context['transformed_text'] = transformed_text
            # context['original_text'] = original_text   

    return render(request, 'phonetique/index.html',context=context )


def delete_history(request,id):
    history = get_object_or_404(TextTransformation,pk=id)
    history.delete()
    messages.success(request,'Supression effectuer avec success')
    return redirect('text_transform')
    
def detail_history(request,id):
    history = get_object_or_404(TextTransformation,pk=id)
    original_text = history.original_text
    hystory_text = history.transformed_text
    context ={
                'original_text' : original_text,
                'transformed_text' : hystory_text
            }
    return render(request, 'phonetique/detail.html', context)
