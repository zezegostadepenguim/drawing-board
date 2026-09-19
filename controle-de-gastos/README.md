# Controle de Gastos Pessoais

App de controle de gastos em **um único arquivo** (`index.html`), com HTML, CSS e
JavaScript puros — sem frameworks, sem build, sem dependências e sem servidor.
Todos os dados ficam no `localStorage` do próprio navegador.

## Funcionalidades

- Adicionar gasto com **valor**, **descrição**, **categoria** e **data**
- Listar os gastos **ordenados por data** (mais recentes primeiro), agrupados por dia
- Mostrar o **total do mês** selecionado (ou de todos os períodos)
- **Excluir** um gasto, com confirmação
- Persistência automática em `localStorage`
- Layout responsivo, pensado primeiro para celular
- Tema claro/escuro automático, conforme a preferência do sistema

## Como rodar

### Opção 1 — abrir o arquivo (mais simples)

Dê um duplo clique em `index.html`, ou arraste o arquivo para a janela do navegador.
Funciona direto via `file://`, sem instalar nada.

### Opção 2 — servidor local (recomendado para testar no celular)

Na pasta `controle-de-gastos/`, rode um dos comandos abaixo e acesse o endereço
mostrado no terminal:

```bash
python3 -m http.server 8000     # http://localhost:8000
# ou
npx serve .
```

Para abrir no celular, use o IP da máquina na mesma rede Wi-Fi
(ex.: `http://192.168.0.10:8000`).

### Opção 3 — publicar

Como é um arquivo estático, qualquer hospedagem serve: GitHub Pages, Netlify,
Vercel, Cloudflare Pages. Basta subir o `index.html`.

## Onde ficam os dados

Tudo é gravado na chave `controle-gastos:v1` do `localStorage`, no formato:

```json
[
  {
    "id": "b3f1…",
    "descricao": "Almoço no centro",
    "centavos": 3290,
    "data": "2026-09-05",
    "categoria": "Alimentação",
    "criadoEm": 1757030400000
  }
]
```

Consequências práticas:

- Os dados **não saem do dispositivo** e não são enviados a lugar nenhum.
- Cada navegador (e cada perfil) tem sua própria lista — não há sincronização.
- Limpar os dados do site, ou usar uma janela anônima, apaga o histórico.

### Backup manual

No console do navegador (F12):

```js
// exportar
copy(localStorage.getItem('controle-gastos:v1'))

// importar
localStorage.setItem('controle-gastos:v1', '<conteúdo colado aqui>')
```

## Compatibilidade

Navegadores atuais de desktop e celular (Chrome, Safari, Firefox, Edge).
Usa `Intl.NumberFormat`, `<input type="date">`, `Element.closest()` e
`crypto.randomUUID()` (com alternativa própria quando indisponível).

## Estrutura do código

Dentro do `index.html`, o JavaScript roda em uma IIFE (nada é exposto no escopo
global) e está dividido em blocos comentados:

| Bloco | Responsabilidade |
| --- | --- |
| Persistência | ler, validar e gravar no `localStorage` |
| Utilidades | parse de valores, datas e rótulos em pt-BR |
| Render | filtro de mês, resumo e lista |
| Validação | checagem dos campos do formulário |
| Inicialização | categorias, estado inicial e listeners |
