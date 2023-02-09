from home.models import Subscription
from rest_framework.response import Response
from django.http import JsonResponse
from home.models import SubscriptionOrder
import datetime

class SubscriptionCheck(object):
    def __init__(self,get_response) -> None:
        self.get_response = get_response

    def __call__(self, request): #here we apply all logic
        # print(request.path) #route ko check krege ki actual m kaunsa route hai
        url_path = set((request.path).split('/'))
        if 'blog_detail' in url_path :
                # print('yes found')
                if not request.user.is_authenticated:
                    return JsonResponse({
                        'status' : False,
                        'message' : 'you are not authenticated',
                        'data' : {}
                    },
                    content_type = 'application/json'
                    )

                else:
                    subscription_order = SubscriptionOrder.objects.filter (
                        user = request.user,
                        is_paid = True,
                        subscription_end_date__gte = datetime.datetime.today().date() #current date se jyada ki date chahye ho tb
                    )

                if not subscription_order.exists():
                    return JsonResponse({
                        'status' : False,
                        'message' : 'you havent purchased the subscription',
                        'data' : {}
                    },
                    content_type = 'application/json'
                    )
        return self.get_response(request)
        