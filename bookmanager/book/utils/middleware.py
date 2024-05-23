from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare1(MiddlewareMixin):
    def process_request(self, request):
        # username = request.COOKIES.get("sessionid")
        # print("username: ", username)
        print("process_request1")

    def process_response(self, request, response):
        print("process_response1")
        # print(response)
        return response


class TestMiddleWare2(MiddlewareMixin):
    def process_request(self, request):
        # username = request.COOKIES.get("sessionid")
        # print("username: ", username)
        print("process_request2")

    def process_response(self, request, response):
        print("process_response2")
        # print(response)
        return response
