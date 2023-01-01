from random import random, randint
from math import log
from eventos import evento
from cadeias import cap
from filas import fila

def simula(mc1, mc2, ma, me, md, x, ts):
    
    global c, f, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p
    
    def obsexp(m):
        x = random()
        return -m * log(x)
    
    def inicializa():
        global c, f, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p
    
        c = cap()
        f = fila()
        ic = 0
        e = evento(ic + obsexp(mc1), 'chega')
        c.acr(e, 'nao_pri')
        pe = e
        pista = 'livre'
        tmed = 0
        tmeap = 0
        tmeanp = 0
        nmea = 0
        nad = 0
        nma = 0
        print('aqui primeiro')
    def simula_evento(evt):
        global c, f, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p
        if evt.cat() == 'chega':
            if (ts > 180 and ts < 660):
                e = evento(ic + obsexp(mc2), 'chega')
                c.acr(e, 'nao_pri')
                e = evento(ic + obsexp(ma), 'aterra')
                c.acr(e, 'nao_pri')
            else:
                e = evento(ic + obsexp(mc1), 'chega')
                c.acr(e, 'nao_pri')
                e = evento(ic + obsexp(ma), 'aterra')
                c.acr(e, 'nao_pri')
        elif evt.cat() == 'aterra':
            p = randint(1, x)
            if pista == 'ocupada': # and p == x:
                f.entra(ic) 
                if f.comp() > nmea:
                    nmea = f.comp()
            else:
                pista = 'ocupada'
                e = evento(ic + obsexp(me), 'estadia')
                c.acr(e, 'nao_pri')
                e = evento(ic + obsexp(md), 'descola')
                c.acr(e, 'nao_pri')
            if ic - evt.inst() > 20 and randint(1, 10) == 5 and f.comp() > 15:
                f.elimina(evt.inst())
        # elif evt.cat() == 'estadia':
        else: # evt.cat() == 'descola' 
            if f.vaziaQ():
                pista = 'livre'
            else:
                f.sai()
                e = evento(ic + obsexp(md), 'fimd')
                c.acr(e, 'nao_pri')




    def finaliza():
        
        print('Tempo medio de espera para descolar', tmed)
        print('Tempo maximo de espera para aterrar de um aviao prioritario', tmeap)
        print('Tempo maximo de espera para aterrar de um aviao nao prioritario','%.2f' % tmeanp)
        print('Numero maximo de avioes a espera para aterrar', nmea)  
        print('Numero total de avioes que desistiram de estar a espera para aterrar', nad)  
        print('Numero maximo de avioes que esteve no aeroporto', nma)  
        
    
    
    # corpo do programa simulador:       
    inicializa()
    while pe.inst() <= ts:
        ic = pe.inst()
        # simula próximo evento:
        simula_evento(pe)
        # atualiza próximo evento a simular
        c.retira()
        pe = c.proximo()
    finaliza()
    #fim do programa simulador  