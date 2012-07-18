from gi.repository import Gtk


class AboutDialog(Gtk.AboutDialog):

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated AboutDialog object.
        """
        self.builder = Gtk.Builder()
        self.builder.add_from_file("data/ui/AboutIvolutionDialog.glade")
        new_object = builder.get_object("about_ivolution_dialog")
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called while initializing this instance in __new__

        finish_initalizing should be called after parsing the ui definition
        and creating a AboutDialog object with it in order
        to finish initializing the start of the new AboutIvolutionDialog
        instance.
        
        Put your initialization code in here and leave __init__ undefined.
        """
        # Get a reference to the builder and set up the signals.
        print "in"