# Importações necessárias
import streamlit as st
import pandas as pd

# Tabelas com os dados fornecidos
# Tabela de Materiais com Peso por Volume
materials_volume = pd.DataFrame({
    "Categoria": [
        "Argamassas e concreto", "Argamassas e concreto", "Argamassas e concreto",
        "Blocos artificiais e pisos", "Blocos artificiais e pisos", "Blocos artificiais e pisos",
        "Blocos artificiais e pisos", "Blocos artificiais e pisos", "Madeiras", "Madeiras",
        "Madeiras", "Metais", "Metais", "Metais", "Metais", "Rochas naturais", "Rochas naturais"
    ],
    "Material": [
        "Argamassa de areia e cimento", "Argamassa de cal e gesso", "Concreto simples",
        "Blocos de concreto vazados", "Blocos cerâmicos vazados", "Blocos maciços",
        "Blocos de concreto celular autoclavado", "Porcelanato", "Cedro", "Compensados",
        "Ipê", "Aço", "Alumínio", "Bronze", "Chumbo", "Arenito", "Granito"
    ],
    "Peso (kN/m³)": [
        21, 15, 25, 16, 16, 18, 9, 23, 7, 10, 12, 78, 28, 88, 113, 27, 30
    ]
})

# Tabela de Materiais com Peso por Área
materials_area = pd.DataFrame({
    "Categoria": ["Paredes", "Telhados", "Revestimentos"],
    "Material": ["Alvenaria de tijolo comum", "Telhas cerâmicas", "Revestimento cerâmico"],
    "Peso (kN/m²)": [1.8, 0.6, 0.9]
})

# Tabela de Cargas Variáveis
occupations = pd.DataFrame({
    "Tipo de Ocupação": ["Residencial", "Comercial", "Industrial"],
    "Carga Variável (kN/m²)": [2.0, 3.0, 5.0]
})

# Funções de cálculo
def calcular_peso_total(volume, peso_por_volume):
    return volume * peso_por_volume

def calcular_forca_inclinada(peso, angulo, caso):
    import math
    if caso == 1:
        return peso / 2  # Força perpendicular na metade do comprimento
    elif caso == 2:
        return (peso * math.cos(math.radians(angulo))) / (2 * math.sin(math.radians(angulo)))

def calcular_escombros(peso_total, area_afetada):
    return peso_total / area_afetada

# Interface do Streamlit
st.title("Calculadora de Cargas Estruturais")

# Seleção do tipo de cálculo
calculation_type = st.selectbox(
    "Selecione o tipo de cálculo:",
    ["Elemento Isolado", "Elemento Inclinado", "Escombros (Distribuição por Área)", "Pavimento Completo"]
)

if calculation_type == "Elemento Isolado":
    st.header("Elemento Isolado")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    peso = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    comprimento = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    largura = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    altura = st.number_input("Altura (m):", min_value=0.0, format="%.2f")
    volume = comprimento * largura * altura
    peso_total = calcular_peso_total(volume, peso)
    st.write(f"Peso Total: {peso_total:.2f} kN")

elif calculation_type == "Elemento Inclinado":
    st.header("Elemento Inclinado")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    peso = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    comprimento = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    largura = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    altura = st.number_input("Altura (m):", min_value=0.0, format="%.2f")
    angulo = st.number_input("Ângulo de inclinação (°):", min_value=0.0, max_value=90.0, format="%.1f")
    volume = comprimento * largura * altura
    peso_total = calcular_peso_total(volume, peso)
    caso = st.radio("Selecione o caso:", [1, 2])
    forca = calcular_forca_inclinada(peso_total, angulo, caso)
    st.write(f"Força de equilíbrio (Caso {caso}): {forca:.2f} kN")

elif calculation_type == "Escombros (Distribuição por Área)":
    st.header("Escombros")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    peso = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    comprimento = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    largura = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    altura = st.number_input("Altura (m):", min_value=0.0, format="%.2f")
    area_afetada = st.number_input("Área afetada (m²):", min_value=0.1, format="%.2f")
    volume = comprimento * largura * altura
    peso_total = calcular_peso_total(volume, peso)
    peso_por_area = calcular_escombros(peso_total, area_afetada)
    st.write(f"Peso por unidade de área: {peso_por_area:.2f} kN/m²")

elif calculation_type == "Pavimento Completo":
    st.header("Pavimento Completo")
    wall_material = st.selectbox("Material das paredes:", materials_area["Material"])
    wall_weight = materials_area.loc[materials_area["Material"] == wall_material, "Peso (kN/m²)"].values[0]
    comprimento = st.number_input("Comprimento do pavimento (m):", min_value=0.0, format="%.2f")
    largura = st.number_input("Largura do pavimento (m):", min_value=0.0, format="%.2f")
    altura = st.number_input("Altura das paredes (m):", min_value=0.0, format="%.2f")
    area_paredes = 2 * (comprimento + largura) * altura
    peso_paredes = area_paredes * wall_weight
    st.write(f"Peso Total das Paredes: {peso_paredes:.2f} kN")
