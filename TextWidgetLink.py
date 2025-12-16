from webbrowser import open_new as open_link
from tkinter import Toplevel, Label
class TextWidgetLink:
    """
    Author: Kevin Glentworth
    Date: December-2025
    Adds clickable URLs to a text widget.
    """
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.popup: Toplevel = None

        
    def show_url_popup(self, message, p_fg: str='blue', p_bg: str='lightyellow', p_bd: str='red', p_font: list = None):
        """
        Shows the URL of the link under the mouse.

        If the mouse pointer ends up over the popup object, it is treated as a <Leave>, which closes the popup window.
        As the mouse is still within the text_widget, it then performs another <Enter> and goes into a loop until the mouse is
        moved off the popup. Adjust both mouse_x and mouse_y to keep the popup away from the mouse cursor.
        The popup_border isn't a Label widget item, it is applied to the Toplevel widget with padding, to make it appear
        as a border colour.
        """
        mouse_x = self.text_widget.winfo_pointerx() + 10
        mouse_y = self.text_widget.winfo_pointery() - 30

        self.popup = Toplevel(self.text_widget, bg=p_bd, padx=2, pady=2) # padx & pady allow the colour to show around the label.
        self.popup.overrideredirect(True)
        self.popup.geometry(f'+{mouse_x}+{mouse_y}')
        self.popup.attributes('-topmost', True) # Ensure the popup is above everything else.

        Label(self.popup, text=message, fg=p_fg, bg=p_bg, relief='flat', borderwidth=0, padx=2, pady=2, font=p_font).pack()

        
    def kill_url_popup(self):
        self.popup.destroy()

    def do_enter(self, show_url, link_name, the_link, hover_ul, hover_bg, popup_fg, popup_bg, popup_border, popup_font):
        self.text_widget.configure(cursor='hand2')
        self.text_widget.tag_config(link_name, underlinefg=hover_ul, background=hover_bg)
        if show_url:
            self.show_url_popup(the_link, popup_fg, popup_bg, popup_border, popup_font)

    def do_leave(self, show_url, link_name, underlinefg, bg_color):
        self.text_widget.configure(cursor='xterm')
        self.text_widget.tag_config(link_name, underlinefg=underlinefg, background=bg_color)
        if show_url:
            self.kill_url_popup()

    def create(self,
               the_text: str,
               link_name: str,
               the_link: str,
               new_text: str = None,
               underline: bool=True,
               underlinefg: str='red',
               hover_ul: str='green',
               hover_bg: str='orange',
               fg_color: str='blue',
               bg_color: str='yellow',
               popup_fg: str='blue',
               popup_bg: str='palegreen',
               popup_border: str='red',
               popup_font: list = ('Code New Roman', 13),
               show_url: bool = True):
        str0: str = self.text_widget.get('1.0', 'end')
        if len(str0) == 0:
            return
        if (text_length := len(the_text)) == 0:
            return
        if (find_location := str0.find(the_text)) == -1:
            return
        begin_pos = '1.0 linestart+' + str(find_location) + 'c'
        if new_text is not None and len(new_text) > 0:
            end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
            self.text_widget.configure(state='normal')
            self.text_widget.delete(begin_pos, end_pos)
            self.text_widget.insert(begin_pos, new_text)
            self.text_widget.configure(state='disabled')
            text_length = len(new_text)
            # str0 = self.text_widget.get('1.0', 'end') # reload text from widget rather than slicing str0
        end_pos = '1.0 linestart+' + str(find_location + text_length) + 'c'
        self.text_widget.tag_add(link_name, begin_pos, end_pos)
        if fg_color is not None:
            self.text_widget.tag_config(link_name, foreground=fg_color)
        if bg_color is not None:
            self.text_widget.tag_config(link_name, background=bg_color)
        if underline is not None:
            self.text_widget.tag_config(link_name, underline=underline)
        if underlinefg is not None:
            self.text_widget.tag_config(link_name, underlinefg=underlinefg)
        self.text_widget.tag_bind(link_name, '<Button-1>', lambda x: open_link(the_link))
        self.text_widget.tag_bind(link_name, '<Enter>', lambda x: self.do_enter(show_url, link_name, the_link, hover_ul, hover_bg,
                                                                                popup_fg, popup_bg, popup_border, popup_font))
        self.text_widget.tag_bind(link_name, '<Leave>', lambda x: self.do_leave(show_url, link_name, underlinefg, bg_color))

if __name__ == '__main__':
    exit()
