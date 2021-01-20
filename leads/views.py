from django.shortcuts import render, redirect, reverse
from .models import User, Agent, Lead
from .forms import LeadForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing_page.html"

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead_list")

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse('leads:lead_list')

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead_list')

# def landing_page(request):
#     return render(request,"landing_page.html")

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads':leads,
#     }
#     return render(request,'leads/lead_list.html',context)

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead':lead,
#     }
#     return render(request, 'leads/lead_detail.html', context)

# def create_lead(request):
#     form = LeadForm

#     if request.method == "POST":
#         form = LeadForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("/leads/")
#     return render(request, 'leads/create_lead.html', {'form':form})

# def edit_lead(request,pk):
    
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm(instance=lead)

#     if request.method == "POST":
#         form = LeadForm(request.POST, instance=lead)

#         if form.is_valid():
#             form.save()
#             return redirect("/leads/")
#     return render(request, "leads/edit_lead.html", {'lead':lead, 'form':form})

# def delete_lead(request, pk):
#     lead = Lead.objects.get(id = pk)
#     lead.delete()
#     return redirect("/leads/")
