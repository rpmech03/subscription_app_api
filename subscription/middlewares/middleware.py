from home.models import Subscription

class SubscriptionCheck(object):
    def __init__(self,get_response) -> None:
        self.get_response = get_response

    def __call__(self, request): #here we apply all logic
        # print(request.path) #route ko check krege ki actual m kaunsa route hai
        url_path = set((request.path).split('/'))
        if 'blog_detail' in url_path:
                # print('yes found')
                if not request.user.is_authenticated:
                    
        return self.get_response(request)
        