from django.shortcuts import render
import random


def index(request):
    return render(request, 'core/index.html')

def singup(request):
    return render(request, 'core/singup.html')

def magic(request):
    if request.method == "POST":
        random_number = random.randint(1,10)
        user_guess = int(request.POST['user_guess'])
        if random_number == user_guess:
            result = 'молодец ты выиграл'
        else:
             result = f'ты проиграл magic number is: {random_number}'
        return render(request, 'core/magic.html', {'result':result})
    return render(request, 'core/magic.html')