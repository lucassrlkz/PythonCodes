import pywhatkit

imageReceiver = input(
    'nome e tipo do arquivo a ser transformado (arquivo.jpg): ')
imr = imageReceiver

result = imr.split('.')
result = 'results/%s.txt' % (result[0])

imageReceiver = 'images/'+imageReceiver
pywhatkit.image_to_ascii_art(imageReceiver, result)

# resultado do path os esta a imagem original e a convertida em txt
print('--------------------------------------------')
print('--------------------------------------------')
print(imageReceiver)
print('--------------------------------------------')
print('--------------------------------------------')
print(result)
