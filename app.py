from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

s = ""
conversation = []
dic = {}
sendBack = ""
lastUserMesg = -1


@app.route('/', methods=['POST'])
def getAlexaText():

    echo = request.get_json(force=True)
    i_d = str(echo['session']["user"]["userId"])
    text = str(echo["request"]["intent"]["slots"]["Text"]["value"])[8:]
    sendBack = "sent message"

    if (text == "playback"):  # instead of sending a message, have Alexa retrieve last message sent by another person or by the user
        lastUserMesg = -1
        for ind in range(len(conversation)):
            if (i_d == conversation[ind][0]):
                lastUserMesg = ind  # last point when user sent a message
                break
        plbk = ""
        temp = []  # reversed list (reversed conversation) of the messages up to last user message
        if (lastUserMesg > 0):  # another person/people sent the last message/messages
            for yy in range(lastUserMesg):
                temp.insert(0, conversation[yy])  # push all messages sent by other people up until last user message
            for zz in temp:
                plbk = plbk + "Person " + zz[0] + " said " + zz[1] + ". "  # turn all messages from temp into one string
            sendBack = plbk
            print(plbk)
        elif (lastUserMesg == -1 and len(
                conversation) > 0):  # all messages in the conversation were sent by other people
            for w in range(len(conversation)):
                temp.insert(0, conversation[w])  # push all messages sent by other people up until last user message
            for z in temp:
                plbk = plbk + "Person " + z[0] + " said " + z[1] + ". "  # turn all messages from temp into one string
            sendBack = plbk
            print(plbk)
        elif (lastUserMesg == 0):
            sendBack = "You sent the last message. You said " + conversation[0][
                1]  # user sent the last message, no new messages sent by other people
            print(sendBack)
        else:
            sendBack = "Nothing to playback"  # there are no messages in the chatroom
            print(sendBack)
    else:
        tup = [i_d, text]
        global conversation
        conversation.insert(0, tup)  # store message in the conversation
        if i_d not in dic:
            global dic
            dic[i_d] = str(len(dic) + 1)  # map the long id to a simplified int based on the size of the dictionary
        s = ""
        for atup in conversation:
            global s
            s = s + dic[atup[0]] + "," + atup[1] + "|"  # format the entire conversation into a string, send the mapped id (simple int) instead of long id
        s = s[:-1]  # cut off last "|"
        print(s)

    data = {"version": '1.0',
            "response": {"outputSpeech": {"type": "PlainText", "text": sendBack}, "shouldEndSession": "true"}}
    return (jsonify(data))  # send above line as json in above line format


@app.route('/', methods=['GET'])
def indexHTML():
    print(s)
    return render_template("index.html",
                           data=s)  # send the conversation string to an html page to be displayed as a chatroom


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=443, ssl_context=("certificate.pem", "private-key.pem"))
