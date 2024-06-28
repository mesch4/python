import cryptocode

chave = "4DC7055F264A33E1ACE93C40529B828D"

MensagemCriptografada = input("Cripto: ")

MensagemDescriptografada = cryptocode.decrypt(MensagemCriptografada, chave)
print("Sua mensagem descriptografada: " + str(MensagemDescriptografada))