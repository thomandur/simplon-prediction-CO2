import streamlit as st
from api import Api

class Page:

    def __init__(self):
        st.set_page_config(layout='centered', page_icon="🧊")
        # self.df = Api.get_data('data/')

    def form_prediction(self):
        try:
            st.write(f"<p style='display:none'>{Api.get_data('data/get-feature/?feature=Fuel%20Type')}</p>", unsafe_allow_html=True)
            make = st.text_input('Marque de la voiture', placeholder="Audi, Aston Martin...", key = "make")
            model = st.text_input('Modèle de la voiture', placeholder="A4, A5...", key = "model")
            engine_size  = st.number_input('Taille du moteur (L)', min_value=0.00, key = "engine")
            vehicle_class  = st.selectbox('Class du véhicule', Api.get_data('data/get-feature/?feature=Vehicle%20Class'), key = "vehicle_class")
            cylinders  = st.number_input('Cylindres', min_value=0, key = "cylinders")
            transmission  = st.selectbox('Type de transmission', Api.get_data('data/get-feature/?feature=Transmission'), key = "transmission")
            fuel_type  = st.selectbox('Type de carburant', [f for f in Api.get_data('data/get-feature/?feature=Fuel%20Type') if f != 'N'], key = "fuel_type")
            cons_city  = st.number_input('Consommation en ville', min_value=1.00, key = "city")
            cons_hwy  = st.number_input('Consommation sur autoroute', min_value=1.00, key = "hwy")
            cons_comb  = st.number_input('Consommation combiné', min_value=1.00, key = "comb")

            if st.button('Predire'):
                st.metric('consommation', Api.predict(make,model,engine_size,vehicle_class,cylinders,transmission,fuel_type,cons_city,cons_hwy,cons_comb), 'g/km')

        except Exception:
            st.error('API is offline')
            # self.api_url()

    def api_url(self):
        new_url = st.text_input('New API URL:', key = "api_url")
        Api.change_baseurl(new_url)


    def container(self):
        st.title(':car: Emissions de CO2 (g/km)')
        self.form_prediction()

    def render(self):
        self.container()

if __name__ == "__main__":
    page = Page()
    page.render()
