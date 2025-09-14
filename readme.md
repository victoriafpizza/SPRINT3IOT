# 👁️ Detector de Rostos com OpenCV (Haar Cascade)

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

<p align="center">
  📸 Um sistema em Python que detecta rostos em tempo real (ou em vídeo) utilizando o algoritmo Haar Cascade do OpenCV.
</p>

---

## 👥 Desenvolvedores
- **Victoria Franceschini Pizza** – RM 550609  
- **Eric de Carvalho Rodrigues** – RM 550249  

---

<p align="center">
<img src="https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white" /> 
<img src="https://img.shields.io/badge/-OpenCV-5C3EE8?logo=opencv&logoColor=white" /> 
<img src="https://img.shields.io/badge/-MediaPipe-FF6F00?logo=google&logoColor=white" />
<img src="https://img.shields.io/badge/-Feito%20com%20cafe-6f4e37?logo=buymeacoffee&logoColor=white" />
</p>

---

## 🧠 Sobre o Projeto
Este projeto implementa um **detector de rostos em vídeo** usando a biblioteca **OpenCV** e o classificador **Haar Cascade**.  

Ele é capaz de identificar rostos em tempo real (via webcam) ou em arquivos de vídeo (`.mp4`), desenhando um **retângulo vermelho** ao redor da face detectada e exibindo a mensagem **"Rosto Detectado"** acima.

---

## 🚀 Tecnologias Utilizadas
- 🐍 **Python 3.10+**
- 🎥 **OpenCV**
- 🧩 **Haar Cascade Classifier**

---

## 🔍 Como Funciona
1. O algoritmo Haar Cascade é carregado a partir do arquivo `haarcascade_frontalface_default.xml`.  
2. A imagem é convertida para tons de cinza, melhorando a performance da detecção.  
3. O detector percorre o frame e identifica regiões que se parecem com rostos.  
4. Para cada rosto encontrado:
   - Um **retângulo vermelho** é desenhado ao redor.  
   - O texto **“Rosto Detectado”** aparece acima.  

✅ O sistema funciona em tempo real ou com vídeos gravados.  
✅ Encerramento com a tecla `q`.  

---

## 🎯 Funcionalidades
- ✅ Detecção de rostos em tempo real (webcam).  
- ✅ Suporte a arquivos de vídeo (`video.mp4`).  
- ✅ Indicação visual clara com retângulo e texto.  
- ✅ Código simples e fácil de executar.  

---

## 📹 Demonstração
[![Vídeo de Demonstração](https://img.shields.io/badge/🔗-Assista%20ao%20Vídeo-blue?style=for-the-badge)](LINK_DO_VIDEO_AQUI)

---

## ⚙️ Como Rodar o Projeto

### 1️⃣ Clone este repositório
```bash
git clone https://github.com/victoriafpizza/GSPhysicalComputing.git
cd GSPhysicalComputing
```
### 2️⃣ Instale as dependências
pip install opencv-python

### 3️⃣ Baixe o classificador Haar Cascade

Certifique-se de ter o arquivo:
👉 haarcascade_frontalface_default.xml

Ele pode ser baixado do repositório oficial do OpenCV:
Download XML

### 4️⃣ Execute o programa
python detector_face.py

