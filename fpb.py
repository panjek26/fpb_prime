import streamlit as st

def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

st.title('Mencari FPB')
a = st.number_input('Masukkan bilangan pertama', value=0, step=1)
b = st.number_input('Masukkan bilangan kedua', value=0, step=1)

if st.button('Cari FPB'):
    if a == 0 or b == 0:
        st.error('Harap masukkan bilangan yang valid.')
    else:
        result = fpb(a, b)
        st.success(f'FPB dari {a} dan {b} adalah {result}.')
