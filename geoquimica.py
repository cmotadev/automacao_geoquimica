import streamlit as st
from owslib.wfs import WebFeatureService
from owslib.util import Authentication

import geopandas as gpd

NOVO_FCAMPO_WFS = 'https://geoservicos.cprm.gov.br/geoserver/geoquimica/wfs'

@st.cache
def load_data(bbox, max_features=1000):
    wfs = WebFeatureService(NOVO_FCAMPO_WFS, version='1.1.0', auth=Authentication(verify=False))
    response = wfs.getfeature(typename='geoquimica:novo-fcampo', bbox=bbox,
                              srsname='urn:x-ogc:def:crs:EPSG:4326', maxfeatures=max_features)

    data = gpd.read_file(response)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)

    return data

# Streamlit
# Barra lateral
min_x = st.sidebar.number_input(
    "Longitude minima",
    min_value=-75.,
    max_value=-30.,
    value=-41.26
)

min_y = st.sidebar.number_input(
    "Latitude minima",
    min_value=-35.,
    max_value=8.,
    value=-12.82
)

max_x = st.sidebar.number_input(
    "Longitude maxima",
    min_value=-75.,
    max_value=-30.,
    value=-40.88
)

max_y = st.sidebar.number_input(
    "Latitude maxima",
    min_value=-35.,
    max_value=8.,
    value=-12.52
)


max_features = st.sidebar.number_input(
    "Numero de Feicoes",
    min_value=1,
    max_value=10000,
    step=1,
    value=500
)

# Tela principal
st.title('Download dos dados do Novo FCampo')

data_load_state = st.text('Loading data...')
df = load_data((min_x, min_y, max_x, max_y), max_features)
df.plot()
data_load_state.text("Loaded!")

st.pyplot()
