from .models import Documents
from datetime import timedelta, date

enddate = date.today()
startdate = enddate - timedelta(days=30)
obj = Documents.objects.filter(expiry_date=[startdate, enddate])