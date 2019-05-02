# Alexa-Flask
Amazon Alexa Chatroom using Flask

This project was on https://95tristanl.hopto.org/ and could be connected to through the use of the 
Amazon Echo, or Amazon Echoism online. My project implemented the Alexa Skill Kit API on Amazon.com and used Flask to host my server. The
chatroom works is as follows: any number of people can send messages to the chatroom by speaking to Alexa. To connect to the chatroom one
needs to say: "Alexa doFlask" followed by anything the person wants to say. The Amazon Alexa Skill I built will recognize "doFlask" in 
the speech utterance and will send an https request as an intent, to my Flask server, hosted on an Amazon EC2 instance or the domain 
https://95tristanl.hopto.org/. My Flask server will parse each incoming request into json so it can grab the amazon id, the id associated 
with the login of the user, and the utterance, the message the user said to Alexa, from the request and put them into a tuple and into 
a conversation list. My server then turns this list into a string and while doing so, maps each amazon id into a simple integer id so that 
when the conversation is later presented, the list of messages will say the simple integer person id and the message that person said to 
Alexa. My server sends the string into an html template where the string is split into its individual, original, tuple pairs and presented 
as a message list in webpage on https://95tristanl.hopto.org/ in a per line format: "Person (integer id) said:" followed by what they said. 

The neat thing about this chatroom is that while you can see all the messages that each person said to Alexa on the html webpage, if a 
person does not want to look online, he/she has the option to say to Alexa: "Alexa doFlask playback". "playback" is a keyword that the
server will look for, but only if it is the only word said after "doFlask". Normaly, after each message you tell Alexa, Alexa respondes 
by saying "sent message", but upon uttering "Alexa doFlask playback", the server will go through the conversation until the last time the
user sent a message and it will read all the messages after the users last message back to the user in one long string. This keeps the user up-to-date on what he has not heard from the chatroom. If he sent the last message in the chatroom, Alexa will reply "You sent the last message. You said" followed by the last message the user sent. If someone were to say use the playback option and no messages were in the chatroom then Alexa would respond "Nothing to playback". The playback option does nothing to the html webpage.
