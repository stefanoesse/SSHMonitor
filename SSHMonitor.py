#/usr/bin/python
# coding: interpy

import smtplib,sys,os
from optparse import OptionParser

FAILED = '/etc/sshguard/failed'
SUCCESSFUL = '/etc/sshguard/successful'
BANNED_IPS = '/etc/sshguard/banned_ips'

def usage():
    print "Usage: SSHMonitor.py <email address> <password> [options]"
    print "OPTIONS:\n"
    print "    [port]     - If the port is not specified it will default to 445.\n"
    print "    [logging]  - If sshgaurd is installed then you can have SSHGuard log failed and successful\n"
    print "                   attempts. As well as blocked IPs.\n"
    print "    [email]    - This is the email address you want SSHMonitor to send the notifications to.\n"
    print "    [log file] - You can specify the log file or it will default to /var/log/auth.log.\n\n"
    print "SWITCHES:\n"
    print "    Enable SSHGuard logging: --log-enable, -L, log-enable\n"
    print "    Help: --help, -h, help\n"
    print "    Port: --port, -p, port."
    sys.exit(1)

parser = OptionParser()
parser.add_option("-e", "--email", dest='email')
parser.add_option("-p", "--password", dest='password')
parser.add_option("-P", "--port", dest='port')
parser.add_option("-l", "--log-file", dest='logfile')
(options, args) = parser.parse_args()

def file_exists(file):
    return os.path.exists(file)

if options.email is None:
    print "\nE-mail cannot be empty!\n"
    usage
else:
    sender,to = options.email,options.email

if options.password is None:
    print "\nMust provide a password!\n"
    usage
else:
    password = options.password

if options.port is None:
    port = 587
else:
    port = options.port

if options.logfile is None or not file_exists(options.logfile):
    logfile = '/var/log/auth.log'
else:
    logfile = options.logfile

for i in [FAILED,SUCCESSFUL,BANNED_IPS]:
    if not file_exists(i):
        open(i, 'w')

def send_mail(sender,to,password,port):
    try:
        mail = smtplib.SMTP('smtp.gmail.com',port)
        mail.starttls()
        mail.login(sender,password)
        mail.sendmail(sender, to, "Test email.")
        print "\nSent email successfully.\n"
    except smtplib.SMTPAuthenticationError:
        print "\nCould not athenticate with password and username!\n"

if len(sys.argv) > 4:
    send_mail(sender,to,password,port)
