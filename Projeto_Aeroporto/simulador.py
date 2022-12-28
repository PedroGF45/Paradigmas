from random import *
from math import *
from eventos import *
from cadeias import *
from filas import *

def simula(mc1, mc2, ma, me, md, x, y, ts):
    
    global c, f, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma
    
    def obsexp(m):
        x = random()
        return -m * log(x)
    
    def inicializa():
        global c, f, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma
    
        c = cap()
        f = fila()
        ic = 0
        e = evento(ic + obsexp(mc1), 'aterra')
        c.acr(e)
        pe = e
        pista = 'livre'
        tmed = 0
        tmeap = 0
        tmeanp = 0
        nmea = 0
        nad = 0
        nma = 0
        
    def simula_evento(evt):

            if (ts > 180 and ts < 187):
                e = evento(ic + obsexp(mc1), 'aterra')
            else:
                e = evento(ic + obsexp(mc2), 'aterra')


    def finaliza():
        
        print('Tempo médio de espera para descolar', tmed)
        print('Tempo máximo d espera para aterrar de um avião prioritário', tmeap)
        print('Tempo máximo de esepera para aterrar de um avião não prioritário','%.2f' % tmeanp)
        print('Número máximo de aviões à espera para aterrar', nmea)  
        print('Número total de aviões que desistiram de estar à espera para aterrar', nad)  
        print('Número máximo de aviões que esteve no aeroporto', nma)  
        
    
    # corpo do programa simulador:       
    inicializa()

    while pe.inst() <= ts:
        ic = pe.inst()
        # simula prox evento
        simula_evento(pe)
        #atualiza prox evento a simular
        c.retira()
        pe = c.proximo()

    finaliza()
     #fim do programa simulador  