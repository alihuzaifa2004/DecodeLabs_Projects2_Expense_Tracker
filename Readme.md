# Project 2: The Expense Tracker (Data Processing Engine)

## 📌 Overview
Welcome to **Project 2: The Expense Tracker**, the core Logic Processing Phase completed as part of the DecodeLabs Industrial Training framework.

While Project 1 established layout mechanics for collection arrays (To-Do list tracking), this milestone establishes the foundations of mathematical **Data Accumulation, Type Transformation, and Fault-Tolerant System Environments**. This engine tests a developer's mastery over handling unbounded incoming numeric fields safely using state preservation across runtime triggers.

---

## ⚙️ Core Architectural Pillars

[ Raw Text Input Stream ]
│
▼
┌───────────────────────────────────┐
│     PHASE 1: THE GATEKEEPER       │  --> Catches letters ("ten") & throws
│   (Defensive Poka-Yoke Shield)    │      safe validation warnings.
└───────────────────────────────────┘
│
▼ [ Valid Float Parsed ]
┌───────────────────────────────────┐
│   ACCUMULATOR MODIFIER ENGINE     │  --> Safely runs math logic:
│    total = total + new_expense    │      total_spent += current_input
└───────────────────────────────────┘


### 1. Mathematical Accumulation Principle
Unlike arrays that grow index sizing on the heap, an accumulator utilizes persistent static primitives to sum elements instantly. It forms the algorithmic basis for metric analysis systems, logging loops, and pipeline analytical calculation blocks.

### 2. Type Transformation & Safety
Incoming text items received by programs capture information strictly via string arrays. Processing raw text directly can cause unexpected program crashes or visual arithmetic anomalies (such as string concat bugs where `'100' + '50' = '10050'`). This tracker establishes type control, safely modifying incoming data points before computing equations.

### 3. Defensive Error Proofing (Digital Poka-Yoke)
By implementing targeted `try...except ValueError` guard barriers, the computational processing thread isolates type formatting exceptions safely. It prevents unexpected values from causing unexpected engine crashes, sustaining structural availability.

---

## 🚀 Technical Requirements & Launch Instructions

### Setup & Requirements
* Environment target: Python 3.8+
* Web framework layer: Streamlit

### Run CLI Script Core
```bash
python main_cli.py
Run Web Application Interface Dashboard
Bash
pip install streamlit
streamlit run app.py