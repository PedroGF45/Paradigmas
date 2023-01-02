from random import random, randint
from math import log
from eventos import evento
from cadeias import cap
from filas import fila_aterragem, fila_descolagem

def simula(mc1, mc2, ma, me, md, x, y, ts):
    
    global c, fater, fdesc, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p
    
    def obsexp(m):
        z = random()
        return -m * log(z)
    
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
        
        if evt.cat() == 'chega':
            if (ts > 180 and ts < 660): # arrival of new planes depending on the current time of the simulation
                e = evento(ic + obsexp(mc2), 'chega', 'indiferente') 
                c.acr(e)
            else:
                e = evento(ic + obsexp(mc1), 'chega', 'indiferente')
                c.acr(e)

            if randint(1,x) == x:
                p = 'prioritario'
            else:
                p = 'nao_prioritario'

            if pista == 'livre':
                if fater.vaziaQ(): # check if queue is empty
                    e = evento(ic + obsexp(ma), 'fate', p)
                    c.acr(e)
                    pista = 'ocupada'
                else:
                    e = evento(ic + obsexp(ma), 'fate', p)
                    c.acr(e)
                    fater.sai()
                    pista = 'ocupada'
            else:
                e = evento(ic + obsexp(me), 'fate', p)
                c.acr(e)
                fater.entra(ic) 
                if fater.comp() > nmea:
                    nmea = fater.comp()

                    
        elif evt.cat() == 'fate' or evt.cat() == 'fdes':

            pista = 'livre' # frees the runway

            # checkar se existe algum aviao prioritario e manda-lo aterrar
            if fater.comp() > 0 and isinstance(c.getIndexPri('prioritario'), int): # orders the priority plane waiting longer to land
                c.moveToFirst(c.getIndexPri('prioritario'))
                e = evento(ic + obsexp(me), 'fest', 'indiferente')
                c.acr(e)
                pista = 'ocupada'
                fater.sai()
                print('OK')
            # se existerem menos de y avioes para descolar, podem aterrar os outros avioes
            elif fdesc.comp() > y and not c.vaziaQ():
                c.moveToFirst(c.getIndexCat('fdes'))
                pista = 'ocupada'
                fdesc.sai()
                print('xd')
            elif fater.comp() > 0 and isinstance(c.getIndexCat('fate'), int):
                c.moveToFirst(c.getIndexCat('fate'))
                e = evento(ic + obsexp(me), 'fest', 'indiferente')
                c.acr(e)
                pista = 'ocupada'
                fater.sai()   
                print('wtf')
        else:
            e = evento(ic + obsexp(md), 'fdes', 'indiferente')
            c.acr(e)
            fdesc.entra(ic)

    def finaliza():
        
        print('Tempo medio de espera para descolar', tmed)
        print('Tempo maximo de espera para aterrar de um aviao prioritario', tmeap)
        print('Tempo maximo de espera para aterrar de um aviao nao prioritario','%.2f' % tmeanp)
        print('Numero maximo de avioes a espera para aterrar', nmea)  
        print('Numero total de avioes que desistiram de estar a espera para aterrar', nad)  
        print('Numero maximo de avioes que esteve no aeroporto', nma)  
        
    # corpo do programa simulador:       
    inicializa()
    i = 0
    while pe.inst() <= ts:
        ic = pe.inst()
        # simula próximo evento:
        print('c -> ', dict(iter = i, inst = pe.inst(), cat = pe.cat(), prio = pe.pri()))
        c.mostra()
        simula_evento(pe)
        # atualiza próximo evento a simular
        c.primeiro()
        c.retira()
        print('--------------------------')
        c.primeiro()
        c.mostra()
        pe = c.proximo()
        i += 1
    finaliza()
    #fim do programa simulador  

