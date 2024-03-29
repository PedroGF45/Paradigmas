from random import randint, random
from math import log
from eventos import evento
from cadeias import cap
from filas import fila

def simula(tec, tpt, tdp, ts):
    
    global c, f, ic, pe, portageiro, nct, nmaxt, nmaxf, tmaxe, ncheg
    
    def obsexp(m):
        x=random()
        return -m*log(x)
    
    def inicializa():
        global c, f, ic, pe, portageiro, nct, nmaxt, nmaxf, tmaxe, ncheg
    
        c=cap()
        f=fila()
        ic=0
        e=evento(ic+obsexp(tec),'cheg', 'crl')
        c.acr(e)
        pe=e
        portageiro = 'livre'
        nct=0
        nmaxt=0
        tmaxe = 0
        ncheg = 0
        nmaxf = 0
    def simula_evento(evt):
            global c, f, ic, pe, portageiro, nct, nmaxt, nmaxf, tmaxe, ncheg
            if evt.cat() == 'cheg':
                e = evento(ic+obsexp(tec), 'cheg', 'crl')
                c.acr(e)
                e = evento(ic+obsexp(tpt), 'fimt', 'crl')
                c.acr(e)
                nct= nct + 1
                if nct > nmaxt:
                    nmaxt = nct
                ncheg = ncheg+1
            elif evt.cat() == 'fimt':
                nct = nct - 1
                x = randint(1,5)
                if x == 5:
                    if portageiro == 'ocupado':
                        f.entra(ic)
                        if f.comp() > nmaxf:
                            nmaxf = f.comp()
                            
                    else:
                        portageiro = 'ocupado'
                        e = evento(ic+obsexp(tdp),'fpag', 'crl')
                        c.acr(e)
                        
            else:#evt.cat() == 'fpag'
                if f.vaziaQ():
                    portageiro = 'livre'
                else:
                    if ic - f.primeiro() > tmaxe: #instrumentação 
                        tmaxe = ic - f.primeiro()
                        f.sai()
                        e = evento(ic+obsexp(tdp),'fpag', 'crl')
                        c.acr(e)
             
    def finaliza():
        #como as variaveis usadas não são alteradas, não é necessario declarar que são globais
        
        print('Número máximo de veículos a atravessar o troço', nmaxt)
        print('Número máximo de veículos a espera para pagar', nmaxf)
        print('Tempo máximo de espera para pagar','%.2f' % tmaxe)
        print('Número de chegadas de veículos troço ', ncheg)  
        
        # corpo do programa simulador:
        
    inicializa()
    i = 0
    while pe.inst() <= ts:
        ic = pe.inst()
        # simula prox evento
        print(dict(iter = i, inst = pe.inst(), cat = pe.cat(), prio = pe.pri()))
        c.mostra()
        simula_evento(pe)
        #atualiza prox evento a simular
        c.retira()
        pe = c.proximo()
        i +=1
    finaliza()
     #fim do programa simulador  

simula(0.5, 0.5, 3, 300)