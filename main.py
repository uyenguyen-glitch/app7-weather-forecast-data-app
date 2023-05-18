import streamlit as st
import plotly.express as px
from backend import get_data

# Add widgets
st.title("Weather Forecast For The Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")




if place:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)
        if option == "Temperature":
             temperature = [dict["main"]["temp"] / 10for dict in filtered_data]
             dates = [dict["dt_txt"] for dict in filtered_data]

             # Create a temperature plot
             figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
             st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Rain": "images/rain.png", "Snow": "images/snow.png", "Clouds": "images/cloud.png"}
            img_paths = [images[condition] for condition in sky_conditions]
            st.image(img_paths, width=111)
    except KeyError:
        st.write("Your city is not correct!!!")

