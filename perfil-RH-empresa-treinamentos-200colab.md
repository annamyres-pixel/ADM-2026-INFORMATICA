# 🏢 Simulação de Dados de RH — Empresa Especializada em Treinamentos e Desenvolvimento de Equipes e Líderes
### Disciplina: ADM-2026-INFORMÁTICA | Base com 200 colaboradores | Dados fictícios para fins acadêmicos

> **Arquivos desta entrega:**
> 1. `dados-rh-200-colaboradores.csv` — base com 200 linhas + cabeçalho, separador `;`, encoding UTF-8
> 2. Este relatório — perfil da empresa + análise do perfil profissional
> 3. Scripts geradores: `gerar_dados_rh.py` (reprodutível, seed 42)

---

## 1. Perfil da Empresa Simulada

**Nome fantasia:** TALENTAR — Desenvolvimento de Equipes e Líderes  
**Razão social fictícia:** Talentar Educação Corporativa S.A.  
**Porte:** Média empresa — 200 colaboradores  
**Setor:** Serviços especializados de mão de obra intelectual / Educação corporativa  
**Modelo de negócio:** Criação de treinamentos sob medida (presencial, híbrido e EAD), trilhas de liderança, coaching executivo, assessment psicológico, consultoria de clima e cultura.

**Missão:** Desenvolver pessoas, equipes e líderes para gerar resultado sustentável nos clientes.  
**Visão:** Ser referência nacional em universidade corporativa terceirizada até 2030.  
**Valores:** Aprendizagem contínua, ética, diversidade, foco em evidências, colaboração.

**Organograma resumido:**

```
Diretoria (4)
├── Academia de Liderança e Coaching (31)
├── Design Instrucional e Conteúdo EAD (30)
├── Facilitação e Instrutoria Corporativa (34)
├── Consultoria em Desenvolvimento de Equipes (26)
├── Psicologia Organizacional e Avaliação (15)
├── Comercial e Vendas B2B (22)
├── Marketing e Growth (14)
├── Operações e CX — Sucesso do Cliente (11)
├── Administrativo-Financeiro + RH Interno (8)
└── TI e Plataforma EAD (5)
```

> Lógica da simulação: empresa intensiva em conhecimento — 65% do headcount está no core (Academia + Design + Facilitação + Consultoria + Psicologia = 136 pessoas / 68%).

---

## 2. Dicionário de Dados (`dados-rh-200-colaboradores.csv`)

| Coluna | Descrição | Exemplo |
|---|---|---|
| ID | Matrícula fictícia COL-001 a COL-200 | COL-001 |
| Nome | Nome fictício gerado aleatoriamente | Diego Monteiro Araujo |
| Sexo | F / M | F |
| Idade | Anos | 38 |
| Estado_Civil | Solteiro(a), Casado(a), União Estável, Divorciado(a) | Casado(a) |
| Escolaridade | Técnico, Superior Incompleto/Completo, MBA/Pós, Mestrado | MBA/Pós-graduação |
| Cargo | 53 cargos distintos | Coach Executivo Sr |
| Departamento | 11 áreas | Academia de Liderança e Coaching |
| Nivel_Hierarquico | Diretoria, Gerência, Coordenação, Senior, Pleno, Junior, Estágio | Pleno |
| Tempo_Empresa_Anos | Tempo de casa | 6.7 |
| Salario_R$ | Salário mensal bruto em R$ | 21143 |
| Tipo_Contrato | CLT, CLT Flex, PJ, Estágio | CLT |
| Avaliacao_Desempenho_1a5 | Avaliação anual 1.0–5.0 | 4.7 |
| Horas_Treinamento_Ano | Capacitação recebida no ano | 80 |
| Engajamento_% | Pesquisa de clima 45–99% | 89 |
| Absenteismo_Dias_Ano | Faltas não programadas | 4 |
| Risco_Turnover | Baixo / Médio / Alto (regra: engajamento + performance) | Baixo |
| Potencial_Lideranca | Baixo / Médio / Alto | Médio |
| Ultima_Promocao_Ano | Ano da última promoção | 2025 |

---

## 3. Raio-X dos 200 Colaboradores — Estatísticas Reais da Base Gerada

Calculado via Python sobre o CSV (médias arredondadas):

| Indicador | Resultado |
|---|---|
| **Headcount** | 200 |
| **Idade média** | 33,8 anos |
| **Faixa etária** | 19–25: 29 (14,5%) · 26–32: 70 (35%) · 33–40: 61 (30,5%) · 41–50: 37 (18,5%) · 51+: 3 (1,5%) |
| **Sexo** | F: 124 (62%) · M: 76 (38%) |
| **Tempo médio de casa** | 3,4 anos |
| **Salário médio** | R$ 5.927,11 · **Mediana** R$ 5.043,50 · **Folha mensal** R$ 1.185.423 |
| **Avaliação média** | 4,01 / 5,0 |
| **Engajamento médio** | 77,7% |
| **Horas de treinamento/ano (média)** | 58,0 h (bem acima do mercado ~30h — coerente: empresa que vende treinamento treina muito) |
| **Absenteísmo médio** | 3,2 dias/ano |

### 3.1 Por nível hierárquico

| Nível | Qtd | % | Salário médio |
|---|---|---|---|
| Diretoria | 4 | 2% | R$ 20.560 |
| Gerência | 12 | 6% | R$ 13.536 |
| Coordenação | 20 | 10% | R$ 8.793 |
| Sênior / Especialista | 47 | 23,5% | R$ 7.099 |
| Pleno | 62 | 31% | R$ 4.677 |
| Júnior / Assistente | 45 | 22,5% | R$ 2.846 |
| Estágio | 10 | 5% | R$ 1.321 |

> Pirâmide saudável para empresa de conhecimento: 18% em cargos de gestão (36 pessoas) para 82% executores/especialistas.

### 3.2 Por departamento

| Departamento | Qtd | % | Salário médio |
|---|---|---|---|
| Facilitação e Instrutoria Corporativa | 34 | 17% | R$ 5.634 |
| Academia de Liderança e Coaching | 31 | 15,5% | R$ 5.926 |
| Design Instrucional e Conteúdo EAD | 30 | 15% | R$ 5.716 |
| Consultoria em Desenvolvimento de Equipes | 26 | 13% | R$ 5.396 |
| Comercial e Vendas B2B | 22 | 11% | R$ 5.641 |
| Psicologia Organizacional e Avaliação | 15 | 7,5% | R$ 6.082 |
| Marketing e Growth | 14 | 7% | R$ 4.647 |
| Operações e CX | 11 | 5,5% | R$ 4.456 |
| Administrativo-Financeiro | 8 | 4% | R$ 6.135 |
| TI e Plataforma EAD | 5 | 2,5% | R$ 7.520 |
| Diretoria | 4 | 2% | R$ 20.560 |

### 3.3 Escolaridade e contrato

- **Escolaridade:** Superior Completo 77 (38,5%) · MBA/Pós 72 (36%) · Superior Incompleto 30 (15%) · Mestrado 14 (7%) · Técnico 7 (3,5%). → 81,5% com ensino superior completo ou mais — perfil esperado para instrutores, psicólogos, designers e coaches.
- **Contrato:** CLT 151 (75,5%) · PJ 24 (12%) · CLT Flex 15 (7,5%) · Estágio 10 (5%). PJ concentrado em diretoria e instrutores Sr (flexibilidade de agenda).

### 3.4 Desempenho, engajamento e risco

- **Risco Turnover:** Baixo 110 (55%) · Médio 74 (37%) · Alto 16 (8%)
- **Potencial Liderança:** Médio 112 (56%) · Alto 44 (22%) · Baixo 44 (22%)

Leitura gerencial (matriz 9-box simplificada):
- ~44 talentos com **Alto potencial** = pipeline de sucessão para as 32 posições de coordenação/gerência.
- 16 colaboradores em **Alto risco** (engajamento <65% + avaliação <3,5) = prioridade para entrevista de retenção, PDI e revisão salarial. Custo estimado de reposição: 50–150% do salário anual por vaga técnica.

---

## 4. Perfil Profissional Típico por Área (persona)

1. **Coach Executivo Sr (Academia):** 30–45 anos, MBA/Pós ou Mestrado, salário R$ 6.500–8.500, 60–100h de capacitação/ano, certificação ICF/PCC simulada, avaliação ~4,3.
2. **Designer Instrucional Sr:** Superior + Pós em Educação, portfólio EAD, R$ 6.000–8.000, domínio Articulate/Captivate/LMS.
3. **Instrutor Corporativo Sr:** Carisma + didática, R$ 5.800–7.800, 80% do tempo em campo (cliente).
4. **Consultor de Desenvolvimento Sr:** Diagnóstico organizacional, people analytics, R$ 6.200–8.500.
5. **Psicólogo Organizacional:** CRP ativo, assessment DISC/MBTI/Birkman, R$ 6.000–8.000.
6. **Executivo de Contas B2B:** Hunter/Farmer, variável por comissão (não simulada aqui), R$ 3.500–7.500.
7. **TI EAD:** Full-stack + Moodle/Totara, menor time (5) mas maior salário médio (R$ 7.520) — gargalo de capacidade.

---

## 5. Alertas e Plano de Ação de RH (para discussão em sala)

1. **Retenção dos 16 Alto Risco:** rodar PDI de 90 dias + mentoria + checar salário vs mediana do nível.
2. **Sucessão:** mapear os 44 Alto Potencial para programa de formação de líderes internos (a empresa “vende” liderança — precisa praticar em casa).
3. **Capacitação:** média 58h/ano é ponto forte de employer branding — divulgar. Garantir mínimo de 40h para Pleno/Júnior com avaliação <3,7.
4. **Diversidade:** 62% mulheres — ponto positivo; auditar equidade salarial por nível (ex.: comparar médias F vs M dentro de cada nível).
5. **Absenteísmo:** média 3,2 dias é saudável (<4). Investigar outliers >10 dias.
6. **PJ (12%):** revisar risco trabalhista; manter PJ só para atuação eventual/projeto.

---

## 6. Como usar academicamente (ADM-2026-INFORMÁTICA)

- Abrir o CSV no Excel / Google Sheets / Power BI: Tabela Dinâmica por `Departamento x Nivel_Hierarquico` (contagem + média salarial).
- Exercícios sugeridos: 
  - Calcular turnover potencial (Alto+½ Médio ÷ 200)
  - Gráfico pirâmide etária e funil hierárquico
  - Correlação `Horas_Treinamento x Avaliação` (esperado: positiva fraca, por construção)
  - Folha por departamento e custo médio por hora de treinamento
- Reprodutibilidade: `python3 gerar_dados_rh.py` regenera os mesmos 200 registros (seed 42). Para variar, troque a seed.

> **Aviso metodológico:** todos os nomes, salários e avaliações são **sintéticos e fictícios**, gerados por distribuição aleatória calibrada por nível — não representam pessoas reais. Adequado para simulação, modelagem e aulas de planilha/BI, não para decisão real de pessoal.

---

*Gerado em 29/09/2026 — TALENTAR (fictícia) · 200 colaboradores · folha R$ 1,19M/mês · engajamento 77,7% · avaliação 4,01*
