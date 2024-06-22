from django.utils.timezone import now
from django.http import JsonResponse
from .models import CustomUser, RequestLog, UserType


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin'):
            return self.get_response(request)

        response = self.get_response(request)
        if request.user:
            RequestLog.objects.create(
                username=request.user.username,
                path=request.path,
                method=request.method,
                timestamp=now()
            )
        return response                     

class UserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        response = self.get_response(request)
        if request.user and request.user.is_authenticated:
            user_type = request.user.user_type
            if user_type not in [UserType.MANAGER.value, UserType.CUSTOMER.value]:
                return JsonResponse({'error': 'Invalid user type'}, status=403)
            else:
                request.user_type = user_type
        else:
            request.user_type = None
            
        return response
