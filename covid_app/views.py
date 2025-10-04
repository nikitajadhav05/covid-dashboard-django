from django.shortcuts import render, redirect
import requests

# 👤 LOGIN view (hardcoded)
def login(request):
    
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '12345':
            request.session['logged_in'] = True
            print("✅ Logged in successfully")
            return redirect('covid_report')
        else:
            print("❌ Invalid login attempt")
            return render(request, 'login.html', {'error': 'Invalid credentials'})

# 🦠 COVID Report (protected)
def covid_report(request):
    print("DEBUG >> session.logged_in =", request.session.get('logged_in'))  # Terminal debug

    if not request.session.get('logged_in'):
        print("🔐 Not logged in → redirecting to login")
        return redirect('login')  # 🔒 Force login

    try:
        url = "https://api.rootnet.in/covid19-in/stats/latest"
        response = requests.get(url, headers={"User-Agent": "XY"})
        data = response.json()

        total_cases = data['data']['summary']['total']
        regional_data = data['data']['regional']

        print("✅ COVID data fetched successfully")
        return render(request, 'covid_report.html', {
            'total_cases': total_cases,
            'data': regional_data
        })

    except Exception as e:
        print("⚠️ Error While Fetching API:", e)
        return render(request, 'covid_report.html', {
            'total_cases': 'N/A',
            'data': []
        })
