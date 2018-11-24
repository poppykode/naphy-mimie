from django.shortcuts import render
from django.views.generic.list import ListView,View
from django.views.generic import CreateView
from .models import Gallery,RSVP,BridalTeam,Contact
from django.contrib import messages
from .forms import RSVPForm,ContaUsForm

# Create your views here.
# class HomeView(View):
#     template_name = 'wedding/index.html'

#     def get(self, request):
#        return render(request, self.template_name)

class GalleryView(ListView):
    template_name = 'wedding/gallery.html'
    context_object_name = 'gallery_list'
    model = Gallery
    queryset = Gallery.objects.all()

class RSVPView(CreateView):
    model = RSVP
    form_class = RSVPForm
    template_name='wedding/rsvp.html'

    def form_valid(self, form):
        messages.success(self.request, "RSVP successfully Sent.")
        return super(RSVPView, self).form_valid(form)

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContaUsForm
    template_name= 'wedding/contact_us.html'

    def form_valid(self, form):
        messages.success(self.request, "Message successfully Sent.")
        return super(ContactCreateView, self).form_valid(form)

class HomeView(ListView):
    template_name = 'wedding/index.html'
    context_object_name = 'bridal_team_list'
    model = BridalTeam
    queryset = BridalTeam.objects.all()


    