import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (ListProperty,NumericProperty)

 
kivy.require('1.7.0')


class PainelJogoDaVelha(BoxLayout):
        pass

class BotaoEntrada(Button):
    coordenada = ListProperty([0, 0])

class GradeJogoDaVelha(GridLayout):
    status = ListProperty([0, 0, 0,0, 0, 0,0, 0, 0])
    jogadorAtual = NumericProperty(1)
    
    def __init__(self, *args, **kwargs):
        super(GradeJogoDaVelha, self).__init__(*args, **kwargs)
        
        for linha in range(3):
            for coluna in range(3):
                botaoE = BotaoEntrada(coordenada=(linha,coluna))
                botaoE.bind(on_release=self.botao_pressionado)
                self.add_widget(botaoE)

    def botao_pressionado(self, botao):
        # Print output just to see what's going on
        #print ("Botao {} pressionado!".format(botao.coordenada))
        jogador = {1: 'O', -1: 'X'}
        cores = {1: (1, 0, 0, 1), -1: (0, 0, 1, 1)}

        linha, coluna = botao.coordenada  

        indiceStatus = 3*linha + coluna
        
        posicaoJaOcupada = self.status[indiceStatus]

        if not posicaoJaOcupada:
            self.status[indiceStatus] = self.jogadorAtual
            botao.text = {1: 'O', -1: 'X'}[self.jogadorAtual]
            botao.background_color = cores[self.jogadorAtual]
            self.jogadorAtual *= -1




class JogoDaVelhaApp(App):
    def build(self):
        return  PainelJogoDaVelha()


if __name__ == '__main__':
    JogoDaVelhaApp().run()