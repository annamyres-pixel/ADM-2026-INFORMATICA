# Análise de Variação - Controle Gerencial em Organização Pública

Data: 15/09/2026

## 1. Instrução usada (idêntica nas duas execuções)

Nenhum arquivo de instrução/prompt versionado no repositório. `git log` mostra apenas `Initial commit` (fbc711f) com `.gitattributes`. Arquivos em `saidas/` são `untracked`.

Instrução reconstruída pelo conteúdo das duas saídas (5 proposições idênticas em estrutura):

> Definir controle gerencial em organização pública em 5 linhas: conceito, etapas/instrumentos, diferença vs. controle legal-formal, e autor(es) de referência.

## 2. Arquivos de resposta em `saidas/`

### saidas/teste-variacao-1.md
```
Controle gerencial numa organização pública é o processo pelo qual os gestores garantem que os recursos sejam obtidos e usados com eficiência, eficácia e efetividade.
Envolve planejamento, orçamentação, execução, monitoramento e avaliação do desempenho organizacional.
Diferencia-se do controle legal-formal por focar no apoio à decisão e no alcance dos objetivos estratégicos e das políticas públicas.
Utiliza instrumentos como indicadores de desempenho, contabilidade de custos, orçamento e sistemas de informação gerencial.
Autor de referência: Robert N. Anthony, clássico em *Management Control Systems*, com adaptações ao setor público por autores como Peter Jackson.
```

### saidas/teste-variacao-2.md
```
Controle gerencial na organização pública é o conjunto de processos para assegurar que a estratégia se converta em ação e resultados de valor público.
Compreende planejar objetivos e metas, alocar recursos via orçamento e acompanhar a execução por indicadores e custos.
Enfatiza a avaliação de desempenho (eficiência, eficácia e efetividade) e o feedback para correção de rumos e aprendizagem organizacional.
Distingue-se do controle formal/legalista por orientar a tomada de decisão gerencial e a responsabilização por resultados.
Autor de referência: Robert N. Anthony e Vijay Govindarajan — Sistemas de Controle Gerencial; no Brasil, referência complementar em controle no setor público: Djalma de Pinho Rebouças de Oliveira.
```

## 3. O que mudou entre as duas (diff)

Todas as 5 linhas foram parafraseadas mantendo o núcleo, mas com troca de ênfase e de referência:

1. **Linha 1 - Conceito:** `processo pelo qual os gestores garantem que os recursos sejam obtidos e usados com eficiência, eficácia e efetividade` -> `conjunto de processos para assegurar que a estratégia se converta em ação e resultados de valor público` (introduz "valor público" - Mark Moore - ausente na v1)
2. **Linha 2 - Etapas:** `planejamento, orçamentação, execução, monitoramento e avaliação` -> `planejar objetivos e metas, alocar recursos via orçamento e acompanhar a execução por indicadores e custos` (compactação)
3. **Linha 3 - Diferença vs. controle formal:** `apoio à decisão e alcance dos objetivos estratégicos e das políticas públicas` -> `avaliação de desempenho (eficiência, eficácia e efetividade) e o feedback para correção de rumos e aprendizagem organizacional` (desloca 3Es para linha 3 e adiciona feedback/aprendizagem)
4. **Linha 4 - Instrumentos:** lista explícita `indicadores, contabilidade de custos, orçamento e sistemas de informação gerencial` -> diluído em linha 2 e substituído por `responsabilização por resultados` na linha 4
5. **Linha 5 - Autor:** `Robert N. Anthony [...] Peter Jackson` -> `Robert N. Anthony e Vijay Govindarajan [...] Djalma de Pinho Rebouças de Oliveira` (troca completa da referência complementar)

## 4. Julgamento - qual está mais correta (com justificativa)

**Empate técnico no núcleo, vantagem marginal para `teste-variacao-1.md` na definição e para `teste-variacao-2.md` na referenciação.**

* **Definição:** `teste-variacao-1.md:1` é literal a Anthony, R.N. *Planning and Control Systems* (1965) - "resources be obtained and used effectively and efficiently" - verificável. `teste-variacao-2.md:1` introduz "valor público", conceito de Mark Moore, não de Anthony.
* **Instrumentos:** `teste-variacao-1.md:4` lista instrumentos canônicos corretamente. `teste-variacao-2.md` omite Sistemas de Informação Gerencial.
* **Referências:** `Anthony + Govindarajan` em `teste-variacao-2.md:5` está correto - desde a 9ª ed. (1998) *Management Control Systems* é Anthony/Govindarajan (confirmado HBS e WorldCat). `teste-variacao-1.md:5` omite coautor. Porém ambos erram no complementar brasileiro: `Peter Jackson` não é referência canônica em controle público (provável alucinação - homônimo do cineasta) e `Djalma de Pinho Rebouças de Oliveira` é autor real de *Sistemas, organização e métodos* (Atlas) mas não especialista em controle no setor público - ambos exigem verificação primária e não devem ser citados sem checagem.

Para prova/avaliação que cobra Anthony clássico: usar `teste-variacao-1.md` com correção da referência para Anthony & Govindarajan.

## 5. Implicação para uso em trabalho avaliado

Mesmo prompt gera parafraseamento e troca de referências (risco de alucinação), logo IA é não-determinística e exige verificação em fonte primária e padronização de referências, sob risco de reprodutibilidade e penalidade por citação inexata.
