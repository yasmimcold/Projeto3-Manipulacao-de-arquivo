🗂️ Projeto de Manipulação de Arquivos em Python
📘 Descrição

Este projeto tem como objetivo demonstrar o uso da manipulação de arquivos em Python, utilizando as funções open() e o bloco with para realizar o cadastro de pessoas em um arquivo de texto.

O sistema permite que o usuário registre informações como nome e idade, salvando-as de forma permanente em um arquivo .txt. Também é possível visualizar todos os cadastros realizados, garantindo a prática dos principais conceitos de entrada e saída de dados (I/O).

🎯 Objetivo

O foco deste projeto é ensinar de forma prática como trabalhar com arquivos em Python, aprendendo a:

Criar e abrir arquivos usando open()

Utilizar o bloco with para manipular arquivos com segurança

Gravar dados em um arquivo texto

Ler informações previamente armazenadas

Compreender a importância do fechamento automático de arquivos

⚙️ Funcionalidades

✅ Cadastro de pessoas (nome e idade)

✅ Armazenamento permanente dos dados em um arquivo .txt

✅ Visualização dos cadastros já realizados

✅ Tratamento de erros caso o arquivo ainda não exista

✅ Interface simples e totalmente interativa no terminal

🧱 Estrutura do Projeto
projeto_cadastro/
│
├── app.py              # Arquivo principal do sistema
├── cadastros.txt       # Arquivo onde os dados são armazenados
└── README.md           # Documentação do projeto

🧠 Conceitos Envolvidos
🔹 Função open()

A função open() é responsável por abrir arquivos em Python.
Ela pode ser utilizada em diferentes modos de acesso, como:

"r" → leitura

"w" → escrita (sobrescreve o arquivo)

"a" → append (adiciona novas linhas sem apagar o conteúdo anterior)

🔹 Estrutura with

A estrutura with garante que o arquivo seja aberto e fechado automaticamente, mesmo que aconteça algum erro durante a execução.
Essa é a forma mais segura e recomendada de manipular arquivos em Python.

📂 Exemplo de Saída (Arquivo Gerado)

O arquivo cadastros.txt conterá as informações cadastradas, seguindo um formato simples e legível, por exemplo:

Nome: João, Idade: 25
Nome: Maria, Idade: 30
Nome: Pedro, Idade: 18

🏁 Conclusão

Este projeto serve como uma excelente introdução ao tema de manipulação de arquivos em Python, mostrando como armazenar e recuperar informações de forma prática.
Com ele, o aluno aprende na prática os fundamentos de persistência de dados usando apenas recursos nativos da linguagem.

✍️ Autor
🧠 Linguagem: Python
