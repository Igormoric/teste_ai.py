
from matgeo import dist2p
import random, time, sys
import pygame


pygame.init()

limitemapx=800
limitemapy=600
goal=(750,300)

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
YELLOW = (255,255,0)

startpoint=(50,300)	#ponto de partida
raio=10
passos=5	#distancia de cada passo+-
maispassos=40	#quantidade de passos a ser adisionado por geracao
ppg=50 		#Passos Por Geracao
gera=1

window = pygame.display.set_mode((limitemapx,limitemapy), 0, 32)

class pessoa:
	def __init__(self,startpoint,caminho):	#cada pessoa e um ponto
		self.x=startpoint[0]
		self.y=startpoint[1]
		self.caminho=caminho	#esse e o caminho q o ponto vai seguir
		self.live=True
		
	def pessoamov(self,dire):	#movimenta o ponto de acordo com o teclado numerico
		if((dire==7)or(dire==8)or(dire==9)):
			if(self.x<limitemapy):
				self.x+=passos
			else:
				self.live=False
		if((dire==3)or(dire==6)or(dire==9)):
			if(self.y<limitemapx):
				self.y+=passos
			else:
				self.live=False
		if((dire==7)or(dire==4)or(dire==1)):
			if(self.y>1):
				self.y-=passos
			else:
				self.live=False
		if((dire==1)or(dire==2)or(dire==3)):
			if(self.x>1):
				self.x-=passos
			else:
				self.live=False
		
class simu:
	def __init__(self):
		self.populacao=[]
		x=self.createway(ppg)
		for i in range(1,10):
			x=self.createway(ppg)
			self.populacao.append(pessoa(startpoint,x))
			
	def createway(self,x):	#cria um caminho randomico
		caminho=[]
		for i in range(1,x):
			caminho.append(random.randint(1,9))
		return caminho
		
	def copybest(self,y):
		
		#for i in range(maispassos):	#almenta a distancia q um ponto pode chegar
			#y.caminho.append(random.randint(1,9))
		x=y.caminho	#copia o caminho passado
		self.populacao=[]	#zera a populacao
		for i in range(0,10):	#cria uma nova populacao com o caminho passado
			self.populacao.append(pessoa(startpoint,x))
	
	def definebest(self):
		bestai=self.populacao[0]
		bestdis=dist2p(self.populacao[0].x,self.populacao[0].y,goal[0],goal[1])	#usa o primeiro como base
		print(bestdis)
		for i in self.populacao:
			dist=dist2p(i.x,i.y,goal[0],goal[1])
			if dist<bestdis:
				bestai=i
				bestdis=dist
				print(bestai,bestdis)
		print("{}:{}".format(bestai,bestdis))
		print(bestai.caminho)
		return bestai	#retorna o q chegou mais proximo do objetivo
		
	def changeway(self):	#muda um passo de cada membro da populacao
		for i in self.populacao:
			if i == self.populacao[0]:	#exeto o primeiro, para evitar q se afastem do objetivo
				print(i)
				continue
			x=random.randint(1,len(i.caminho)-1)
			y=random.randint(1,9)
			i.caminho[x]=y
	
	
			
	
test=simu()
window.fill(BLACK)
pygame.draw.circle(window, GREEN, goal, raio*2, 0)
pygame.display.update()		
while True:
	for p in range(ppg-1):
		window.fill(BLACK)
		pygame.draw.circle(window, GREEN, goal, raio*2, 0)
		for i in test.populacao:
			i.pessoamov(i.caminho[p])
			posisao=(i.x,i.y)
			pygame.draw.circle(window, YELLOW, posisao, raio, 0)
		pygame.display.update()
		#time.sleep(0.1)
	
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			     
	test.copybest(test.definebest())
	test.changeway()
	gera+=1
	time.sleep(0.1)
	if(gera==10):
		break
while True:
	
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		     
	continue
