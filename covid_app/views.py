from django.shortcuts import render
import requests

def covid_report(request):
    try:
        # Fetch data from Rootnet API
        url = "https://api.rootnet.in/covid19-in/stats/latest"
        response = requests.get(url, headers={"User-Agent": "XY"})
        data = response.json()

        # Get total confirmed cases from summary
        total_cases = data['data']['summary']['total']

        # Get state-wise/regional data
        regional_data = data['data']['regional']

        # Pass data to your HTML template
        return render(request, 'covid_report.html', {
            'total_cases': total_cases,
            'data': regional_data
        })

    except Exception as e:
        print("Error While Fetching API:", e)

        # In case of API failure, pass empty/default values
        return render(request, 'covid_report.html', {
            'total_cases': 'N/A',
            'data': []
        })

