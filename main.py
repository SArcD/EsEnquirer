import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Función para evaluar el comportamiento
def evaluar_comportamiento(respuestas):
    puntuacion_total = sum(respuestas)
    if puntuacion_total <= 8:
        return "Buen juicio y toma de decisiones."
    elif puntuacion_total <= 16:
        return "Promedio, algunas áreas de mejora."
    elif puntuacion_total <= 24:
        return "Deficiencias significativas en el juicio y la toma de decisiones."
    else:
        return "Fuerte tendencia a comportamientos de juicio deficiente."

# Función para generar consejos basados en las respuestas
def generar_consejos(respuestas):
    conceptos = [
        "Revisión y planificación",
        "Evaluación crítica de información",
        "Consideración de sentimientos ajenos",
        "Impulsividad en la toma de decisiones",
        "Interés en el aprendizaje y mejora",
        "Aceptación de responsabilidad",
        "Búsqueda de soluciones",
        "Manejo de consecuencias negativas",
        "Confianza en datos y evidencia",
        "Solución de problemas simples"
    ]
    
    consejos = [
        "Intenta revisar tus listas y planificación antes de salir de casa.",
        "Es importante evaluar críticamente la información y pedir pruebas cuando sea necesario.",
        "Siempre es bueno considerar los sentimientos y necesidades de los demás en tus decisiones.",
        "Trata de pensar en las consecuencias antes de tomar decisiones impulsivas.",
        "Mantén un interés constante en aprender y mejorar tus habilidades.",
        "Aceptar la responsabilidad de tus errores es crucial para el crecimiento personal.",
        "Buscar soluciones rápidas y efectivas a los problemas cotidianos es una habilidad valiosa.",
        "Aprender de las consecuencias negativas y ajustar tu comportamiento es importante.",
        "Confía en datos y evidencia en lugar de supersticiones o teorías infundadas.",
        "Desarrolla habilidades para resolver problemas simples de manera eficiente."
    ]
    
    recomendaciones = []
    for i, respuesta in enumerate(respuestas):
        if respuesta > 1:  # Asumimos que respuestas C (2) y D (3) indican áreas de mejora
            recomendaciones.append(f"**{conceptos[i]}**: {consejos[i]}")
    
    return recomendaciones

# Función para crear un gráfico de radar
def crear_grafico_radar(respuestas, categorias):
    N = len(categorias)
    
    # What will be the angle of each axis in the plot? (we divide the plot / number of variables)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    
    # The plot is a circle, so we need to "complete the loop" and append the start value to the end.
    respuestas += respuestas[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, respuestas, color='red', alpha=0.25)
    ax.plot(angles, respuestas, color='red', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categorias)
    
    return fig

# Función para administrar la encuesta
def administrar_encuesta():
    st.title("Cuestionario de Evaluación de Comportamiento")

    situaciones = [
        "Olvidaste comprar algo importante para la cena. ¿Cómo sueles manejar este tipo de situaciones?\nA) Siempre reviso la lista antes de salir.\nB) A menudo reviso, pero a veces olvido.\nC) Raramente reviso la lista.\nD) Nunca hago una lista.",
        "Un amigo te cuenta algo sorprendente pero no tiene pruebas. ¿Qué haces?\nA) Siempre pido pruebas antes de creerlo.\nB) A menudo creo, pero busco pruebas más tarde.\nC) Raramente pido pruebas.\nD) Nunca pido pruebas y siempre creo.",
        "Tu pareja te pide que consideres sus sentimientos en una decisión importante. ¿Qué haces?\nA) Siempre considero sus sentimientos.\nB) A menudo los considero.\nC) Raramente los considero.\nD) Nunca los considero.",
        "Ves un objeto interesante en una tienda y decides comprarlo sin pensarlo. ¿Qué tan frecuente es esto para ti?\nA) Nunca lo hago.\nB) Raramente lo hago.\nC) A menudo lo hago.\nD) Siempre lo hago.",
        "Te ofrecen un curso gratuito para mejorar tus habilidades. ¿Cuál es tu reacción?\nA) Siempre acepto y asisto.\nB) A menudo acepto.\nC) Raramente acepto.\nD) Nunca acepto.",
        "Cometes un error en el trabajo. ¿Cómo reaccionas?\nA) Siempre acepto la responsabilidad.\nB) A menudo acepto la responsabilidad.\nC) Raramente acepto la responsabilidad.\nD) Nunca acepto la responsabilidad.",
        "Se presenta un problema en casa, como una fuga de agua. ¿Cómo lo enfrentas?\nA) Siempre busco una solución inmediatamente.\nB) A menudo busco una solución.\nC) Raramente busco una solución.\nD) Nunca busco una solución.",
        "Tus acciones causan un conflicto con un amigo. ¿Cómo manejas la situación?\nA) Siempre aprendo y cambio mi comportamiento.\nB) A menudo me siento mal pero no cambio.\nC) Raramente culpo a otros o a las circunstancias.\nD) Nunca me importa.",
        "Te cuentan una superstición en una conversación casual. ¿Cuál es tu reacción?\nA) Nunca creo en supersticiones.\nB) Raramente creo en supersticiones.\nC) A menudo creo en supersticiones.\nD) Siempre creo en supersticiones.",
        "Tienes que resolver un problema sencillo en casa, como una bombilla fundida. ¿Cómo lo manejas?\nA) Nunca me resulta difícil.\nB) Raramente me resulta difícil.\nC) A menudo me resulta difícil.\nD) Siempre me resulta difícil."
    ]

    conceptos = [
        "Revisión y planificación",
        "Evaluación crítica de información",
        "Consideración de sentimientos ajenos",
        "Impulsividad en la toma de decisiones",
        "Interés en el aprendizaje y mejora",
        "Aceptación de responsabilidad",
        "Búsqueda de soluciones",
        "Manejo de consecuencias negativas",
        "Confianza en datos y evidencia",
        "Solución de problemas simples"
    ]

    opciones = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    respuestas = []

    for i, situacion in enumerate(situaciones):
        st.write(f"Situación {i+1}: {situacion}")
        respuesta = st.selectbox("Selecciona una opción:", ['A', 'B', 'C', 'D'], key=i)
        respuestas.append(opciones[respuesta])

    if st.button("Enviar respuestas"):
        resultado = evaluar_comportamiento(respuestas)
        puntuacion_total = sum(respuestas)
        st.write(f"Puntuación total: {puntuacion_total}")
        st.write(f"Evaluación: {resultado}")

        st.write("### Conceptos Clave y Consejos:")
        recomendaciones = generar_consejos(respuestas)
        for recomendacion in recomendaciones:
            st.write(recomendacion)
        
        st.write("### Gráfico de Radar de tus Respuestas:")
        fig = crear_grafico_radar(respuestas, conceptos)
        st.pyplot(fig)

# Ejecutar la encuesta en Streamlit
administrar_encuesta()
