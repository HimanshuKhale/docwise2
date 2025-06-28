from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import requests
from plyer import storagepath


# Set default size (for desktop testing)
Window.size = (360, 640)

class HomeScreen(MDScreen):
    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical')

        toolbar = MDTopAppBar(title="Docwise App", pos_hint={"top": 1})
        layout.add_widget(toolbar)

        img = Image(source="assets/bg.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(img)

        # Fix: use a bound method instead of lambda with assignment
        btn = MDRaisedButton(
            text="Create Document",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_release=self.go_to_form
        )
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_to_form(self, instance):
        self.manager.current = "form"

class FormScreen(MDScreen):
    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(MDLabel(text="Enter Details", halign="center", font_style="H5"))

        self.name_input = MDTextField(hint_text="Enter Name")
        self.address_input = MDTextField(hint_text="Enter Address")
        layout.add_widget(self.name_input)
        layout.add_widget(self.address_input)

        submit_btn = MDRaisedButton(text="Submit", pos_hint={"center_x": 0.5})
        submit_btn.bind(on_release=self.submit_form)
        layout.add_widget(submit_btn)

        self.add_widget(layout)

    def submit_form(self, *args):
        name = self.name_input.text
        address = self.address_input.text
        data = {"name": name, "address": address}

        api_url = "https://trial-api-2.onrender.com/generate-pdf/"
        response = requests.post(api_url, json=data)

        if response.status_code == 200:
            pdf_data = response.content

            # Get filename from headers
            content_disposition = response.headers.get("Content-Disposition", "")
            filename = "generated_doc.pdf"  # fallback
            if "filename=" in content_disposition:
                filename = content_disposition.split("filename=")[-1].strip().strip('"')

            # Save file to Downloads directory
            filepath = storagepath.get_downloads_dir() + f"/{filename}"
            with open(filepath, "wb") as f:
                f.write(pdf_data)

            self.manager.current = "success"
        else:
            print("Error:", response.status_code)

class SuccessScreen(MDScreen):
    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(MDLabel(text="✅ Document Submitted Successfully!", halign="center", font_style="H5"))

        back_btn = MDRaisedButton(
            text="Back to Home",
            pos_hint={"center_x": 0.5},
            on_release=self.go_home
        )
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_home(self, instance):
        self.manager.current = "home"


class DocwiseApp(MDApp):
    def build(self):
        self.title = "Docwise Mobile"
        sm = MDScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(FormScreen(name="form"))
        sm.add_widget(SuccessScreen(name="success"))
        return sm

if __name__ == "__main__":
    DocwiseApp().run()
