# 📘 Tutorial Básico de Markdown para Iniciantes

> **Para quem nunca programou e quer aprender do zero!**
> Markdown é uma forma simples de formatar textos. Você escreve de um jeito fácil e ele vira um texto bonito.

---

## 🤔 1. O que é Markdown?

Pense assim:

| Você escreve isso... | ...e aparece isso |
|---|---|
| `**negrito**` | **negrito** |
| `# Título grande` | Título bem grande |
| `- item da lista` | • item da lista |

**Onde você já usa sem saber?**
- ✅ WhatsApp (`*negrito*`, `_itálico_`)
- ✅ README do GitHub
- ✅ Documentos no Notion, Discord, Trello

> 💡 **Ideia principal:** você não precisa apertar botões. Você escreve símbolos simples e o texto se formata sozinho.

---

## ✍️ 2. Títulos e Subtítulos

Use o símbolo `#` (jogo da velha). Quanto mais `#`, menor o título.

```markdown
# Título principal - bem grande
## Subtítulo - grande
### Seção menor
#### Detalhe pequeno
```

**Vai ficar assim:**

# Título principal - bem grande
## Subtítulo - grande
### Seção menor
#### Detalhe pequeno

> 📌 **Regra de ouro:** deixe sempre um espaço depois do `#`.
> ✅ `# Meu título` (certo)
> ❌ `#Meu título` (errado)

---

## ✨ 3. Negrito, Itálico e Riscado

```markdown
**Isso fica em negrito**
*Isso fica em itálico*
~~Isso fica riscado~~
***Isso fica em negrito e itálico***
```

**Resultado:**

**Isso fica em negrito**
*Isso fica em itálico*
~~Isso fica riscado~~
***Isso fica em negrito e itálico***

> 💡 **Dica de vizinho:**
> - Negrito = `**texto**` (2 asteriscos de cada lado)
> - Itálico = `*texto*` (1 asterisco de cada lado)

---

## 📝 4. Listas

### Lista com bolinhas (não ordenada)

```markdown
- Café
- Leite
- Pão
```

- Café
- Leite
- Pão

> Você pode usar `-` ou `*` ou `+`. O `-` é o mais comum.

### Lista numerada (ordenada)

```markdown
1. Acordar
2. Escovar os dentes
3. Tomar café
```

1. Acordar
2. Escovar os dentes
3. Tomar café

### Lista dentro de lista (sublista)

Basta dar **2 espaços** antes do `-`:

```markdown
- Compras do mercado
  - Frutas
  - Verduras
- Farmácia
```

- Compras do mercado
  - Frutas
  - Verduras
- Farmácia

---

## ✅ 5. Lista de Tarefas (Checklist)

Muito usada para organizar tarefas:

```markdown
- [ ] Estudar Markdown
- [ ] Fazer exercício
- [x] Tomar café (pronto!)
```

- [ ] Estudar Markdown
- [ ] Fazer exercício
- [x] Tomar café (pronto!)

> `[ ]` = vazio, `[x]` = marcado com X

---

## 🔗 6. Links e Imagens

### Link (texto clicável)

```markdown
[Clique aqui para abrir o Google](https://www.google.com)
```

[Clique aqui para abrir o Google](https://www.google.com)

> 🧠 **Macete para lembrar:**
> `[texto que aparece](endereço do link)`
>
> Pense: `[o que eu vejo](para onde vai)`

### Imagem

É quase igual ao link, só coloca um `!` na frente:

```markdown
![Descrição da foto](https://exemplo.com/foto.jpg)
```

> Exemplo real:
> `![Gatinho fofo](https://placekitten.com/300/200)`

---

## 💬 7. Citação

Use `>` para destacar uma frase, como uma fala de alguém:

```markdown
> A persistência é o caminho do êxito.
```

> A persistência é o caminho do êxito.

---

## ➖ 8. Linha de Separação

Para dividir o texto, digite três traços `---` em uma linha sozinha:

```markdown
Texto de cima

---

Texto de baixo
```

Texto de cima

---

Texto de baixo

---

## 💻 9. Código

### Uma palavra de código no meio da frase

Use uma crase `` ` `` (aquele acento virado para trás, fica do lado da tecla P no teclado brasileiro):

```markdown
Para salvar, aperte `Ctrl + S`.
```

Para salvar, aperte `Ctrl + S`.

### Bloco de código maior

Use três crases em cima e embaixo:

````markdown
```
Olá, mundo!
Esse é um bloco de código.
```
````

```
Olá, mundo!
Esse é um bloco de código.
```

---

## 📊 10. Tabelas Simples

Parece difícil, mas é só desenhar com `|` e `-`:

```markdown
| Nome  | Idade | Cidade       |
|-------|-------|--------------|
| Ana   | 20    | São Paulo    |
| Bruno | 25    | Rio de Janeiro |
```

| Nome  | Idade | Cidade       |
|-------|-------|--------------|
| Ana   | 20    | São Paulo    |
| Bruno | 25    | Rio de Janeiro |

> 🧠 **Como entender:**
> - `|` separa as colunas (parede)
> - Segunda linha `|---|---|` diz "aqui começa a tabela"
> - Cada linha nova = uma linha da tabela

---

## 🎨 11. Extras Legais

### Emoji

É só copiar e colar! 🎉 🚀 ❤️ 👍

```markdown
Parabéns! 🎉 Você terminou! 🚀
```

Parabéns! 🎉 Você terminou! 🚀

### Destaque colorido (aviso)

Alguns sites aceitam isso:

```markdown
> [!NOTE]
> Isso é uma informação importante.

> [!WARNING]
> Cuidado com isso aqui!
```

> [!NOTE]
> Isso é uma informação importante.

---

## 🏋️ 12. Mini Exercício Prático

Tente criar um arquivo `meu-perfil.md` com isso:

```markdown
# Meu nome é [Seu Nome]

## Sobre mim
Sou estudante e estou aprendendo **Markdown**.

## Meus hobbies
- [ ] Ler
- [ ] Jogar
- [x] Aprender coisas novas

## Minha frase favorita
> Nunca desista!

## Meu site favorito
[Clique aqui](https://www.google.com)

---
Feito com ❤️ por mim!
```

---

## 🗺️ 13. Cola Rápida - Resumo Visual

| Quero fazer... | Escrevo assim... |
|---|---|
| Título grande | `# Título` |
| Subtítulo | `## Subtítulo` |
| **Negrito** | `**texto**` |
| *Itálico* | `*texto*` |
| ~~Riscado~~ | `~~texto~~` |
| Lista com bolinha | `- item` |
| Lista numerada | `1. item` |
| Tarefa a fazer | `- [ ] tarefa` |
| Link | `[texto](link)` |
| Imagem | `![texto](link-da-imagem)` |
| Citação | `> frase` |
| Linha divisória | `---` |
| Código curto | `` `código` `` |

---

## 🚀 Próximos Passos

1. Abra o **Bloco de Notas** ou **VS Code**
2. Salve um arquivo terminando com `.md` (exemplo: `teste.md`)
3. Copie os exemplos deste tutorial e veja o resultado
4. Dica: cole seu `.md` neste site para ver bonito na hora: **https://dillinger.io**

> 🎉 **Parabéns!** Se você chegou até aqui, você já sabe 90% do Markdown que vai usar no dia a dia. O resto se aprende praticando!

---
*Tutorial criado para iniciantes em Informática - ADM 2026* 💙
