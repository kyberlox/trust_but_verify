from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class  MakePhotoApp(App):
  def build(self):
    
    #camera
    self.camera_obj = Camera()
     
    #button
		button_obj = Button(text = 'Photo!')
		button_obj.bind(on_press = self.photo)
    
    #Layout
		layout = BoxLayout()
		layout.add_widget(self.camera_obj)
		layout.add_widget(button_obj)
		return layout
    
   def photo(self, *args):
    print("Try selfie")
		self.camera_obj.export_to_png("./selfie.png")


if __name__ == '__main__':
	MakePhotoApp().run()
