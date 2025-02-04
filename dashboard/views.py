from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.models import Lead
from client.models import Client
from team.models import Team

@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)[0]
    leads = Lead.objects.filter(team=team).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]
    
    total_leads = Lead.objects.filter(team=team).count()
    total_clients = Client.objects.filter(team=team).count()
    
    lead_status_data = Lead.objects.values('status').annotate(count=Count('status'))
    
    statuses = ['new', 'contacted', 'won', 'lost']
    status_counts = {status: 0 for status in statuses}
    for entry in lead_status_data:
        status_counts[entry['status']] = entry['count']
    
    conversion_rate = (total_clients / total_leads * 100) if total_leads > 0 else 0
    
    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
        'total_leads': total_leads,
        'total_clients': total_clients,
        'conversion_rate': round(conversion_rate, 2),
        'status_counts': status_counts, 
    })
