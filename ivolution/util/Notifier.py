"""
.. module:: Notifier
   :platform: Unix, Windows
   :synopsis: Implements a simple Observer/Observable pattern for communication between between Facemovie thread and Ivolution GUI 

.. moduleauthor:: Julien Lengrand-Lambert <jlengrand@gmail.com>

"""

class Observer():
    """
    Implements a simple Observer from the Observer pattern
    """

    def __init__(self, name="Observer"):
        """
        """
        self.name = name


    def update(self, message):
        """
        """
        if message is not None:
            #print "%s received %s" %(self.name, message)
            pass

    def __str__(self):
        return self.name

class Observable():
    """
    Implements a simple Observable from the Observer pattern
    """

    def __init__(self):
        """
        """
        self.val = 1
        self.obs_collection = []


    def subscribe(self, observer):
        """
        """
        try:
            if not(observer in self.obs_collection):
                self.obs_collection.append(observer)
                #print "%s added to collection" %(str(observer))
            else:
                #print "%s already in collection" %(str(observer))
                pass

        except TypeError:
            #print "Failed to add %s" %(str(observer))
            pass

    def unsubscribe(self, observer):
        """
        """
        try:
            if observer in self.obs_collection:
                self.obs_collection.remove(observer)
                #print "%s removed from collection" %(str(observer))
            else:
                #print "%s not in collection" %(str(observer))
                pass

        except TypeError:
            #print "Failed to remove %s" %(str(observer))
            pass

    def notify(self, message):
        """
        """
        for observer in self.obs_collection:
            #print "sent %s to %s" %(message, str(observer))
            observer.update(message)


    def set_val(self, val=1):
        """
        """
        self.val += val
        self.notify(str(self.val))