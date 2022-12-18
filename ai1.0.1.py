	
from matgeo import dist2p
import random, time, sys
import pygame


pygame.init()

limitemapx=800
limitemapy=600
goal=(650,300)

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
YELLOW = (255,255,0)

startpoint=(50,300)	#ponto de partida
raio=10
passos=5	#distancia de cada passo+-
maispassos=20	#quantidade de passos a ser adisionado por geracao
ppg=200	#Passos Por Geracao
opg=50#Objetos Por Geracao
gera=1
varia=0.05

window = pygame.display.set_mode((limitemapx,limitemapy), 0, 32)

class pessoa:
	def __init__(self,startpoint,caminho):	#cada pessoa e um ponto
		self.x=startpoint[0]
		self.y=startpoint[1]
		self.caminho=caminho.copy()	#esse e o caminho q o ponto vai seguir
		self.live=True
		
	def pessoamov(self,dire):	#movimenta o ponto de acordo com o teclado numerico
		if((dire==7)or(dire==8)or(dire==9)):
			if(self.y<limitemapy):
				self.y+=passos
			else:
				self.live=False
		if((dire==3)or(dire==6)or(dire==9)):
			if(self.x<limitemapx):
				self.x+=passos
			else:
				self.live=False
		if((dire==7)or(dire==4)or(dire==1)):
			if(self.x>1):
				self.x-=passos
			else:
				self.live=False
		if((dire==1)or(dire==2)or(dire==3)):
			if(self.y>1):
				self.y-=passos
			else:
				self.live=False
		
class simu:
	def __init__(self):
		self.populacao=[]
		x=self.createway(ppg)
		for i in range(1,opg):
			x=self.createway(ppg)
			self.populacao.append(pessoa(startpoint,x))
			
	def createway(self,x):	#cria um caminho randomico
		caminho=[]
		for i in range(1,x):
			caminho.append(random.randint(1,9))
		return caminho
		
	def copybest(self,y):
		
		#for i in range(maispassos):	#aumenta a distancia q um ponto pode chegar
			#y.append(random.randint(1,9))
		x=y	#copia o caminho passado
		self.populacao=[]	#zera a populacao
		for i in range(0,opg):	#cria uma nova populacao com o caminho passado
			self.populacao.append(pessoa(startpoint,x))
	
	def definebest(self):
		bestai=self.populacao[0]
		bestdis=dist2p(self.populacao[0].x,self.populacao[0].y,goal[0],goal[1])	#usa o primeiro como base
		print(bestdis)
		x=0
		for i in self.populacao:
			dist=dist2p(i.x,i.y,goal[0],goal[1])
			#print("{}-{}".format(x,i.caminho))
			x+=1
			if dist<bestdis:
				bestai=i
				bestdis=dist
		print("geracao {} :{}-com {} passos:{}".format(gera,bestai,len(bestai.caminho),bestdis))
		if bestdis == 0 :
			bestai.caminho.pop()
			global ppg
			ppg=ppg-1
		return bestai.caminho	#retorna o q chegou mais proximo do objetivo
		
	def changeway(self):	#muda um passo de cada membro da populacao
		z=0
		
		for i in range(len(self.populacao)):
			z+=1
			if z == 1: #self.populacao[0]:	#exeto o primeiro, para evitar q se afastem do objetivo
				
				continue
			v=int(len(self.populacao[1].caminho) * varia)	#quantidade de variacao
			for c in range(v):
				x=random.randint(1,len(self.populacao[i].caminho)-1)
				y=random.randint(1,9)
				while y == self.populacao[i].caminho[x]:	#confirma se esta mudando a direcao
					y=random.randint(1,9)
				self.populacao[i].caminho[x]=y
		
	
			
	
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
	
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
	
	x=test.definebest()		     
	test.copybest(x)
	test.changeway()
	gera+=1
	time.sleep(0.1)
	if(gera==100):
		break
while True:
	
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		     
	continue

