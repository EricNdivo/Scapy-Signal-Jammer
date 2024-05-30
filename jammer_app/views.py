from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scapy.all import IP, ICMP, send
import threading
import time
import logging

logger = logging.getLogger(__name__)
jamming = False
interface = None
jam_thread = None

def home(request):
    return render(request, 'home.html')

def jam_wireless_networks():
    global jamming, interface
    channels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    try:
        while jamming:
            for channel in channels:
                packet = IP(dst="1.2.3.4") / ICMP()
                send(packet, verbose=False, iface=interface)
                logger.info(f"Sent ICMP packet to destination: {packet[IP].dst}")
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass

@csrf_exempt
def start_jamming(request):
    global jamming, jam_thread, interface

    if request.method == 'POST':
        interface = request.POST.get('interface')

        if not jamming:
            jamming = True
            jam_thread = threadng.Thread(target=jam_wireless_networks)
            jam_thread.start()
            return JsonResponse({'status': 'Jamming started'})
        else:
            return JsonResponse({'status': 'Jamming already in progress'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def stop_jamming(request):
    global jamming, jam_thread
    
    if request.method == 'POST':
        if jamming:
            jamming = False
            if jam_thread:
                jam_thread.join()
            return JsonResponse({'status': 'Jamming stopped'})
        else:
            return JsonResponse({'status': 'No jamming in progress'})
    else:
        return JsonResponse({'error':'Method not allowed'}, status=405)


