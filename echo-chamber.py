# An application that allows ChatGPT to have a conversation with...itself! 😲
import openai

# Track the conversation to add to "conversation.txt" file at the end
master_conversation = ''

# Create instance 1
instance1_messages = [{"role": "system", "content": "You are a interlocutor in an intellectual discussion, and you do not waver from your point of view."}]

instance1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=instance1_messages
)

# Create instance 2
instance2_messages = [{"role": "system", "content": "You are a interlocutor in an intellectual discussion, but you disagree with everything I say. You do not waver from your point of view."}]

instance2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=instance2_messages
)


# Seed the conversation by querying the first instance
seed = input("Conversation seed: ")
master_conversation += "Conversation seed: " + seed + "\n"

instance1_messages.append({"role": "user", "content":seed})
instance1 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=instance1_messages
)

# Put output of instance one into query of instance 2
instance1_response = instance1['choices'][0]['message']['content']
print("\nSpeaker 1: " + instance1_response + "\n")
master_conversation += "\nSpeaker 1: " + instance1_response + "\n"

instance2_messages.append({"role": "user", "content":instance1_response})
instance2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=instance2_messages
)
instance2_response = instance2['choices'][0]['message']['content']
print("\nSpeaker 2: " + instance2_response + "\n")
master_conversation += "\nSpeaker 2: " + instance2_response + "\n"

# Etc...
# Don't forget to set a timer so they don't talk to each other forever and spend all your $$$
turns = int(input("\nHow many turns do you want the speakers to take (integer)? "))
master_conversation += "\nTurns: " + str(turns) + "\n"

for i in range(0, turns):
    print("----------\n\nRound: " + str(i+1) + "\n")
    master_conversation += "----------\n\nRound: " + str(i+1) + "\n"
    instance1_messages.append({"role":"user", "content":instance2_response})
    instance1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=instance1_messages
    )
    instance1_response = instance1['choices'][0]['message']['content']
    print("\nSpeaker 1: " + instance1_response + "\n")
    master_conversation += "\nSpeaker 1: " + instance1_response + "\n"
   
    instance2_messages.append({"role": "user", "content":instance1_response})
    instance2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=instance2_messages
    )
    instance2_response = instance2['choices'][0]['message']['content']
    print("\nSpeaker 2: " + instance2_response + "\n")
    master_conversation += "\nSpeaker 2: " + instance2_response + "\n"

print("\nModerator: Thank you, gentlemen. We'll have to end our discussion there...\n")
master_conversation += "\n\nEND\n\n"

# Create a text file out of the conversation
with open('convo.txt', 'w') as f:
    f.write(master_conversation)

print("\nConversation stored in convo.txt")
