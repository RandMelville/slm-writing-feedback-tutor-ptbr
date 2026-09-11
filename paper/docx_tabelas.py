"""Deixa legiveis as tabelas de um .docx gerado pelo pandoc.

O pandoc desenha as tabelas so por estilo, e boa parte dos leitores (Quick Look,
Google Docs, Pages) ignora borda que vem de estilo: a tabela chega sem linha
nenhuma. Aqui a formatacao entra direto em cada tabela: grade completa, respiro
nas celulas e cabecalho em negrito com fundo cinza.

Uso: python3 docx_tabelas.py arquivo.docx [outro.docx ...]
"""
import re
import shutil
import sys
import zipfile

BORDAS = (
    '<w:tblBorders>'
    '<w:top w:val="single" w:sz="8" w:space="0" w:color="595959" />'
    '<w:left w:val="single" w:sz="8" w:space="0" w:color="595959" />'
    '<w:bottom w:val="single" w:sz="8" w:space="0" w:color="595959" />'
    '<w:right w:val="single" w:sz="8" w:space="0" w:color="595959" />'
    '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="A6A6A6" />'
    '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="A6A6A6" />'
    '</w:tblBorders>'
)
MARGENS = (
    '<w:tblCellMar>'
    '<w:top w:w="80" w:type="dxa" /><w:left w:w="108" w:type="dxa" />'
    '<w:bottom w:w="80" w:type="dxa" /><w:right w:w="108" w:type="dxa" />'
    '</w:tblCellMar>'
)
FUNDO = '<w:shd w:val="clear" w:color="auto" w:fill="EDEDED" />'

# largura util da pagina A4 com margem de 2 cm, em twips
LARGURA_UTIL = 9638


def larguras(tabela):
    """Reparte a largura da pagina entre as colunas conforme o conteudo.

    O pandoc escreve todas as colunas iguais, o que faz uma coluna de duas letras
    ocupar o mesmo espaco de uma de trinta palavras. Aqui cada coluna ganha, no
    minimo, o espaco da sua maior palavra (que nao quebra), e o que sobra e
    dividido na proporcao do texto que cada uma carrega.
    """
    linhas = re.findall(r'<w:tr>.*?</w:tr>', tabela, flags=re.S)
    if not linhas:
        return []
    peso, palavra = [], []
    for linha in linhas:
        for i, celula in enumerate(re.findall(r'<w:tc>.*?</w:tc>', linha, flags=re.S)):
            texto = ''.join(re.findall(r'<w:t(?:\s[^>]*)?>(.*?)</w:t>', celula, flags=re.S))
            if i >= len(peso):
                peso.append(0)
                palavra.append(0)
            peso[i] = max(peso[i], len(texto))
            maior = max((len(w) for w in texto.split()), default=0)
            palavra[i] = max(palavra[i], maior)

    # piso: a maior palavra da coluna, ~120 twips por caractere, mais o respiro
    piso = [min(max(p * 120 + 220, 600), 3200) for p in palavra]
    if sum(piso) >= LARGURA_UTIL:
        fator = LARGURA_UTIL / sum(piso)
        larg = [max(int(w * fator), 400) for w in piso]
    else:
        sobra = LARGURA_UTIL - sum(piso)
        pesos = [min(max(p, 6), 90) for p in peso]
        total = sum(pesos)
        larg = [piso[i] + int(sobra * pesos[i] / total) for i in range(len(piso))]
    resto = LARGURA_UTIL - sum(larg)
    larg[larg.index(max(larg))] += resto
    return larg


def negrita(xml):
    """Poe <w:b /> em cada run, respeitando a ordem exigida pelo OOXML."""
    def com_rpr(m):
        rpr = m.group(1)
        if '<w:b />' in rpr or '<w:b/>' in rpr:
            return m.group(0)
        estilo = re.match(r'(<w:rStyle[^>]*/>)', rpr)
        if estilo:  # rStyle precisa vir antes de b
            return '<w:rPr>' + estilo.group(1) + '<w:b />' + rpr[estilo.end():] + '</w:rPr>'
        return '<w:rPr><w:b />' + rpr + '</w:rPr>'

    xml = re.sub(r'<w:rPr>(.*?)</w:rPr>', com_rpr, xml, flags=re.S)
    return xml.replace('<w:r><w:t', '<w:r><w:rPr><w:b /></w:rPr><w:t')


def formata_tabela(tabela):
    def props(m):
        p = m.group(0)
        if '<w:tblBorders>' not in p:
            if '<w:tblLayout' in p:
                p = p.replace('<w:tblLayout', BORDAS + '<w:tblLayout', 1)
            elif '<w:tblLook' in p:
                p = p.replace('<w:tblLook', BORDAS + '<w:tblLook', 1)
            else:
                p = p.replace('</w:tblPr>', BORDAS + '</w:tblPr>', 1)
        if '<w:tblCellMar>' not in p:
            if '<w:tblLook' in p:
                p = p.replace('<w:tblLook', MARGENS + '<w:tblLook', 1)
            else:
                p = p.replace('</w:tblPr>', MARGENS + '</w:tblPr>', 1)
        return p

    tabela = re.sub(r'<w:tblPr>.*?</w:tblPr>', props, tabela, count=1, flags=re.S)

    larg = larguras(tabela)
    if larg:
        grade = '<w:tblGrid>' + ''.join(f'<w:gridCol w:w="{w}" />' for w in larg) + '</w:tblGrid>'
        tabela = re.sub(r'<w:tblGrid>.*?</w:tblGrid>', grade, tabela, count=1, flags=re.S)

        def celulas(m):
            linha = m.group(0)
            i = [0]

            def largura_da_celula(mc):
                c = mc.group(0)
                w = larg[i[0]] if i[0] < len(larg) else larg[-1]
                i[0] += 1
                tcw = f'<w:tcW w:w="{w}" w:type="dxa" />'
                if '<w:tcPr />' in c:
                    return c.replace('<w:tcPr />', '<w:tcPr>' + tcw + '</w:tcPr>', 1)
                if '<w:tcW' in c:
                    return c
                return c.replace('<w:tcPr>', '<w:tcPr>' + tcw, 1)

            return re.sub(r'<w:tc>.*?</w:tc>', largura_da_celula, linha, flags=re.S)

        tabela = re.sub(r'<w:tr>.*?</w:tr>', celulas, tabela, flags=re.S)

    primeira = re.search(r'<w:tr>.*?</w:tr>', tabela, flags=re.S)
    if primeira:
        cabecalho = primeira.group(0)
        # o sombreado entra no fim do tcPr: no OOXML, shd vem depois de tcW
        nova = cabecalho.replace('<w:tcPr />', '<w:tcPr>' + FUNDO + '</w:tcPr>')
        nova = re.sub(r'<w:tcPr>((?:(?!</w:tcPr>).)*?)</w:tcPr>',
                      lambda m: m.group(0) if '<w:shd' in m.group(1)
                      else '<w:tcPr>' + m.group(1) + FUNDO + '</w:tcPr>',
                      nova, flags=re.S)
        nova = negrita(nova)
        tabela = tabela[:primeira.start()] + nova + tabela[primeira.end():]
    return tabela


def processa(caminho):
    zin = zipfile.ZipFile(caminho)
    itens = {n: zin.read(n) for n in zin.namelist()}
    zin.close()

    doc = itens['word/document.xml'].decode('utf-8')
    if doc.count('<w:tbl>') != doc.count('</w:tbl>'):
        raise SystemExit(f'{caminho}: XML de tabela inesperado')
    total = 0

    def troca(m):
        nonlocal total
        total += 1
        return formata_tabela(m.group(0))

    doc = re.sub(r'<w:tbl>.*?</w:tbl>', troca, doc, flags=re.S)
    itens['word/document.xml'] = doc.encode('utf-8')

    tmp = caminho + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for nome, dados in itens.items():
            zout.writestr(nome, dados)
    shutil.move(tmp, caminho)
    return total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for arq in sys.argv[1:]:
        print(f'{arq}: {processa(arq)} tabelas formatadas')
