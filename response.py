import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Sorry ! I am not sure what that means as I am normal python bot and dont have much knowledge about this particular topic but you can always refer my friends CHAT-GPT OR BARD-AI ,I am sure they will provide you with what you are looking for !!\n Have a Nice Day !!!"][
        random.randrange(1)]
    return response