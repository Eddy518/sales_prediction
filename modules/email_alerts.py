import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_sales_alert(recipient_email, change_percent, previous_value, current_value):
    """
    Send a simple email alert about sales changes

    Parameters:
    recipient_email (str): User's email address
    change_percent (float): Percentage change in sales
    previous_value (float): Previous sales value
    current_value (float): Current sales value
    """
    # Email configuration
    sender_email = "edmwangi2@gmail.com"
    password = "zidh idui dkjx ezwk"
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = (
        f"Sales Alert: {abs(change_percent):.1f}% {'Increase' if change_percent > 0 else 'Decrease'}"
    )

    # Email body
    body = f"""
    <html>
    <body>
        <h2>Sales Pattern Alert</h2>
        <p>We've detected a significant change in your sales pattern:</p>
        <ul>
            <li>Previous sales value: {previous_value:,.0f} units</li>
            <li>Current sales value: {current_value:,.0f} units</li>
            <li>Change: {change_percent:+.1f}%</li>
        </ul>
        <p>Log in to your dashboard for more details.</p>
    </body>
    </html>
    """

    message.attach(MIMEText(body, "html"))

    try:
        # Connect to server and send email
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Adjust for your email provider
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
