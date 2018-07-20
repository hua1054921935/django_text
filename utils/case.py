from django.http import HttpResponse


class Middleware_common(object):
    def process_request(self,request):
        # ip=request.META['REMOTE_ADDR']
        #
        #
        # return HttpResponse('禁止%s访问' %(ip))

        return None
    def process_response(self,request,response):
        ip = request.META['REMOTE_ADDR']
        if ip=='192.168.68.1':
            data='pc机'
        else:
            data='虚拟机'
        print('当前相应的是%s访问' % (data))
        return response


    def process_exception(self, request, exception):
        if exception:
            # print(exception)
            return HttpResponse('404')
        else:
            return None