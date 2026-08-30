import streamlit as st
from main import RandomPasswordGenerator, MemorablePasswordGenerator, Pingenerator


st.image("../images/images.png", width=500)
st.title(":zap: Password Generator")
'--------------------------------------------------------------'

option = st.radio(
    "Please Select the type of password generator you want to use:",
    ("Random Password Generator", "Memorable Password Generator", "Pin Generator")
)

"----------------------------------------------------------------"

if option == "Random Password Generator":
    length = st.number_input("Enter the length of the password:", min_value=1, max_value=100, value=8)
    include_numbers = st.checkbox("Include numbers?")
    include_symbols = st.checkbox("Include symbols?")
    
    if st.button("Generate Password"):
        generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
        st.success(f"Generated Password: {generator.generate()}")

elif option == "Memorable Password Generator":
    number_of_words = st.number_input("Enter the number of words:", min_value=2, max_value=10, value=4)
    seperator = st.text_input("Enter the separator (default is '-'):", value='-')
    capitalization = st.checkbox("Randomly capitalize words?")
    
    if st.button("Generate Password"):
        generator = MemorablePasswordGenerator(number_of_words, seperator, capitalization)
        st.success(f"Generated Password: {generator.generate()}")

elif option == "Pin Generator":
    length = st.number_input("Enter the length of the PIN:", min_value=1, max_value=10, value=4)
    
    if st.button("Generate PIN"):
        generator = Pingenerator(length)
        st.success(f"Generated PIN: {generator.generate()}")

