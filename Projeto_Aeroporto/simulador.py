from random import random, randint
from math import log
from eventos import evento
from cadeias import cap
from filas import fila_aterragem, fila_descolagem, fila_media

# problema de instanciacao de eventos

def simula(mc1, mc2, ma, me, md, x, y, k, ts):
    
    global c, fater, fdesc, fmed, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p, counter
    
    def obsexp(m):
        z = random()
        return -m * log(z)
    
    def inicializa():
        global c, fater, fdesc, fmed, ic, pe, pista, tmed, tmeap, tmeanp, nmea, nad, nma, p, counter
    
        # create objects using classes provided
        c = cap()
        fater = fila_aterragem()
        fdesc = fila_descolagem()
        fmed = fila_media()
        
        # set the initial instant of the simulation to 0
        ic = 0
        
        # number of planes ready to take-off in the beginning of the simulation
        n = 0 
        while n < k:
            e = evento(ic + obsexp(md), 'fdes', 'nao_prioritario')
            c.acr(e)
            fdesc.entra(ic)
            n += 1
        
        # add the first airplane arriving at the airport
        e = evento(ic + obsexp(mc1), 'chega', 'nao_prioritario') 
        c.acr(e)
        pe = e

        #definition of other variables
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
                e = evento(ic + obsexp(me), 'fate', 'nao_prioritario')
                c.acr(e)
                pista = 'ocupada'
            else:
                e = evento(ic + obsexp(ma), 'fate', p) # nao ha necessidade de calcular 
                c.acr(e)
                fater.entra(ic) 
                if fater.comp() > nmea:
                    nmea = fater.comp()
                          
        elif evt.cat() == 'fate' or evt.cat() == 'fdes':

            # If there's a priority plane, then tell the priorty plane waiting longer to land right away
            if fater.comp() > 0 and c.getfirstIndexPri('prioritario') != 0 : 
                e = evento(ic + obsexp(me), 'fest', 'nao_prioritario')
                c.acr(e)
                c.moveToSecond(c.getfirstIndexPri('prioritario'))
                pista = 'ocupada'

            # if there's more than y planes waiting to land, tell the plane waiting longer in the queue to take-off
            elif (fdesc.comp() > y or fater.comp() == 0) and isinstance(c.getFirstIndexCat('fdes'), int):
                pista = 'ocupada'
                if evt.cat() == 'fate':
                    c.moveToSecond(c.getFirstIndexCat('fdes'))

                # careful - if the event being simulated has the category 'fdes' then we should move the second event with 'fdes' and not the first
                elif isinstance(c.getSecondIndexCat('fdes'), int):
                    c.moveToSecond(c.getSecondIndexCat('fdes'))
                
            # if there's planes waiting to land, tell the plane waiting longer to land
            elif fater.comp() > 0 and isinstance(c.getFirstIndexCat('fate'), int):
                e = evento(ic + obsexp(me), 'fest', 'nao_prioritario')
                c.acr(e)
                pista = 'ocupada'
                if evt.cat() == 'fdes':
                    c.moveToSecond(c.getFirstIndexCat('fate'))

                # careful - if the event being simulated has the category 'fate' then we should move the second event with 'fdes' and not the first
                elif isinstance(c.getSecondIndexCat('fate'), int):
                    c.moveToSecond(c.getSecondIndexCat('fate'))

            # otherwise the runway is free    
            else:
                pista = 'livre'

            # if there's more than 15 planes waiting to land and a plane is waiting more than 20 mins to land it has a probability of 1/10 to give-up landing
            if fater.comp() > 15:
                l = 0
                while l < c.comp():
                    if ic - c.mostraE(l).inst() > 20 and c.mostraE(l).cat() == 'fate' and randint(1, 10) == 5:
                        c.retira(l)
                        fater.sai()
                        nad += 1
                    #else:
                    l += 1

            # remove plane from waiting queues
            if evt.cat() == 'fate' and fater.comp() > 0: 
                fater.sai()
            elif evt.cat() == 'fdes' and fdesc.comp() > 0:
                fdesc.sai()
            
            # count of maximum number of planes in the airport
            if evt.cat() == 'fate':
                counter += 1
                if counter > nma:
                    nma = counter
            elif evt.cat() == 'fdes': 
                counter -= 1
            
            # calculus of maximum holding landing time of priority planes
            if evt.pri() == 'prioritario' and not fater.vaziaQ() and (ic - fater.primeiro() > tmeap) :
                tmeap = ic - fater.primeiro()

            # calculus of maximum holding landing time of non priority planes
            if evt.pri() == 'nao_prioritario' and evt.cat() == 'fate' and not fater.vaziaQ() and (ic - fater.primeiro() > tmeanp):
                tmeanp = ic - fater.primeiro()

            # adding instants of take-off times to a list
            if evt.cat() == 'fdes' and not fdesc.vaziaQ():
                fmed.entra(ic - fdesc.primeiro())

        #evt.cat() == 'fest'
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
        
    # body of the simulator:       
    inicializa()
    while pe.inst() <= ts:
        ic = pe.inst()
        simula_evento(pe)
        c.retira(0)
        pe = c.proximo()
    finaliza()
    #end of simulation  