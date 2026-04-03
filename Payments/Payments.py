import csv, datetime, boto3, io
from Notifier import send_SMS

def read_csv_from_s3():
    s3 = boto3.client('s3', region_name='us-west-2')
    response = s3.get_object(Bucket='mofin-landscaping-client-data', Key='Clients.csv')
    content = response['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(content), skipinitialspace=True)
    next(reader)
    return list(reader)

def BehindPayments():
    csv_reader = read_csv_from_s3()

    today = datetime.datetime.now()
    Behind_on_Payments = []

    for line in csv_reader:
        payment_date = datetime.datetime.strptime(line[5], "%m-%d-%Y")
        days_late = (today - payment_date).days

        if days_late > 0:
            Behind_on_Payments.append(line)
    
    return Behind_on_Payments


def serviceDay():
    clients = BehindPayments()
    today = datetime.datetime.now()

    if len(clients) == 0:
        send_SMS("No clients are behind on payments", " ")

    else:
        subject = "Clients Who Are Behind on Payments:"
        message = "Clients:\n\n"
        for i in clients:
            payment_date = datetime.datetime.strptime(i[5], "%m-%d-%Y")
            days_late = (today - payment_date).days
            message += (
                f"- {i[0]} on {i[2]} is {days_late} days behind on payment,\n"
                f"  they owe ${i[3]}, their number is {i[1]}\n\n"
            )

        send_SMS(subject, message)


def lambda_handler(event, context):
    serviceDay()

    return {
        "statusCode": 200,
        "body": "Behind payment notifications sent"
    }