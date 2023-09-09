from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime
import pytz

# Create your views here.
class DetailAPI(APIView):
    
    def get(self, request):
        #extract slack_name and track parametesr from the request
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')
        #get current day of the week
        current_day = datetime.now().strftime("%A")
        #utc time
        utc_time = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        github_file_url = "https://github.com/onyeka-embedded/task_one_hngx/tree/main/api"
        github_repo_url = "https://github.com/onyeka-embedded/task_one_hngx"

        if track is None:
            return HttpResponse("Query parameter missing")
        else:
           _data = {
                    "slack_name": slack_name,
                    "current_day": current_day,
                    "utc_time": utc_time, #"2023-08-21T15:04:05Z",
                    "track": track,
                    "github_file_url": github_file_url,
                    "github_repo_url": github_repo_url,
                    "status_code": status.HTTP_200_OK
                    }       

        return JsonResponse(_data)