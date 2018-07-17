#PyXSS - XSS Tool Written In Python2
import os, time, argparse
try:
  import mechanize
except:
  print("Mechanize Not Installed! Run setup.py to install it!")
  quit()
def banner():
  print('''

   __ ____  ___  _________ _________     /\  __   
  / / \   \/  / /   _____//   _____/    / /  \ \  
 / /   \     /  \_____  \ \_____  \    / /    \ \ 
 \ \   /     \  /        \/        \  / /     / / 
  \_\ /___/\  \/_______  /_______  / / /     /_/  
            \_/        \/        \/  \/           
                                                  
                                              
def args():
  global args
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', '--url', help="URL To Scan")
  parser.add_argument('-f' '--form', help="Input Form's Name")
  args = parser.parse_args()
def test()
  global br
  br = mechanize.Browser() 
  br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
  br.set_handle_robots(False)
  br.set_handle_equiv(True)
  text = "TESTING_FOR_XSS"
  br.open(args.url)
  br.select_form(nr=0)
  br.form[args.form] = text
  r = br.submit()
  if (text in r.geturl()):
    print "XSS Vulnerability Found!"
    print "Would You Like To Inject a Script In the Site?"
    yorn = raw_input("Y/N: ")
    if yorn == 'Y' or 'y':
      br.open('http://www.google.com')
      code = raw_input("Enter Code: ")
      br.open(args.url)
      br.select_form(nr=0)
      br.form[args.form] = text
      r = None
      r = br.submit()
      print "Injected code: " + code + " URL: " + str(r.geturl())
    if yorn == 'N' or 'n':
      print "Okay, Quitting tool..."
      time.sleep(2)
      quit()
def main():
  banner()
  args()
  test()
main()
