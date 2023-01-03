from random import random, randint
from math import log
from eventos import evento
from cadeias import cap
from filas import fila_aterragem, fila_descolagem, fila_media

def simula(mc1, mc2, ma, me, md, x, y, ts):
    
    global c, fater, fdesc, fmed, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p, counter
    
    def obsexp(m):
        z = random()
        return -m * log(z)
    
    def inicializa():
        global c, fater, fdesc, fmed, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p, counter
    
        c = cap()
        fater = fila_aterragem()
        fdesc = fila_descolagem()
        fmed = fila_media()
        ic = 0

        
        e = evento(ic + obsexp(mc1), 'chega', 'nao_prioritario') 
        c.acr(e)
        pe = e

        pista = 'livre'
        tmed = 0
        tmeap = 0
        tmeanp = 0
        nmea = 0
        nad = 0
        nma = 0
        counter = 0
    def simula_evento(evt):
        global c, fater, fdesc, fmed, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p, counter
        
        if randint(1,x) == x:
            p = 'prioritario'
        else:
            p = 'nao_prioritario'

        if evt.cat() == 'chega':
            if (ts > 180 and ts < 660): # arrival of new planes depending on the current time of the simulation
                e = evento(ic + obsexp(mc2), 'chega', 'nao_prioritario') 
                c.acr(e)
            else:
                e = evento(ic + obsexp(mc1), 'chega', 'nao_prioritario')
                c.acr(e)

            if pista == 'livre': 
                e = evento(ic + obsexp(me), 'fest', 'nao_prioritario')
                c.acr(e)
                pista = 'ocupada'
            else:
                e = evento(ic + obsexp(ma), 'fate', p)
                c.acr(e)
                fater.entra(ic) 
                if fater.comp() > nmea:
                    nmea = fater.comp()
                          
        elif evt.cat() == 'fate' or evt.cat() == 'fdes':

            # checkar se existe algum aviao prioritario e manda-lo aterrar
            if fater.comp() > 0 and c.getIndex('prioritario') != 0 : # orders the priority plane waiting longer to land´
                e = evento(ic + obsexp(me), 'fest', 'nao_prioritario')
                c.acr(e)
                c.moveToSecond(c.getIndex('prioritario'))
                pista = 'ocupada'
            # se existerem menos de y avioes para descolar, podem aterrar os outros avioes
            elif (fdesc.comp() > y or fater.comp() == 0) and isinstance(c.getFirstIndex('fdes'), int):
                pista = 'ocupada'
                if evt.cat() == 'fate':
                    c.moveToSecond(c.getFirstIndex('fdes'))
                elif isinstance(c.getSecondIndex('fdes'), int):
                    c.moveToSecond(c.getSecondIndex('fdes'))
                
            elif fater.comp() > 0 and isinstance(c.getFirstIndex('fate'), int):
                e = evento(ic + obsexp(me), 'fest', 'nao_prioritario')
                c.acr(e)
                pista = 'ocupada'
                if evt.cat() == 'fdes':
                    c.moveToSecond(c.getFirstIndex('fate'))
                elif isinstance(c.getSecondIndex('fate'), int):
                    c.moveToSecond(c.getSecondIndex('fate'))

                
            else:
                pista = 'livre'

            if fater.comp() > 15:
                for i in range(c.comp()):
                    if ic - c.mostraE(i).inst() > 20 and c.mostraE(i).cat() == 'fate': # randint(1, 10) == 5 and 
                        print('algum foi com o crl AHUAUHEHUAEHAUEHAUHEHAUHEHAUEHAUHEUHAEHAUHEUAHEUHAUHEUHAHUEAHUEUHAEHAUHEEAH')
                        c.retira(i)
                        fater.sai()
                        nad += 1

            if evt.cat() == 'fate' and fater.comp() > 0: 
                fater.sai()
            elif evt.cat() == 'fdes' and fdesc.comp() > 0:
                fdesc.sai()
            
            if evt.cat() == 'fate':
                counter += 1
                if counter > nma:
                    nma = counter
            elif evt.cat() == 'fdes': 
                counter -= 1
            
            if evt.pri() == 'prioritario' and not fater.vaziaQ() and (ic - fater.primeiro() > tmeap) :
                tmeap = ic - fater.primeiro()

            if evt.pri() == 'nao_prioritario' and evt.cat() == 'fate' and not fater.vaziaQ() and (ic - fater.primeiro() > tmeanp):
                tmeanp = ic - fater.primeiro()

            if evt.cat() == 'fdes' and not fdesc.vaziaQ():
                fmed.entra(ic - fdesc.primeiro())

        else:
            e = evento(ic + obsexp(md), 'fdes', 'nao_prioritario')
            c.acr(e)
            fdesc.entra(ic)

    def finaliza():
        tmed = sum(fmed._ri) / fmed.comp()
        print('Tempo medio de espera para descolar','%.2f' % tmed)
        print('Tempo maximo de espera para aterrar de um aviao prioritario','%.2f' % tmeap)
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
        #print('--------------------------')
        #print('evento simulado -> ', dict(iter = i, inst = pe.inst(), cat = pe.cat(), prio = pe.pri()))
        #c.mostra()
        #print('fila pa aterrar ', fater.comp())
        #print('fila pa descolar ', fdesc.comp())
        #print('SIMULAÇAO')
        simula_evento(pe)
        #print('fila pa aterrar ', fater.comp())
        #print('fila pa descolar ', fdesc.comp())
        # atualiza próximo evento a simular
        c.retira(0)
        
        #c.mostra()
        
        pe = c.proximo()
        #print('proximo evento -> ', dict(iter = i, inst = pe.inst(), cat = pe.cat(), prio = pe.pri()))
        #print('--------------------------')
        i += 1
    finaliza()
    #fim do programa simulador  

simula(5, 5 ,20 ,10 ,30 ,10 , 10, 960)
