from helium import *


def start_chrome(param):
    pass


start_chrome('google.com')
write('helium selenium github')


def press(ENTER):
    pass


press(ENTER)
click('mherrmann/helium')
go_to('github.com/login')
write('username', into='Username')
write('password', into='Password')
click('Sign in')
kill_browser()