import streamlit as st


def main():
    st.title("Esse é meu título")
    st.write("Um exemplo de texto")

    st.header("Input de texto")
    input_text = st.text_input("Digite um texto aqui")
    if input_text:
        st.write(f"Você digitou: {input_text}")

    st.header("Seleção")
    selected_option = st.selectbox("Selecione uma opção", ["Opção 1", "Opção 2", "Opção 3"])
    if selected_option:
        st.write(f"Opção selecionada: {selected_option}")

    st.header("Slider")
    slider_value = st.slider("Escolha um valor", 0, 100, 50)
    st.write("Valor escolhido:", slider_value)

    st.header("Checkbox")
    checkbox_state = st.checkbox("Marque para ativar")
    st.write(f"Checkbox ativado: {checkbox_state}")

    st.header("Gráfico")
    data = {'x':[1,2,3,4,5], 'y':[1,4,9,16,25]}
    st.line_chart(data)

if __name__ == "__main__":
    main()
