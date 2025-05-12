
# UML Diagram Development Assistant

A conversational assistant that leverages Large Language Models (LLMs) to support Object-Oriented Analysis and Design (OOAD) through interactive UML diagram generation, visualization, and iterative refinement.

---

## 🧠 Project Overview

The **UML Diagram Development Assistant** bridges the gap between **natural language requirements** and **formal UML modeling**. It harnesses the capabilities of Large Language Models (e.g., GPT-4, GLM-4) and integrates **PlantUML** rendering, offering users a hands-on environment to:

- Generate UML class diagrams from textual descriptions
- Refine diagrams interactively through conversation
- Explore multiple diagram projections (e.g., inheritance, aggregation)
- Edit PlantUML code and preview changes instantly

This project was developed as part of **CPS 3962: Object-Oriented Analysis and Design** at **Kean University**, under the mentorship of **Dr. Hamza Djigal**.

---

## 🎯 Objectives

- 📐 Generate UML diagrams from user-defined scenario descriptions via natural language
- 🧑‍💻 Provide an interactive, iterative, and conversational design experience
- 🎞️ Render and visualize UML diagrams in real-time using PlantUML
- ✅ Ensure model validity through adherence to OOAD principles such as encapsulation, inheritance, and modularity
- 🚀 Lower the entry barrier for model-driven development in AI, Cloud, and Big Data environments

---

## ✨ Key Features

- **Conversational AI Interface**: Natural language chat-based interaction to design UML diagrams
- **Multi-Model Support**: Choose among OpenAI, Replicate, BigModel (GLM-4), Ollama, and more
- **Real-time Rendering**: Convert PlantUML code into visual diagrams with instant feedback
- **Projections and Perspectives**: View diagrams from different analytical lenses (e.g., structure, association, composition)
- **Code & Diagram Sync**: Edit PlantUML code in real-time with live preview
- **Session History**: Auto-log conversation context and diagrams for revision and continuation

---

## 🧱 System Architecture

### 1. LLM Inference Pipeline
- **Data Preparation**: Annotated scenario descriptions + UML mappings
- **Fine-Tuning** (optional): Extend base LLMs (e.g., BART, GPT) for PlantUML generation
- **Inference Equation**:

  \[
  P(t_i \mid t_{<i}) = \text{LLM}(t_1, t_2, \dots, t_{i-1})
  \]

- **API Integration**: FastAPI-based RESTful backend connecting front-end with inference engine

### 2. Frontend Architecture
- Developed using **ReactJS**
- Chatbox UI with:
  - Scenario input
  - Diagram rendering panel
  - PlantUML code editor
  - Model configuration sidebar

### 3. Backend Components
- **UMLDiagramGenerationApp**: Coordinates user interactions and rendering pipeline
- **LanguageModelApiClient**: Manages inference calls across different LLM providers
- **DiagramInterpreter**: Converts descriptions into diagrams using PlantUML
- **ProjectionManager**: Filters UML views by inheritance, association, etc.
- **ConversationDataStorage**: Logs and retrieves session data

---

## 🔧 Installation Guide

### 📌 Prerequisites

- Python 3.8+
- `pip` package manager
- Internet access for model inference APIs

### 🛠️ Setup Instructions

```bash
# 1. Clone repository
git clone https://github.com/yourusername/UML-Diagram-Development-Assistant.git
cd UML-Diagram-Development-Assistant

# 2. (Optional) Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate     # Windows

# 3. Install core dependencies
pip install streamlit requests

# 4. Optional: Add support for specific LLM APIs
pip install openai replicate llama-cpp-python plantweb

# 5. Run application
streamlit run UML_Diagram_development_Assistant_V0.9.py
````

### 🌐 Access Interface

Open your browser and navigate to:

```
http://localhost:8501
```

---

## 🧭 Application Workflow

### Step 1: Start a Conversation

* Select a language model from the sidebar
* Enter a natural language description (e.g., "A university has students and professors...")

### Step 2: Diagram Generation

* The assistant interprets your input
* PlantUML code is generated and visualized

### Step 3: Iterative Refinement

* Update the scenario or diagram through conversation
* Use projection filters to focus on inheritance, composition, etc.

### Step 4: Editing and Customization

* Modify PlantUML code directly in the editor
* Preview changes in real-time

### Step 5: Session Management

* Your diagrams and conversations are auto-logged
* Resume from previous sessions at any time

---

## 🧩 Technologies Used

| Layer         | Technologies                          |
| ------------- | ------------------------------------- |
| **Frontend**  | ReactJS, Streamlit                    |
| **Backend**   | FastAPI, Python                       |
| **LLMs**      | GPT-4, GLM-4, Replicate, Ollama |
| **Rendering** | PlantUML, Graphviz                    |
| **Packaging** | pip, virtualenv                       |


---

## 🧑‍🤝‍🧑 Contributors

* **Zhentong Ye** ([zye@kean.edu](mailto:zye@kean.edu))
* **Yanwu Lang** ([langy@kean.edu](mailto:langy@kean.edu))

---

## 🔗 Additional Resources

* 📘 [PlantUML Class Diagram Docs](https://plantuml.com/class-diagram)
* 🧭 [UML Class Diagram Tutorial](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/)
* 📙 [OOAD Principles Overview](https://www.oodesign.com/)
* 🧪 [BART\_PlantUML Paper](https://arxiv.org/abs/2106.11037)

---

## 📌 Acknowledgements

> *This assistant was built for educational purposes as part of CPS 3962 at Kean University. We gratefully acknowledge the guidance of Dr. Hamza Djigal and the support from the School of Computer Science.*


