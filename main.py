import streamlit as st

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

def administrar_encuesta():
    preguntas = [
        "¿Con qué frecuencia repites los mismos errores?",
        "¿Cambias tu opinión cuando te presentan pruebas sólidas?",
        "¿Consideras los sentimientos y necesidades de los demás antes de actuar?",
        "¿Tomas decisiones impulsivas sin pensar en las consecuencias?",
        "¿Te interesa aprender y mejorar tus conocimientos?",
        "¿Aceptas la responsabilidad de tus errores?",
        "¿Buscas soluciones a los problemas cotidianos?",
        "¿Cómo reaccionas cuando tus acciones tienen consecuencias negativas?",
        "¿Confías en supersticiones o teorías sin fundamento en lugar de en datos y evidencia?",
        "¿Te resulta difícil encontrar soluciones a problemas simples?"
    ]
    
    opciones = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    respuestas = []

    for pregunta in preguntas:
        respuesta = st.radio(pregunta, options=['A', 'B', 'C', 'D'], format_func=lambda x: opciones[x])
        respuestas.append(opciones[respuesta])

    return respuestas

def main():
    st.title("Encuesta sobre Comportamientos y Decisiones")
    st.write("Completa la encuesta respondiendo a cada pregunta. Selecciona la opción que mejor se ajuste a tu comportamiento.")
    
    respuestas = administrar_encuesta()
    resultado = evaluar_comportamiento(respuestas)

    st.write("\n**Resultados de la encuesta:**")
    st.write(f"Puntuación total: {sum(respuestas)}")
    st.write(f"Evaluación: {resultado}")

if __name__ == "__main__":
    main()
