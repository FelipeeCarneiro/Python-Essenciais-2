import pygame #esse código não roda aqui no codespace só na máquina física mesmo.

run = True # o programa será executado enquanto a variável run for True;
width = 400 #tamanho da janela
height = 100
pygame.init() #iniciaçizar o ambiente pygame
screen = pygame.display.set_mode((width, height)) #preparar a janela e definir o seu tamanho
font = pygame.font.SysFont(None, 48) #fazer um bjeto representando a fonte
text = font.render("Bem vindo ao pygame", True, (255, 255, 255)) # fazer um objeto representando i, determinado texto - o texto será anti-aliased (True) e branco (255,255,255)
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2)) #inserir o texto no buffer da tela (atualmente invisível)
pygame.display.flip() #virar os buffer da tela pra tornar o texto visível
while run: #o loop principal do pygame começa aqui
    for event in pygame.event.get(): #obter uma lista com todos os eventos de pygame pendentes
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP: #linhas 14 à 16: verificar se o utilizador fechou a janela ou clicou em algum lugar dentro dela ou pressionou qualquer tecla
            run = False # se sim parar de executar o código.