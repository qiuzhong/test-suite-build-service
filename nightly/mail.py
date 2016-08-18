#!/usr/bin/env python3

import json
import smtplib
from email.mime.text import MIMEText    
from email.mime.multipart import MIMEMultipart


def mail_xwalk_detect_results(smtp_server, fromaddr, toaddrs, platform, branch, json_file, cc = ""):
    '''
    Read the .json file and mail the results to the administrator.
    '''
    with open(json_file) as fp:
        update_info = json.load(fp)

    if not update_info.get('update'):
        print('No update, will not mail to the administrator.')
        return

    msg = MIMEMultipart()
    msg['Subject'] = 'Crosswal Release Notification!'
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Cc'] = cc

    content = '''<html>
                <head>
                </head>
                <body>
                <h1>New Crosswalk for {platform} on {branch} branch released!</h1>
                <h2>Old Version: {old_ver}</h2>
                <h2>New Version: {new_ver}</h2>
                </body>
                </html>'''.format(platform = platform, branch = branch,
                                old_ver = update_info.get('old_ver'),
                                new_ver = update_info.get('new_ver'))
    msgtext = MIMEText(content,'html','utf-8')
    msg.attach(msgtext)

    server = smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg.as_string().encode('utf-8'))
    server.quit()


if __name__ == '__main__':
    server = 'smtp.intel.com'
    fromaddr = 'zhongx.qiu@intel.com'
    toaddrs = 'zhongx.qiu@intel.com'
    platform = sys.argv[1]
    branch = sys.argv[2]
    json_file = sys.argv[3]
    mail_xwalk_detect_results(server, fromaddr, toaddrs, platform, branch, json_file)