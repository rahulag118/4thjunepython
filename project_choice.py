import numpy
import os 
import webbrowser
import time 
import urllib
x='''press 1 to check date and time
     press 2 to create a file 
     press 3 to create a directory
	 press 4 to search on google 
	 press 5 to logout 
	 press 6 to shutdown your os
 	 press 7 to check your internet connection
	 press 8 to login on facebook'''
print (x)
       
choice = int(input("\nEnter the choice "))
 
if      choice==1 :
            print ("showing time")
            print(time.ctime())
elif    choice==2 :
            print ("creating a file")
            f=open("xyz.txt","w+")
            #name.txt=raw_input("enter the file name")
             #           os.touch(name.txt)
elif   choice==3 :
           print ("creating a directory")
           name=input("enter the directory name")
           os.makedirs(name)
elif    choice==4:
           print ("searhing on google")
           ans =input("type to search")
           webbrowser.open_new_tab("https://www.google.com/search?client=ubuntu&channel=fs&q=" + ans)
elif   choice==5:
           print ("logging out")
		
           os.system("pkill -KILL -u rahul")
elif   choice==6:
           print ("shutting down plz close your all apps")
           os.system("reboot")
           time.sleep(2)
elif   choice==7:
           print ("checking the internet connection")
           webbrowser.open_new_tab("https://www.google.com/")
'''
elif   choice==8:
           print ("logging in in facebook")
           #!/usr/bin/python
           from selenium import webdriver
           from selenium.webdriver.support.ui import WebDriverWait

           driver = webdriver.Firefox(executable_path= "/usr/bin/geckodriver")
           driver.get("https://www.facebook.com")
           driver.maximize_window()
           fbusername = 'username'
           fbpassword = 'password'

           emailFieldID = 'email'
           passFieldID = 'pass'
	   
           loginButtonXpath='(//input[@value="Log In"])'
	   fblogoXpath = '(//a[contains(@href, "logo")])[1]'	
		
	   emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))	
	   passFieldElement = WebDriverWait(driver, 10).until(lambda driver: 	driver.find_element_by_id(passFieldID))
	   loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
		
	   emailFieldElement.clear()
	   emailFieldElement.send_keys(fbusername)
           passFieldElement.clear()
	   passFieldElement.send_keys(fbpassword)
           loginButtonElement.click()

	   WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fblogoXpath))
		#driver.quit()
'''	

