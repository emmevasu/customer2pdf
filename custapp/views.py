from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Cust
from django.views import View
from xhtml2pdf import pisa
from django.core import serializers
import json


def render_to_pdf(template_src, context_dict=None):
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
class input(View):
    def get(self,request):
        try:
            if request.method=='POST':
                name1=request.POST['t1']
                no1=request.POST['t2']
                age1=request.POST['t3']
                city1=request.POST['t4']
                f=Cust(name=name1,no=no1,age=age1,city=city1)
                f.save()
                # dt = serializers.serialize("json", Cust.objects.all())
                return HttpResponse("<html><body>data inserted</body></html>")
            else:
                return HttpResponse("<html><body>data notinserted</body></html>")
        except:
            return HttpResponse("<html><body>error occured</body></html>")
# data=Cust.objects.all()


data = {
    "name": "vaasu",
    "no": "9988776655",
    "age":"23",
    "city": "Vancouver",
    # "state": "WA",
    # "zipcode": "98663",
    #
    # "phone": "555-555-2345",
    # "email": "youremail@dennisivy.com",
    # "website": "dennisivy.com",
}


# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
class ViewPlain(View):
    def get(self, request, *args, **kwargs):
        dt=json.dumps(data)
        # txt = render_to_txt('pdf_template.html', data)
        return HttpResponse(dt,content_type='application/txt')



# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "vaasu_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def index(request):
    context = {}
    return render(request, 'index.html', context)
