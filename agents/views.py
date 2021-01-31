from django.shortcuts import render,redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import AgentModelForm

# Create your views here.
class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    queryset = Agent.objects.all()
    context_object_name = "agents"

class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()

        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(DetailView):
    template_name = "agents/agent_detail.html"
    queryset = Agent.objects.all()
    context_object_name = "agent"

class AgentUpdateView(UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    queryset = Agent.objects.all()
    
    def get_success_url(self):
        return reverse('agents:agent_list')

class AgentDeleteView(DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = Agent.objects.all()
    
    def get_success_url(self):
        return reverse('agents:agent_list')