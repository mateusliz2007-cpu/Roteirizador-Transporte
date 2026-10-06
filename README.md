# 🚚 Roteirizador de Transporte

> Projeto em Python aplicado à **roteirização e análise de operações de transporte**.

---

## 📌 Sobre o projeto

O **Roteirizador de Transporte** é um projeto desenvolvido em Python para simular um problema básico de roteirização.

O programa recebe uma **matriz de distâncias** entre um depósito e diferentes clientes. Depois, o usuário informa diferentes sequências de atendimento.

O sistema calcula a **distância total de cada rota**, considerando o retorno ao depósito, e identifica a rota de menor distância.

---

## ⚙️ Funcionalidades

* 📍 Definição da quantidade de clientes e rotas
* 📊 Cadastro de uma matriz de distâncias
* 🔢 Definição da sequência de clientes visitados
* 📏 Cálculo da distância total de cada rota
* 🔄 Retorno ao depósito
* ⚖️ Comparação entre diferentes rotas
* 🏆 Identificação da rota de menor distância

---

## 🐍 Conceitos de Python utilizados

* `input()`
* Conversão de tipos com `int()` e `float()`
* Listas
* Listas dentro de listas (matrizes)
* `for` e `range()`
* `append()`
* Variáveis acumuladoras
* `min()`
* `index()`

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/mateusliz2007-cpu/Roteirizador-Transporte.git
```

### 2. Entre na pasta

```bash
cd Roteirizador-Transporte
```

### 3. Execute o programa

```bash
python main.py
```

---

## 🧭 Exemplo de rota

Uma rota pode ser representada da seguinte forma:

```text
0 → 3 → 2 → 1 → 0
```

Onde:

* `0` = depósito
* `1`, `2` e `3` = clientes
* o último `0` = retorno ao depósito

---

## 🎯 Objetivo do projeto

Este projeto faz parte do meu aprendizado em **Python** e da construção de um portfólio voltado para:

* 🚛 Engenharia de Transportes e Logística
* 📊 Análise de dados
* 💻 Programação
* 🧠 Otimização

A ideia é evoluir gradualmente o projeto para problemas de roteirização mais próximos de aplicações reais.

---

## 🚀 Próximos passos

Possíveis evoluções do projeto:

* Restrições de capacidade
* Restrições de distância
* Mais tipos de veículos
* Algoritmos de otimização
* Visualização das rotas
* Aplicação de técnicas de Pesquisa Operacional
