# -*- coding: utf-8 -*-

def get_site(request):
    """
        - Used to get current Site
    """
    if request.is_secure():
        site = "https://" + request.META['HTTP_HOST']
    else:
        site = "http://" + request.META['HTTP_HOST']
    return site
