from chatterbot import ChatBot
from spacy.cli import download

# TREINAMENTO DO CHAT BOT
from chatterbot.trainers import ListTrainer

# FERRAMENTA QUE SERÁ USADA: chatterbot
# OBS: pode gerar alguns problemas
"""
Para o processo de criação do chat bot vai ser necessário criar um ambiente virtual
"NUNCA FIZ ISSO KKKK"
"ATUALIZAÇÕES : Descobri que eu sempre fiz isso e não sabia kkkkkkk"
"""
# isso aqui só precisa para corrigir o bug
download("en_core_web_sm")


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


# PASSO01 CRIAR O CHATBOT
chatBot = ChatBot("ChatGPT", tagger_language=ENGSM)
# PASSO02 TREINAR O CHATBOT
conversa = [
    "oi",
    "ola",
    "Quem é você ?",
    "Eu sou um chat bot, primeiro desenvolvido pelo meu criador.",
    "como você está ?",
    "bem e você ?",
    "bem",
    "Que ótimo!! Quer que eu conte uma piada ?",
    "sim",
    "Você sabe qual lingua antiga foi espirada no rei do pop?",
    "nao",
    "O ara michaelhahhhahahahahah"
    "mau",
    "Nesse caso vou te conta uma piada: Você conhece o Mario ?",
    "Quem?",
    "Não você não vai ouvir essa piada de mim hahahaha",
    "Que Mario ?",
    "Não você não vai ouvir essa piada de mim hahahaha",
    "Mas eu quero uma piada",
    "Então la vai: Qual o contrário de papelada ?",
    "Não sei",
    "Pá vestida hahahhahaa"
]
trainer = ListTrainer(chatBot)
trainer.train(conversa)

# PASSO 3 DEPOIS DE TREINADO VAMOS USAR O CHATBOT
op = "sim"
print ("Digite 0 para parar a conversa imediatamente")

while op == "sim":

    usuario = input("Você: ")
    if usuario == "0":
        op = None
        break
    print(chatBot.get_response(usuario))

limpar = int(input("Quer limpar os bancos de dados do chat?[1/0]"))


if limpar == 1:
    senha = input("Digite a senha: ")
    if senha == "!@#$%¨&*()_+":
        chatBot.storage.drop()
    else:
        print("Senha incorreta")


