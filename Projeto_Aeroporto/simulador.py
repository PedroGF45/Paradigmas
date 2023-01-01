from random import random, randint
from math import log
from eventos import evento
from cadeias import cap
from filas import fila_aterragem, fila_descolagem

def simula(mc1, mc2, ma, me, md, x, ts):
    
    global c, f, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p
    
    def obsexp(m):
        x = random()
        return -m * log(x)
    
    def inicializa():
        global c, fater, fdesc, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p
    
        c = cap()
        fater = fila_aterragem()
        fdesc = fila_descolagem()
        ic = 0

        if 1/x == x:
            p = 'prioritario'
        else:
            p = 'nao_prioritario'
        e = evento(ic + obsexp(mc1), 'chega', p) 
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
        global c, fater, fdesc, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p

        if 1/x == x:
            p = 'prioritario'
        else:
            p = 'nao_prioritario'

        if evt.cat() == 'chega':
            if (ts > 180 and ts < 660):
                    e = evento(ic + obsexp(mc2), 'chega', 'indiferente')
                    c.acr(e)
                    e = evento(ic + obsexp(ma), 'aterra', p)
                    c.acr(e)
            else:
                    e = evento(ic + obsexp(mc1), 'chega', 'indiferente')
                    c.acr(e)
                    e = evento(ic + obsexp(ma), 'aterra', p)
                    c.acr(e)

        elif evt.cat() == 'aterra' or evt.cat() == 'descola':
            # checkar se existe algum aviao prioritario e manda-lo aterrar
            # se existerem menos de y avioes para descolar, podem aterrar os outros avioes
            # se nao existerem avioes nas filas, pista livre
            if pista == 'ocupada': # and p == x:
                fater.entra(ic) 
                if fater.comp() > nmea:
                    nmea = fater.comp()
            else:
                pista = 'ocupada'
                fater.sai()
                e = evento(ic + obsexp(me), 'estadia', 'indiferente')
                c.acr(e)

            if ic - evt.inst() > 20 and evt.pri() == 'nao_prioritario' and randint(1, 10) == 5 and fater.comp() > 15:
                fater.elimina(evt.inst())

        elif evt.cat() == 'estadia':
            e = evento(ic + obsexp(md), 'descola', 'indiferente')
            c.acr(e)

        else: # evt.cat() == 'descola' 
            if f.vaziaQ():
                pista = 'livre'
            else: 
                fdesc.entra(ic)
                e = evento(ic + obsexp(md), 'descola', 'indiferente')
                c.acr(e)




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