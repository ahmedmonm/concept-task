import click
import smtplib
from validate_email import validate_email


@click.command()
@click.option('--email')
@click.option('--password')
@click.option('--confirm')
@click.option('--to')
@click.option('--subject')
def main(email, password, confirm, to, subject):
    try:

        gmail_user = click.prompt("FROM")  # email of sender account

        # check the format of email
        valid = validate_email(gmail_user)
        if not valid:
            print("\ninvalid email format")
            press = int(input("If you want to try to send email again with vaild email"
                              " press 1, if you want to exist press 0: "))
            for i in range(2):
                if press == 1:
                    main()
                if press == 0:
                    exit()
        else:

            gmail_pwd = click.prompt("Please Enter your password")  # password of sender account

            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  # port number for gmail

            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()

            smtpserver.login(gmail_user, gmail_pwd)  # connect to the sender email


            to = click.prompt("To")

            # check the format of receiver email
            valid = validate_email(to)
            if not valid:
                print("\ninvalid email format")
                press = int(input("\nIf you want to try to send email again with vaild email"
                                  " press 1, if you want to exist press 0: "))
                for i in range(2):
                    if press == 1:
                        main()
                    if press == 0:
                        exit()
            else:

                subject = click.prompt("Subject")  # take the body of email
                body = click.prompt("Body")

                smtpserver.sendmail(gmail_user, to, subject)  # send email

                print("\nSend successfully")

                press = int(input("\nIf you want to send another email press 1, if you want to exist press 0: "))

                for i in range(2):
                    if press == 1:
                        main()
                    if press == 0:
                        exit()
    except Exception as err1:
        print("Email failed to send")
        print(err1)


try:
    if __name__ == '__main__':
        main()
except ValueError as err:
    print(err)
