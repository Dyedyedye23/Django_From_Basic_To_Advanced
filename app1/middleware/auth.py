from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info == '/login':
            return None

        info = request.session.get('info')
        if info:
            return None
        return redirect('/login')