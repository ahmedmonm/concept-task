import click
import smtplib
import re
import getpass


# This function used to validate the format of email
def validateEmail(email):
    return re.match('[\\w-]{1,20}@\\w{2,20}\\.\\w{2,3}$', email)


@click.command()
@click.option('--email')
@click.option('--password')
@click.option('--confirm')
@click.option('--to')
@click.option('--subject')
def main(email, password, confirm, to, subject):
    try:

        gmail_user = click.prompt("FROM")                       # email of sender account

        # check the format of email
        valid = validateEmail(gmail_user)
        if not valid:
            print("\ninvalid email format")
            press = int(input("\nIf you want to try to send email again with vaild email"
                              " press 1, if you want to exist press 0: "))
            for i in range(2):
                if press == 1:
                    main()
                if press == 0:
                    exit()

        gmail_pwd =click.prompt("Please Enter your password")    # password of sender account
        gmail_conf = click.prompt("Confirm Your Password")        # confirm password of sender account

        # if two passwords isn`t equal ask user again
        if gmail_pwd != gmail_conf:
            press = int(input("\nIf you want to try to send email again press 1, if you want to exist press 0: "))
            for i in range(2):
                if press == 1:
                    main()
                if press == 0:
                    exit()

        # if all data is right send email
        if gmail_pwd == gmail_conf and valid:
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  # port number for gmail

            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()

            smtpserver.login(gmail_user, gmail_pwd)  # connect to the sender email

            to = click.prompt("To")

            # check the format of receiver email
            valid = validateEmail(to)
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
                subject = click.prompt("Subject")             # take the body of email
                smtpserver.sendmail(gmail_user, to, subject)  # send email

                print("\nSend successfully\n")

                press = int(input("\nIf you want to send another email press 1, if you want to exist press 0: "))
                print("\n")

                for i in range(2):
                    if press == 1:
                        main()
                    if press == 0:
                        exit()
    except:
        print("\nEmail failed to send")


if __name__ == '__main__':
    main()
