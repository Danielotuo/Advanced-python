import asyncio
import mailtrap as mt


async def send_email(subject, body, to):
    # Create a Mail object with the email details
    mail = mt.Mail(
        sender=mt.Address(email="mailtrap@example.com", name="Mailtrap Test"),
        to=[mt.Address(email=to)],
        subject=subject,
        text=body,
    )

    # Create a MailtrapClient and send the email
    client = mt.MailtrapClient(token="your-api-key")
    client.send(mail)
    print('Email sent successfully')


async def main():
    asyncio.create_task(send_email(
        'subject', 'this is just for testing', 'nobody@example.com'))

    # do other tasks while waiting for email to be sent
    print('doing other tasks')

asyncio.run(main())
