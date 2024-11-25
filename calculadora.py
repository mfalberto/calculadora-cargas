import streamlit as st

# Título da aplicação
st.title("Calculadora de Cargas em Estruturas")

# Seleção do tipo de cálculo
calculation_type = st.selectbox(
    "Selecione o tipo de cálculo:",
    ["Elemento Isolado", "Elemento Inclinado", "Escombros (Distribuição por Área)", "Pavimento Completo"]
)

# Exibição do tipo selecionado
st.write(f"Você selecionou: {calculation_type}")

# Próximo passo (simulação de navegação para as próximas seções)
if calculation_type == "Elemento Isolado":
    st.write("Avançando para a seção de entrada de dados para Elemento Isolado...")
elif calculation_type == "Elemento Inclinado":
    st.write("Avançando para a seção de entrada de dados para Elemento Inclinado...")
elif calculation_type == "Escombros (Distribuição por Área)":
    st.write("Avançando para a seção de entrada de dados para Escombros...")
elif calculation_type == "Pavimento Completo":
    st.write("Avançando para a seção de entrada de dados para Pavimento Completo...")
# Entrada de Dados Dinâmica para Cada Tipo de Cálculo

# Carregar tabelas de materiais e cargas
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

materials_area = pd.DataFrame({
    "Categoria": ["Paredes", "Telhados", "Revestimentos"],
    "Material": [
        "Alvenaria de tijolo comum",
        "Telhas cerâmicas",
        "Revestimento cerâmico"
    ],
    "Peso (kN/m²)": [1.8, 0.6, 0.9]
})

occupations = pd.DataFrame({
    "Tipo de Ocupação": ["Residencial", "Comercial", "Industrial"],
    "Carga Variável (kN/m²)": [2.0, 3.0, 5.0]
})

# Seção de entrada de dados para cada tipo de cálculo
if calculation_type == "Elemento Isolado":
    st.header("Entrada de Dados: Elemento Isolado")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    weight = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    st.write(f"Peso por unidade de volume: {weight} kN/m³")
    length = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    width = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    height = st.number_input("Altura (m):", min_value=0.0, format="%.2f")

elif calculation_type == "Elemento Inclinado":
    st.header("Entrada de Dados: Elemento Inclinado")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    weight = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    st.write(f"Peso por unidade de volume: {weight} kN/m³")
    length = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    width = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    height = st.number_input("Altura (m):", min_value=0.0, format="%.2f")
    angle = st.number_input("Ângulo de inclinação (°):", min_value=0.0, max_value=90.0, format="%.1f")

elif calculation_type == "Escombros (Distribuição por Área)":
    st.header("Entrada de Dados: Escombros")
    material = st.selectbox("Selecione o material:", materials_volume["Material"])
    weight = materials_volume.loc[materials_volume["Material"] == material, "Peso (kN/m³)"].values[0]
    st.write(f"Peso por unidade de volume: {weight} kN/m³")
    length = st.number_input("Comprimento (m):", min_value=0.0, format="%.2f")
    width = st.number_input("Largura (m):", min_value=0.0, format="%.2f")
    height = st.number_input("Altura (m):", min_value=0.0, format="%.2f")
    affected_area = st.number_input("Área afetada (m²):", min_value=0.1, format="%.2f")

elif calculation_type == "Pavimento Completo":
    st.header("Entrada de Dados: Pavimento Completo")
    wall_material = st.selectbox("Material das paredes:", materials_area["Material"])
    wall_weight = materials_area.loc[materials_area["Material"] == wall_material, "Peso (kN/m²)"].values[0]
    st.write(f"Peso por unidade de área das paredes: {wall_weight} kN/m²")
    floor_material = st.selectbox("Material do piso:", materials_area["Material"])
    floor_weight = materials_area.loc[materials_area["Material"] == floor_material, "Peso (kN/m²)"].values[0]
    st.write(f"Peso por unidade de área do piso: {floor_weight} kN/m²")
    floor_area = st.number_input("Área do pavimento (m²):", min_value=0.0, format="%.2f")
    num_columns = st.number_input("Número total de colunas:", min_value=1, format="%d")
