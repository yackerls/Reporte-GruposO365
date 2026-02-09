FROM python:3.11-slim
WORKDIR /app
# Instalamos las librerías necesarias
RUN pip install pandas streamlit
COPY . .
EXPOSE 8501
# Ejecutamos con streamlit, no con python directamente
CMD ["streamlit", "run", "script.py", "--server.address=0.0.0.0"]