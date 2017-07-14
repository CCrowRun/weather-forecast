# Import necessary libraries
import requests
import smtplib

def get_emails():
    emails = []

    try:
        email_file = open('emails.txt', 'r')
        # Parse email file
        for line in email_file:
            emails.append(line.strip())
            
    except FileNotFoundError as err:
        print(err)

    return emails

def get_weather_forecast():
    # Connect to Open Weather API
    url = 'http://api.openweathermap.org/data/2.5/weather?id=5261457&units=imperial&APPID=eb3789de81e658dc5e9ffa2704ce15e4'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Parse JSON into variables
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Create forecast variable
    forecast = 'The forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min))
    
    return forecast

def send_emails(emails, schedule, forecast):
    # Connect to Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    
    # Start TLS encryption
    server.starttls()
    
    # Login
    password = input("What's your password?")
    from_email = 'carrie.g.crow@gmail.com'
    server.login(from_email, password)
    
    # Send to entire email list
    for to_email in emails.items():
        message = "Subject: Today's Forecast\n"
        message += "Hi!\n\n"
        message += forecast + '\n\n'
        message += "Have a lovely day!"
        server.sendmail(from_email, to_email, message)
    server.quit()

def main():
    # Call functions
    emails = get_emails()
    forecast = get_weather_forecast()
    send_emails(emails, forecast)
#Call Main
main()
