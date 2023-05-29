"""Writing custom API endpoints."""

#1 viws.py
...
from django.shortcuts import render
from ..chapter-3.models import ..., Seller
from rest_framework.permissions import IsAuthenticated
from rest_framework.viws import APIView
...

class GetSellerHTMLView(APIView):
    permission_classes = [IsAuthenticated]
    template_name = 'chapter_8/details/seller.html'

    def get(self, request, format=None, id=0, *args, **kwargs):
        if  request.user.is_authenticated and request.user.has_perm
        ('chapter_3.view_seller'):
            try:
                seller = Seller.objects.get(id=id)
            except Seller.DoesNotExist:
                seller = None
        else:
            seller = None

        context = {'seller': seller,}

        return render(
                request,
                self.template_name,
                context = context
        )
