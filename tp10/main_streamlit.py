import streamlit as st
from CustomerDAO import CustomerDAO


def main():
    dao = CustomerDAO('customer_db.db')
    customers = dao.findAll()

    st.set_page_config(layout="wide")
    st.write("# Hello")

    st.button("Reset", type="primary")
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

    title = st.text_input('Votre nom', '')
    if st.button('Dire Bonjour'):
        st.write('Bonjour', title)

    l = list(customers)
    print(l[0].__dict__)
    st.table(l)

if __name__=='__main__':
    main()
