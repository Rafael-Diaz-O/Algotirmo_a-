import numpy as np

# Definición de los estados del clima
states = ["Soleado", "Nublado", "Lluvioso"]

# Matriz de transición de estados
# Las probabilidades en cada fila suman 1
transition_matrix = [
    [0.8, 0.15, 0.05],  # Transiciones a partir de "Soleado"
    [0.2, 0.6, 0.2],    # Transiciones a partir de "Nublado"
    [0.25, 0.25, 0.5]   # Transiciones a partir de "Lluvioso"

]

# Estado inicial
initial_state = "Soleado"

# Número de días a prever
num_days = 10

# Función para encontrar el índice de un estado
def get_state_index(state):
    return states.index(state)

# Función para predecir el clima para los próximos días
def predict_weather(initial_state, num_days):
    current_state = initial_state
    forecast = [current_state]

    for _ in range(num_days - 1):
        current_index = get_state_index(current_state)
        next_state = np.random.choice(
            states, 
            p=transition_matrix[current_index]
        )
        forecast.append(next_state)
        current_state = next_state

    return forecast

# Realizar la predicción
forecast = predict_weather(initial_state, num_days)

# Mostrar la predicción
print(f"Estado inicial: {initial_state}")
print("Predicción para los próximos días:")
for day, state in enumerate(forecast, start=1):
    print(f"Día {day}: {state}")