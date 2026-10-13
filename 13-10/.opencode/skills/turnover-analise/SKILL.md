---
name: turnover-analise
description: Calcula e analisa turnover no Excel. Use quando pedir turnover, rotatividade, retencao, headcount ou analise RH.
---

# Turnover Analise

Skill para transformar dados de RH em analise de turnover padronizada, baseada em:
CAMILO, Sabrina. Como calcular o turnover no Excel: passo a passo. Solides Blog, 09 set. 2026.
https://solides.com.br/blog/calcular-o-turnover-no-excel/

## O que eu faco
- Monto planilha mensal de turnover no Excel
- Calculo headcount medio e taxa de turnover com formula visivel
- Segmento por area, unidade, gestor, cargo, tempo de casa e tipo voluntario/involuntario
- Interpreto tendencia e proponho acoes de retencao

## Quando me usar
Use quando o usuario pedir turnover, rotatividade, calcular turnover no Excel, analise de retencao, headcount ou diagnostico RH para DECC0294 / ADM-2026-INFORMATICA.

## Como agir

### 1. Levantar dados base
Pedir ou localizar:
- Admissoes no periodo (mes/ano)
- Desligamentos no periodo (separar voluntario x involuntario)
- Headcount inicio e headcount fim do periodo
- Opcional para segmentacao: area, unidade, gestor, cargo, tempo de casa, motivo
- Definir regra: incluir estagiarios/temporarios? incluir transferencias internas? Manter mesmo criterio todo mes.

### 2. Montar estrutura da planilha
Linha 1 como cabecalho, um mes por linha:
- A: Mes
- B: Admissoes
- C: Desligamentos
- D: Headcount inicio
- E: Headcount fim
- F: Headcount medio
- G: Turnover (%)

### 3. Calcular headcount medio
Na celula F2:
```
=MEDIA(D2;E2)
```
Arrastar para baixo. Evita distorcao em meses com muita movimentacao.

### 4. Aplicar formula do turnover
Na celula G2:
```
=(((B2+C2)/2)/F2)*100
```
Formatar como Porcentagem. Arrastar para baixo.
Formula: Turnover (%) = ((Admissoes + Desligamentos) / 2) / Headcount medio x 100

Variacao simplificada (so desligamentos):
```
Desligamentos / Headcount medio x 100
```
Documentar qual regra foi usada e manter em todos os relatorios.

### 5. Interpretar - tendencia, concentracao, causa
1. Tendencia 6-12 meses: subindo, estavel ou caindo? Ha picos apos bonus, avaliacao ou troca de lideranca?
2. Comparar com media interna do ano e entre areas semelhantes, nao so com numero ideal generico.
3. Quebrar onde doi: area, unidade, gestor, cargo, tempo de casa (ate 90 dias, 6 meses, 1 ano).
4. Separar voluntario alto (expectativa, lideranca, carga, clima, remuneracao) x involuntario alto (performance, estrutura, selecao, onboarding).
5. Atencao a turnover de novos colaboradores: indica falha em selecao, onboarding, treinamento ou clareza de metas.

### 6. Transformar em acao
- Voluntario alto em time especifico: conversa com lideranca, revisao metas/ritmo, 1:1, pesquisa pulso, plano desenvolvimento
- Pico 3-6 meses: reforcar onboarding, trilha treinamento, mentor/buddy, check-ins 30/60/90 dias
- Cargo critico: revisao faixa salarial/beneficios, trilha carreira, ajuste perfil selecao, sucessao
- Diferenca entre gestores: desenvolvimento lideranca, alinhamento praticas, clima por time

Entregar: tabela mensal + grafico evolucao + ranking motivos + 3 acoes com responsavel, prazo e meta.

## Regras honestas
- NAO inventar numeros de admissoes, desligamentos ou headcount
- Se faltar dado, pedir ao usuario e marcar como PENDENTE
- Sempre mostrar conta visivel (formula + valores usados)
- Sempre marcar saida como RASCUNHO e listar decisoes humanas pendentes
- Citar fonte base: Camilo (2026) Solides

## Exemplo de estrutura de entrega
```
1. Capa - titulo, disciplina DECC0294, autor, data
2. Resumo executivo - taxa atual, tendencia, ponto critico (ate 5 linhas)
3. Memoria de calculo - tabela mensal com formula visivel
4. Diagnostico - onde concentra + voluntario x involuntario
5. Plano retencao - 3 acoes com responsavel/prazo/meta
6. Anexos - base CSV, prints planilha
```
