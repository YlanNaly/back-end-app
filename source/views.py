import logging
import json
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import UserLoginForm

# Configure the logger
logger = logging.getLogger('login_logger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/login_log.txt')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - Request Data: %(request_data)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            cliId = request_data.get('cliId', '')
            username = request_data.get('username', '')
            password = request_data.get('password', '')
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON data in the request'}, status=400)

        # Log the request data to a file
        request_data_to_log = {
            'cliId': cliId,
            'username': username,
            'password': password
        }
        logger.info("User logged in", extra={'request_data': json.dumps(request_data_to_log, indent=4)})

        return JsonResponse({'message': 'Login successful'})
    else:
        try:
            request_data = json.loads(request.body)
            cliId = request_data.get('cliId', '')
            username = request_data.get('username', '')
            password = request_data.get('password', '')
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Invalid JSON data in the request'}, status=400)

        request_data_to_log = {
            'cliId': cliId,
            'username': username,
            'password': password
        }
        logger.info("User logged in", extra={'request_data': json.dumps(request_data_to_log, indent=4)})
        return JsonResponse({'message': 'Invalid request method'}, status=405)
