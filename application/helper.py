import requests
import os
import base64
import json
from pymongo import MongoClient
from cryptography.fernet import Fernet
from Crypto.Util.py3compat import tobytes, tostr


def get_mongo():
    MONGO_URI = os.environ.get('MONGO_URI')
    MONGO_DB = os.environ.get('MONGO_DATABASE')
    client = MongoClient(MONGO_URI)
    db_mongo = client[MONGO_DB]
    return db_mongo


def encryptor(inputStr, decrypt=False):
    secret_key = os.environ.get(
        'encryption_key', 'xunOQzJlpKms1lv1Dg0l2PNGmDKJfbJEppw1xjmMS3w=')
    secret_key = tobytes(secret_key)
    fernetObj = Fernet(secret_key)
    output = ""
    if decrypt:
        inputStr = tobytes(inputStr)
        output = fernetObj.decrypt(inputStr)
        output = tostr(output)
    else:
        inputStr = str.encode(inputStr)
        output = fernetObj.encrypt(inputStr)
        output = tostr(output)
    return output


def encryptor_test(aa="some-password"):
    print("aa:", aa)
    bb = encryptor(aa)
    print("bb:", bb)
    cc = encryptor(bb, True)
    print("cc:", cc)
    print("(%s : %s) test type:%s and value:%s" %
          (aa, cc, type(aa) == type(cc), aa == cc))


def send_email(recipient, subject, message):
    import smtplib
    from email.mime.text import MIMEText
    port, smtp_server, sender_email, password = os.environ.get(
        'SMTP_ACCOUNT').split(',')
    TO = recipient if isinstance(recipient, list) else [recipient]
    FROM = sender_email
    if os.environ.get('EMAIL_FROM'):
        FROM = os.environ.get('EMAIL_FROM') + ' ' + sender_email
    try:
        server_smtp = smtplib.SMTP(smtp_server, int(port))
        server_smtp.ehlo()
        server_smtp.starttls()
        server_smtp.ehlo()
        server_smtp.login(sender_email, password)
        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['From'] = FROM
        msg['To'] = ", ".join(TO)
        sent = server_smtp.sendmail(sender_email, TO, msg.as_string())
        return sent
    except Exception as e:
        print(e)
        return False
