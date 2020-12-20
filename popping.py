import poplib
import getpass
import email

pop3server = 'pop.gmail.com'
username = input("Enter email address : ")
password = getpass.getpass("Enter Password : ")
pop3server = poplib.POP3_SSL(pop3server, '995') # open connection
welcome = pop3server.getwelcome().decode("utf-8")
print (welcome) #show welcome message
print ('Username :' + username + '\n')
pop3server.user(username)
pop3server.pass_(password)
pop3info = pop3server.stat() #access mailbox status
mailcount = pop3info[0] #total email

print("STAT :" + str(pop3info))

while True :

  #email count
  numMessages = len(pop3server.list()[1])
  print("\nTotal no. of Email : " , mailcount)


  #List of email subject
  counter = 0
  for List in range(numMessages) :
      counter = counter + 1
      for msg in pop3server.retr(List+1)[1]:
          msgd =  msg.decode("utf-8")
          if msgd.startswith('Subject'):
              print ('   Email ' + str(counter) + ', ' + str(msgd))
              break
  print('   Enter 0 if you want for all email.\n')
  
  #email number prompt
  print("Which email you want to open ?")
  key = int(input("Email : "))

  #to read one email
  if key > 0 :
    for aaa in pop3server.retr(key)[1]:
      bbb = aaa.decode("utf-8")
      if bbb.startswith('From'):
              print (str(bbb))
      if bbb.startswith('Subject'):
              print (str(bbb))
      if bbb.startswith('To'):
              print (str(bbb))
      if bbb.startswith('Date'):
              print (str(bbb))
      message = email.message_from_string(bbb)
      print(message.get_payload())

  #print('END\n')


  #reading email
  elif key == 0 :
    print ("\n\nStart Reading All Messages\n\n")
    for i in range(mailcount):
      for i in pop3server.retr(i+1)[1]:
        j = i.decode("utf-8")
        if j.startswith('From'):
              print (str(j))
        if j.startswith('Subject'):
              print (str(j))
        if j.startswith('To'):
              print (str(j))
        if j.startswith('Date'):
              print (str(j))
        message = email.message_from_string(j)
        print(message.get_payload())

  #error-catch
  else  :
     print("Error ! You have entered wrong number/input !")

  #quit reading email
  cont = input("\n\nContinue read email ? yes/no : ")
  while cont.lower() not in ("yes","no"):
     cont = input("Continue read email ? yes/no :")
  if cont == "no":
     break

#email deletion
deleto = input('Do you want to delete any email ? (y/n) :')
while deleto.lower() not in ("y","n"):
     deleto = input("Do you want to delete any email  ? (y/n) :")
if deleto == "y" :
     print("Which email you want to delete ?")
     deleti = int(input("Email : "))
     if deleti > 0 :
         pop3server.dele(deleti)
         print("Done delete Email " + str(deleti))
     elif deleti == 0 :
         for z in range(mailcount):
             pop3server.dele(z+1)
     else :
         print("Error ! You have entered wrong number/input !")
     pop3server.quit()

elif deleto == "n" :
     pop3server.quit()

print('Quitting Program...')
#pop3server.quit()
