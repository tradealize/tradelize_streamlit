import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.html(
    """
    <iframe src="https://tradealize.app" style="height: 100vh; width: 100%" />
    """,
    height=750
)