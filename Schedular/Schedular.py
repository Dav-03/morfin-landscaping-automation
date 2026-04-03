import csv, datetime, boto3, io
from Notifier import send_SMS

def read_csv_from_s3():
    s3 = boto3.client('s3', region_name='us-west-2')
    response = s3.get_object(Bucket='mofin-landscaping-client-data', Key='Clients.csv')
    content = response['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(content), skipinitialspace=True)
    next(reader)
    return list(reader)

def Todays_clients():
    csv_reader = read_csv_from_s3()

    today = datetime.datetime.now()
    day_name = today.strftime("%A")
    scheduled = []

    for line in csv_reader:
        if line[6] == day_name:
            scheduled.append(line)
    
    return scheduled

def serviceDay():
    clients = Todays_clients()
    if len(clients) == 0:
        send_SMS('No clients are scheduled for today', ' ')
    
    else:
        subject = "Clients Scheduled for Today"
        message = "Today's Clients:\n\n"
        for i in clients:
            message += f"- {i[0]}\n  {i[2]}\n\n"

        send_SMS(subject, message)

def lambda_handler(event, context):
    serviceDay()

    return {
        "statusCode": 200,
        "body": "Today's client notifications sent"
    }