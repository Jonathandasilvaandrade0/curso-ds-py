# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Sustent%C3%A1vel-yellow?style=for-the-badge&logo=lightning)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

---

## 📌 Sobre o Projeto

A **Calculadora de Consumo Elétrico Inteligente** é um sistema desenvolvido em **Python** com o objetivo de ajudar os usuários a estimarem o consumo mensal de energia elétrica (em kWh) e o custo financeiro aproximado de aparelhos eletrodomésticos a partir de dados simples de uso diário. 

O projeto visa conscientizar sobre o consumo de energia e auxiliar no planejamento financeiro residencial.

---

## 🧮 Fórmula Utilizada

O cálculo do consumo elétrico mensal é realizado através da seguinte equação:

$$\text{consumoMensal} = \frac{\text{potência (W)} \times \text{horas de uso/dia} \times 30}{1000}$$

> **💡 Dica de Custo:** Para calcular o valor financeiro estimado (em R$), o sistema multiplica o consumo mensal em kWh por uma tarifa fixa aproximada de **R$ 0,75 por kWh**.

---

## 🚀 Como Executar o Programa

### Pré-requisitos
* Ter o **Python 3.x** instalado no computador.
* Ter o **Git** instalado (opcional, para clonar o repositório).

### Passo a Passo

1. **Acesse a pasta do projeto** pelo seu terminal ou prompt de comando:
   ```bash
   cd projetos/consumo-energia
   ```

2. **Execute o arquivo principal em Python**:
   ```bash
   python app.py
   ```

3. **Siga as instruções na tela**:
   * Digite o nome do aparelho (ex.: `Geladeira`).
   * Digite a potência em Watts (ex.: `150`).
   * Digite as horas diárias de uso (ex.: `24`).
   * Escolha se deseja realizar novos cálculos ao finalizar.

---

## 💻 Exemplo de Uso

```text
========================================
   CALCULADORA DE CONSUMO ELÉTRICO   
========================================

Digite o nome do aparelho (ex.: Geladeira): Geladeira
Digite a potência do aparelho em Watts (W): 150
Digite o tempo médio de uso diário em horas: 24

----------------------------------------
Aparelho: Geladeira
Consumo estimado: 108.00 kWh/mês
Custo estimado: R$ 81.00/mês
----------------------------------------

Deseja calcular outro aparelho? (s/n): n

Obrigado por utilizar a calculadora! Encerrando o programa...
```

---

## 🛠️ Tecnologias e Ferramentas

* 🐍 **Python 3**: Linguagem de programação responsável pela lógica do sistema.
* 🐙 **GitHub**: Plataforma utilizada para versionamento e publicação do código.
* 💻 **VS Code**: Editor de código utilizado no desenvolvimento.

---

Desenvolvido como atividade prática de iniciação em tecnologia. ⚡