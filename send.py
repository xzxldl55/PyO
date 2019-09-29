# -*- coding: utf-8 -*
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址与密码
from_addr = '15779197748@163.com'
password  = 'xzxldl55'
# 输入收件人地址
to_addr = input('To:')
# 输入SMTP服务器地址
smtp_server = 'smtp.163.com'
# 填写邮件信息
msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('xzxldl <%s>' % from_addr)
msg['To'] = _format_addr('哈希！ <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...From python', 'utf-8').encode()

# smtp协议默认端口为25
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()