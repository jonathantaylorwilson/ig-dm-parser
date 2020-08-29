import json

def export_convo(jdata, idx, username):
    filename = ""
    for user in jdata[idx]["participants"]:
        if user != username:
            filename += user + "-"
    filename = filename[0:-1] + ".txt"
    file = open(filename, 'w')
    conversation = jdata[idx]["conversation"]
    for i in range(len(conversation)-1, -1, -1):
        print(i)
        sender = conversation[i]["sender"]
        time = conversation[i]["created_at"]
        text = ""
        if "text" in conversation[i] and conversation[i]["text"] is not None:
            text += conversation[i]["text"]
        if "media" in conversation[i]:
            text += "\n MEDIA: " + conversation[i]["media"]
        s = sender + " (" + time + "): " + text + "\n"
        print(s)
        file.write(s)
    file.close()


username = input("What is your IG username? (all lowercase): ")

data = ''
with open ('messages.json', 'r') as file:
    data = file.read().replace('\n', '')

jdata = json.loads(data)
for i in range(len(jdata)):
    participants = jdata[i]["participants"]
    recipient = []
    for participant in participants:
        if participant != username:
            recipient.append(participant)
    print(i, " ".join(recipient))

all_or_some = input("Would you like to export ALL conversations to their own file? (y/n) ")

if all_or_some == "y":
    for i in range(len(jdata)):
        export_convo(jdata, i, username)
else:
    target = input("Which conversation # would you like to export? ")
    export_convo(jdata, int(target), username)


