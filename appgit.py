import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.write("# Novo Aplicativo")


l = np.random.randint(5,20,10)
st.write(l)

plt.plot(np.random.randn(200))
