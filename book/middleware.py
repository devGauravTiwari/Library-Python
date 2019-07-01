from django.shortcuts import redirect
class RestrictIfsignup(object):
    restrict_before_authentication =['/book/']
    restrict_after_authentication =['/signup/']
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #before view called
        if request.user.is_authenticated:
            if(request.get_full_path() in self.restrict_after_authentication):
                response = redirect('/')
        else:
            if(request.get_full_path() in self.restrict_before_authentication):
                response = redirect('/login')
        response = self.get_response(request)
        #after view is called
        return response
