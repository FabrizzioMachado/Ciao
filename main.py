from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.network.urlrequest import UrlRequest  

class Temperation(App):
    def build(self):
        layout = FloatLayout()

        # Aggiungi il video di sfondo
        imagi = Image(source="immagine_2023-08-31_092336991.png")
        imagi.allow_stretch = True
        imagi.size_hint = (2.95, 2.9)
        imagi.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        imagi.opacity = 0.60
        layout.add_widget(imagi)

        # Aggiungi il titolo
        title_label = Label(text='TEMPERATION', bold=True, underline=True, italic=True,  font_size='45sp', pos_hint={"center_x": 0.5, "center_y": 0.8}, size_hint=(1, 0.1))
        layout.add_widget(title_label)

        # Le lettere sulla citta che stiamo cercando.
        self.etichetta = Label(text='Qui apparirà la tua città', bold=True,  font_size='20sp', pos_hint={"center_x": 0.5, "center_y": 0.7}, size_hint=(1, 0.1))
        layout.add_widget(self.etichetta)

        #InputTESTO
        self.input_text = TextInput(hint_text="Scrivi la città che cerchi.", pos_hint={"center_x": 0.5, "center_y": 0.2}, font_size='20sp', size_hint=(0.9, 0.09), halign="center", padding_y="12sp")
        self.input_text.bind(on_text_validate=lambda : self.trovaTemp(None))
        layout.add_widget(self.input_text)

        # Aggiungi il bottone
        button = Button(text='Cerca', background_color='#FFCC00', size_hint=(0.9, 0.08), bold=True, pos_hint={"center_x": 0.5, "center_y": 0.1}, halign="center")
        layout.add_widget(button)
        button.bind(on_press=self.trovaTemp)
        return layout

    def trovaTemp(self, instance):
        def edit_label(request, result):
            temp = result['main']['temp']
            self.etichetta.text = f"Attualmente a {self.input_text.text} ci sono {temp}°C"

        lang = "it"  # Imposta la lingua per le risposte dell'API
        api_key = "ceb2feb48163f24a3e08fd2335d0f8bd"  # Inserisci la tua API key di OpenWeatherMap

        link = f"https://api.openweathermap.org/data/2.5/weather?q={self.input_text.text}&appid={api_key}&units=metric&lang={lang}"
        UrlRequest(link, edit_label)

    def trovaTempOnEnter(self, instance): 
        self.trovaTemp(None)   

if __name__ == "__main__":  # Imposta l'app in modalità schermo intero
    Temperation().run()
