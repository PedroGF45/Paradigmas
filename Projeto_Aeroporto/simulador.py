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
        e = evento(ic + obsexp(mc1), 'chega')
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
        global c, f, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma

        if evt.cat() == 'cheg':
            if (ts > 180 and ts < 660):
                e = evento(ic + obsexp(mc2), 'chega')
                c.acr(e)
                e = evento(ic + obsexp(ma), 'aterra')
                c.acr(e)
            else:
                e = evento(ic + obsexp(mc1), 'chega')
                c.acr(e)
                e = evento(ic + obsexp(ma), 'aterra')
                c.acr(e)
        elif evt.cat() == 'aterra':
            if pista == 'ocupada':
                f.entra(ic)
                if f.comp() > nmea:
                    nmea = f.comp()
            else:
                pista = 'ocupada'
                e = evento(ic + obsexp(me), 'estadia')
                c.acr(e)
                e = evento(ic + obsexp(md), 'descola')
                c.acr(e)
        else: # evt.cat() == 'descola'
            if f.vaziaQ():
                pista = 'livre'
            else:
                f.sai()
                e = evento(ic + obsexp(md), 'descola')
                c.acr(e)



    def finaliza():
        
        print('Tempo medio de espera para descolar', tmed)
        print('Tempo maximo de espera para aterrar de um aviao prioritario', tmeap)
        print('Tempo maximo de esepera para aterrar de um aviao nao prioritario','%.2f' % tmeanp)
        print('Numero maximo de avioes a espera para aterrar', nmea)  
        print('Numero total de avioes que desistiram de estar a espera para aterrar', nad)  
        print('Numero maximo de avioes que esteve no aeroporto', nma)  
        
    
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

