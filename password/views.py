from .models import Generate
from .forms import GenerateForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .maincode.create import Create
from .maincode.dico import Dico
from .maincode.check import calculate_password_strength
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def genpassp(request):
    if request.method == 'POST':
        passw = Generate.objects.get(id=108121)
        form = GenerateForm(request.POST, instance=passw)
        
        if form.is_valid():
            scale = form.cleaned_data.get('scale')
            special = form.cleaned_data.get('special')
            simple = form.cleaned_data.get('simple')
            dico_scale = form.cleaned_data.get('dico_scale')
            separator = form.cleaned_data.get('separator')
            create = Create(scale, special, simple)
            passw.mdp = create.genpass()
            passphrase = form.cleaned_data.get('passphrase')
            passphrase_created = create.generate_passphrase(passphrase) if passphrase else ""
            dico = Dico(dico_scale,separator)
            passw.passmot = dico.password()
            passmot = passw.passmot
            form.save()
            password = form.cleaned_data.get('password')
            range_password = passw.mdp
            strength_range = calculate_password_strength(range_password) 
            logger.debug(f"Received password: {password}")
            logger.debug(f"Received passphrase: {passphrase}")
            strength = calculate_password_strength(password)  
            logger.debug(f"Calculated strength: {strength}")
            response_data = {
                'separator' : separator,
                'dico_scale' : dico_scale,
                'passmot' : passmot,
                'passphrase_created' : passphrase_created,
                'passphrase': passphrase,
                'simple': simple,
                'special': special,
                'scale': scale,
                'range_password': range_password,
                'percent_range': strength_range['percent'],
                'colorClassRange': strength_range['colorClass'],
                'message_range': strength_range['message'],
                'percent': strength['percent'],
                'colorClass': strength['colorClass'],
                'message': strength['message']
            }
            return JsonResponse(response_data)
        else:
            logger.debug("Form is not valid")
            logger.debug(f"Form errors: {form.errors}")
            return JsonResponse({'error': 'Invalid form data', 'form_errors': form.errors})
    else:
        logger.debug("Invalid request method")
        return JsonResponse({'error': 'Invalid request method'})



def genpass(request):
    passw = Generate.objects.get(id=108121)
    if request.method == 'POST':
        form = GenerateForm(request.POST, instance=passw)
        if form.is_valid():
            create = Create(passw.scale,passw.special,passw.simple)
            passw.mdp = create.genpass()
            passw.password = ""
            passw.passphrase = ""
            form.save()
            return render(request, 'password/genpass_print.html', {'form':form, 'gen':passw})
    else:
        
        form = GenerateForm(instance=passw)
    return render(request, 'password/genpass.html', {'form':form, 'gen':passw})

