from django.shortcuts import render, redirect
import random
from datetime import datetime
from webapp.forms import CollectData
from webapp.models import UserData

quotes = [
    {"text": "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.", "author": "Helen keller"},
    {"text": "It is during our darkest moments that we must focus to see the light.", "author": "Aristotle"},
    {"text": "Let noble thoughts come to us from all directions.", "author": "Rigveda"},
    {"text": "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.", "author": "Gautama Buddha"},
    {"text": "What is the essence of life? To serve others and to do good.", "author": "Swami Vivekananda"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "A.P.J. Abdul Kalam"},
    {"text": "The mind is everything. What you think you become.", "author": "Buddha"},
]

def index(request):
    generate_quotes = random.choice(quotes)
    dt_time = datetime.now()
    context = {'quote_text': generate_quotes['text'], 
               'quote_author': generate_quotes.get('author', ''),
                'current_date': dt_time.strftime('%Y-%m-%d'), 
                'current_time': dt_time.strftime('%H-%M-%S'),
            }    # will retrieve author related to that quote using get() and the empty string for default value of that key
    return render(request, 'webapp/index.html', context)

def user_data(request):
    if request.method == 'POST':
        form = CollectData(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webapp:success')
    else:
        form = CollectData()
    return render(request, 'webapp/feedback.html', {'form': form})

def display_data(request):
    usr_data = UserData.objects.order_by('-id').first() # display lastly submitted data
    data = {'usr_data': usr_data}
    return render(request, 'webapp/user_details.html', data)