import time
from datetime import datetime

def duration_renderer_before(request): 

    current_datetime = datetime.now()


    return { 
        'time': current_datetime.strftime('%H:%M'),
        'date': current_datetime.strftime('%d %B %Y')
    }

        