#!usr/bin/python

import re
import mechanize
import urllib, os

class MailChecker:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.mails=[]
        self.br=mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')]
        self.logged_in = False
        self.login()
        #check any mails and forward!?

    def login(self) :
        self.br.open("http://www.ee.iitb.ac.in/webmail/src/login.php")
        print self.br.title()
        assert self.br.viewing_html()
        self.br.select_form(nr=0)
        self.br.set_all_readonly(False)
        print "OK!"
        self.br["login_username"]=self.username
        self.br["secretkey"]=self.password
        self.br.find_control(name="loginServer").value=["Student Mail (Sandesh)"]
        self.br.submit()
        if "SquirrelMail" in self.br.title():
            print "Logged in"
            assert self.br.viewing_html()

