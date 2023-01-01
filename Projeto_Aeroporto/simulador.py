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
            if (ts > 180 and ts < 660): # arrival of new planes depending on the current time of the simulation
                    e = evento(ic + obsexp(mc2), 'chega', 'indiferente') 
                    c.acr(e)
            else:
                    e = evento(ic + obsexp(mc1), 'chega', 'indiferente')
                    c.acr(e)
            
            if pista == 'livre' and evt.cat() == 'chega': 
                if fater.vaziaQ(): # check if queue is empty
                    e = evento(ic + obsexp(me), 'fate', 'indiferente') # add next event which is end of landing
                    c.acr(e)
                    pista = 'ocupada'
                else:
                    e = evento(ic + obsexp(me), 'fate', 'indiferente')
                    c.acr(e)
                    fater.sai()
                    pista = 'ocupada'
            elif pista == 'ocupada' and evt.cat() == 'chega': 
                    fater.entra(ic) 
                    if fater.comp() > nmea:
                        nmea = fater.comp()

                    
        elif evt.cat() == 'fate' or evt.cat() == 'fdes':

            # checkar se existe algum aviao prioritario e manda-lo aterrar
            # se existerem menos de y avioes para fdesr, podem fater os outros avioes
            # se nao existerem avioes nas filas, pista livre         
                

            if ic - evt.inst() > 20 and evt.pri() == 'nao_prioritario' and randint(1, 10) == 5 and fater.comp() > 15:
                fater.elimina(evt.inst())

        elif evt.cat() == 'fest':
            e = evento(ic + obsexp(md), 'fdes', 'indiferente')
            c.acr(e)

        else:
            if pista == 'livre' and evt.cat() == 'fdes':
                    if fdesc.vaziaQ(): # check if queue is empty
                        pista = 'ocupada'
                    else:
                        e = evento(ic + obsexp(me), 'fdes', 'indiferente') # add next event which is end of take-off
                        c.acr(e)
                        fdesc.sai()
                        pista = 'ocupada'
            elif pista == 'ocupada' and evt.cat() == 'fdes': 
                    e = evento(ic + obsexp(me), 'fdes', 'indiferente')
                    c.acr(e)
                    fdesc.entra(ic) 




    def finaliza():
        
        print('Tempo medio de espera para fdesr', tmed)
        print('Tempo maximo de espera para fater de um aviao prioritario', tmeap)
        print('Tempo maximo de espera para fater de um aviao nao prioritario','%.2f' % tmeanp)
        print('Numero maximo de avioes a espera para fater', nmea)  
        print('Numero total de avioes que desistiram de estar a espera para fater', nad)  
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