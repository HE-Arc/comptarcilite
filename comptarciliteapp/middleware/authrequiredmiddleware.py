from django.contrib.auth.decorators import login_required


class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        #if getattr(view_func, 'login_exempt', False):
        #    return
        return
        
        print(self, request, view_func, view_args, view_kwargs)
        if request.user.is_authenticated:
            return
        else:
            return login_required(view_func)(request, *view_args, **view_kwargs)

        # You probably want to exclude the login/logout views, etc.

       