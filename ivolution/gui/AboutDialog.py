from gi.repository import Gtk

class AboutDialog():

    def __init__(self):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated AboutDialog object.
        """
        self.builder = Gtk.Builder()
        self.builder.add_from_file("ivolution/data/ui/AboutIvolutionDialog.glade")
        self.window = self.builder.get_object("about_ivolution_dialog")           

        self.window.run()
        self.window.destroy()