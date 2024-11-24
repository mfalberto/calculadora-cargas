import streamlit as st
import pandas as pd

# Carregando dados de materiais e pesos
def load_data():
    materials_volume = pd.DataFrame({
        "Categoria": ["Argamassas e concreto", "Blocos artificiais e pisos", "Madeiras", "Metais", "Rochas naturais"],
        "Material": [
            "Argamassa de areia e cimento",
            "Blocos de concreto vazados",
            "Cedro",
            "Aço",
            "Granito"
        ],
        "Peso (kN/m³)": [21, 16, 7, 78, 30]
    })
    return materials_volume

# Funções de cálculo
def calculate_isolated_element(weight, length, width, height):
    return weight * length * width * height

def calculate_inclined_element(weight, length, width, height, angle, case):
    total_weight = weight * length * width * height
    if case == "Caso 1":
        return total_weight * (angle * 3.1416 / 180)  # Simplificação de sin(θ)
    elif case == "Caso 2":
        return total_weight * (1 - angle * 3.1416 / 180) / 2  # Simplificação de cos(θ)

def calculate_rubble(weight, length, width, height, affected_area):
    total_weight = weight * length * width * height
    return total_weight / affected_area

def calculate_pavement(wall_area, wall_weight, floor_area, floor_weight, num_columns):
    wall_total = wall_area * wall_weight
    floor_total = floor_area * floor_weight
    return (wall_total + floor_total) / num_columns

# Interface da aplicação
materials_volume = load_data()

st.title("Calculadora de Cargas em Estruturas")

# Seleção do tipo de cálculo
calculation_type = st.sidebar.selectbox(
    "Selecione o tipo de cálculo:",
    ["Elemento Isolado", "Elemento Inclinado", "Escombros (Distribuição por Área)", "Pavimento Completo"]
)

# Entrada de dados para cada tipo de cálculo
if calculation_type == "Elemento Isolado":
    st.header("Cálculo: Elemento Isolado")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    weight = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    length = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    width = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    height = st.number_input("Altura (m):", min_value=0.0, format="%.2f")
    if st.button("Calcular"):
        total_weight = calculate_isolated_element(weight, length, width, height)
        st.success(f"Peso total do elemento: {total_weight:.2f} kN")

elif calculation_type == "Elemento Inclinado":
    st.header("Cálculo: Elemento Inclinado")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    weight = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    length = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    width = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    height = st.number_input("Altura (m):", min_value=0.0, format="%.2f")
    angle = st.number_input("Ângulo de inclinação (°):", min_value=0.0, max_value=90.0, format="%.1f")
    case = st.radio("Selecione o caso:", ["Caso 1", "Caso 2"])
    if st.button("Calcular"):
        force = calculate_inclined_element(weight, length, width, height, angle, case)
        st.success(f"Força calculada: {force:.2f} kN")

elif calculation_type == "Escombros (Distribuição por Área)":
    st.header("Cálculo: Escombros")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    weight = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    length = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    width = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    height = st.number_input("Altura (m):", min_value=0.0, format="%.2f")
    affected_area = st.number_input("Área afetada (m²):", min_value=0.1, format="%.2f")
    if st.button("Calcular"):
        distributed_weight = calculate_rubble(weight, length, width, height, affected_area)
        st.success(f"Peso distribuído: {distributed_weight:.2f} kN/m²")

elif calculation_type == "Pavimento Completo":
    st.header("Cálculo: Pavimento Completo")
    wall_area = st.number_input("Área total das paredes (m²):", min_value=0.0, format="%.2f")
    wall_weight = st.number_input("Peso por unidade de área das paredes (kN/m²):", min_value=0.0, format="%.2f")
    floor_area = st.number_input("Área total do piso (m²):", min_value=0.0, format="%.2f")
    floor_weight = st.number_input("Peso por unidade de área do piso (kN/m²):", min_value=0.0, format="%.2f")
    num_columns = st.number_input("Número total de colunas:", min_value=1, format="%d")
    if st.button("Calcular"):
        total_weight = calculate_pavement(wall_area, wall_weight, floor_area, floor_weight, num_columns)
        st.success(f"Peso por coluna: {total_weight:.2f} kN")

---

### **Próximos Passos**
Se você tiver dúvidas ou encontrar algo que precise de ajustes, posso fazer melhorias. Este é o código final ajustado. 😊
