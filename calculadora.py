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
