import streamlit as st
# from streamlit.components.v1 import html


# st.set_page_config(layout="wide", page_title='ML')
# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden; }
#         footer {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)
# locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))


def main():
    st.title(f"ML Panel")
    st.write(f'Whether http://localhost:5000/Whether?submenu=whether')
    # st.write(f'Exchange http://{config["streamlit"]["ip"]}:9999/Standalone_Models?submenu=fraud')
    # st.write(f'Moderation http://{config["streamlit"]["ip"]}:9999/Monitoring?submenu=moderation')
    # st.write(f'NSFW http://{config["streamlit"]["ip"]}:9999/Search_Engine?submenu=nsfw')


if __name__ == "__main__":
    main()

