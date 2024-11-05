import folium
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

from db_manager import get_list_of_places

app = FastAPI()
templates = Jinja2Templates(directory=".")


@app.get("/", response_class=HTMLResponse)
async def get_main_page(request: Request):
    # Создаем карту с заданными параметрами
    bel_map = folium.Map(location=[53.5290, 28.0450], zoom_start=7)

    # Получаем данные о местах
    places = get_list_of_places()

    # Конвертируем данные в DataFrame
    data = pd.DataFrame(
        [
            {
                'title': place.title,
                'description': place.description,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'img_url': place.img_url,
                'date_start': place.date_start,
                'date_end': place.date_end
            } for place in places
        ]
    )

    # Добавляем маркеры для каждого места
    for _, row in data.iterrows():
        marker_template_html = f"""
            <h2>{row['title']}</h2>
            <img src="{row['img_url']}" alt="{row['title']}" style="max-width: 100%; height: auto;">
            <p><strong>{row['date_start']} - {row['date_end']}</strong></p>
            <hr>
            <p>{row['description']}</p>
        """

        iframe = folium.IFrame(html=marker_template_html, width=200, height=300)
        popup = folium.Popup(iframe, max_width=2650)

        # Создаем маркер и добавляем его на карту
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=popup,
            tooltip=row['title']
        ).add_to(bel_map)

    return templates.TemplateResponse(
        name="index.html",
        context={"request": request, "map_iframe": bel_map._repr_html_()}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
