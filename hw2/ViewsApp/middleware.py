from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.cache import cache
from time import sleep

class CacheItemsMiddleware:
    def __init__(self, next):
        self.next = next

    def __call__(self,req: HttpRequest):
        path = req.path.replace('/', '').upper()

        if cache.has_key(path, 1):
            result = cache.get(path, 1)
            cache.set(path, result, 120, 1)
            return result
        
        result = self.next(req)
        print(type(result))
        cache.add(path, result, 10, 1)
        return result
    

class RestrictByIPMiddleware:
    def __init__(self, next):
        self.next = next

    def __call__(self, req: HttpRequest ):
        ip = req.META.get("REMOTE_ADDR")
        print(ip)
        if cache.has_key(ip, 1):
            attempt = cache.get(ip, 1)
            print(attempt)
            if attempt >=5:
                return HttpResponse("Too many attempts")
            else:
                attempt += 1
                cache.set(ip, attempt, 60, 1)
        

        cache.add(ip, 1, 60, 1)
        return self.next(req)