import os

# Input
# ---aaattcc---cccc--
# aactgtgactgcatgcatgactgactg
# Output
# aaattcc---cccc
# aaattcc---cccc

def contar_no_comeco(sequencia):
    '''conta os - no começo da sequência'''

    tracos = 0
    for c in sequência:
        if c == '-':
            tracos = + 1
        else:
            break
        return tracos

def contar_no_final(sequencia):
    '''conta os - no final da sequência'''

    return contar_no_comeco(reversed(sequencia))

def editar_sequencias(sequencia1, sequencia2):
    _inicio = contar_no_comeco(sequencia1)
    _final = contar_no_final(sequencia1)

    #RETORNAR EM PYTHON
    return (sequencia1[_inicio:-_final if _final != 0 else len (sequencia1)],
            sequencia2[_inicio:-_final if _final != 0 else len (sequencia2)])

def teste ():
    '''Teste'''

    sequencia1 = '---aaattcc---cccc--'
    sequencia2 = 'aactgtgactgcatgcatgactgactg'

    ed1, ed2 = editar_sequencias(sequencia1, sequencia2)
    print (ed1)
    print (ed2)

def encontrar_gb (linhas):
    '''encontrar >gb'''

    indice = 0
    for l in linhas:
        if '>gb' in l:
            break
        indice = indice + 1
    return indice

if __name__ == "__main__":

    teste()
    with open ('input/DENV1-X-gb_A75711.fasta.aln') as fasta:
        conteudo = fasta.read()
        #readlines ()
        linhas = conteudo.split('\n')
        #print (linhas)
        cabecalho1 = linhas [0]
        indice = encontrar_gb(linhas)
        
        cabecalho2 = linhas[indice]
        sequencia1 = ''.join(linhas[1:indice])
        sequencia2 = ''.join(linhas[indice+1:])

        #abrir arquivo novo
        with open (os.path.join('output', 'resultado.fasta'), 'w')as res:
            #sequencias editadas retornadas
            editada1, editada2 = editar_sequencias(sequencia1, sequencia2)
            #sequencia editada
            res.write(cabecalho1 + '\n')
            res.write(editada1 + '\n')
            res.write(cabecalho2 + '\n')
            res.write(editada2)