# A company is developing a security system that requires 2 factor authorization.
# This means that the system needs to verify that 2 pieces of data are correct for the person to enter the building.
# When someone approached the building they need to have the correct name and correct passcode to enter the building.
# Which operator would be used here?
# Please provide a code example of how you would write this and output the result using the print() function for python or the console.log() function for javascript?
# I would use comparison operation 


Jaelin= "registered"
Password_5678="registered"
Password_6732="not registered"

print(Jaelin == Password_5678)

# Right Answer
name= 'Jaelin'
password= '123'

secruityName= 'Jaelin'
securitypassword= '123'

print(name == secruityName and password == securitypassword)
# A hospital needs to keep track of medical equipment.
#  they are getting a shipment of new ECG machines and Oxygen tanks and need to verify.
#  If they have more than whats needed in their office, they need to send the overflow 
# of equipment back to the manufacturer, but if they have less, the need to request more. 
# In this scenario, they are supposed to have 10 ECG machines, but only recieved 4,
#  and for the oxygen tanks they are supposed to have 6 in stock, but recieved 9. 
# Which operator would be used here? 
# Please provide a code example of how you would write this and output 
# the result using the print() function for python or the console.log() function for javascript?


ECG_machines= 10
x= 4
print(x >= ECG_machines)

# Right answer

ecgRequest= 10
ecgShipment= 4
print(ecgRequest < ecgShipment)

oxygenRequest= 6
oxygenShipment= 9
print(oxygenRequest > oxygenShipment)

# A company is developing a messaging app that allows people to send text message for free.
#  They need to allow users to capture the user data and then send it to someone else.
#  Which operator would be used here?
#  Please provide a code example of how you would write this and output the result using the print() function for python or the console.log()
#  function for javascript?

Jaelin= 'wassap'
James= 'yo'