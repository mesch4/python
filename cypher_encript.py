import cryptocode

chave = "ADC7055F264A33E1ACE9340529B828D"
mensagem = input("Texto: ")

MensagemCriptografada = cryptocode.encrypt(mensagem, chave)
print("Sua mensagem criptografada: " + MensagemCriptografada)

MensagemDescriptografada = cryptocode.decrypt(MensagemCriptografada, chave)
print("Sua mensagem descriptografada: " + MensagemDescriptografada)
