import streamlit as st   

if __name__ == '__main__':
    st.title('Mídias')

    st.markdown('---')
    st.subheader('Usando imagem')
    st.image('https://get.pxhere.com/photo/panorama-lake-sunset-background-image-wallpaper-nature-waters-landscape-clouds-mood-reflection-atmospheric-atmosphere-dusk-romantic-dramatic-afterglow-summer-evening-sky-horizon-water-dawn-calm-morning-cloud-wetland-water-resources-computer-wallpaper-sunrise-reservoir-sunlight-bank-earth-1444407.jpg'
            )

    st.markdown('---')
    st.subheader('Usando Mp3')
    st.audio('./Lace.mp3')

    st.markdown('---')
    st.subheader('Usando Video')
    st.video('https://www.youtube.com/watch?v=jfKfPfyJRdk')
