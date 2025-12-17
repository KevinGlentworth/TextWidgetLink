<h1 align="center">TextWidgetLink</h1>

<h3 align="center">Add highlighted URL link to a Text Widget.</h3>

```python
from TextWidgetLink import TextWidgetLink
tb_link = TextWidgetLink(textbox)

tb_link.create(the_text='Complex Numbers:', link_name='Complex',
               new_text='Complex Numbers', underline=True,
               popup_fg='red', popup_bg='lightgreen', popup_border='purple',
               the_link='https://en.wikipedia.org/wiki/Complex_number')
tb_link.create(the_text='Base Numbers:', link_name='Base', bg_color='gold', underline=True,
               fg_color='red', the_link='https://en.wikipedia.org/wiki/Radix')
tb_link.create(the_text='Roman Numbers:', link_name='Roman', underline=True, popup_bg='sandybrown',
               the_link='https://en.wikipedia.org/wiki/Roman_numerals')
tb_link.create(the_text='3.1415927', link_name='pi',
               the_link='https://en.wikipedia.org/wiki/Pi')
tb_link.create(the_text='[Email]', new_text='Email', show_url=False,
               link_name='email', the_link='mailto:name1.nam2@someemailserver')
```
![Screenshot](https://github.com/Crystalline-Entity/TextboxLink/blob/main/textwidgetlink_messagebox.png)
<br>
<h2 align='center'> OPTIONS </h2>
<div align='left'>


Parameters for calls to .create to create the link.

  | **Parameter** | **Description** | ** Default** |
  | --- | --- | --- |
  | the_text | The text in the widget to highlight | |
  | link_name | The name to use for this link | |
  | the_link | The URL to assign to the text | |
  | new_text | Replacement text for the_text. e.g. Text in the messagebox could have quotes for the search, but aren't needed for the link. | |
  | underline | True to underline text | True |
  | underlinefg | Underline colour | red |
  | hover_ul | Text colour when mouse hovers over text | green |
  | hover_bg | Background colour when mouse hovers over text | orange |
  | fg_color | Highlighted text foreground colour | blue |
  | bg_color | Highlighted text background colour | yellow |
  | popup_fg | Foreground colour of URL popup | blue |
  | popup_bg | background colour of URL popup | palegreen |
  | popup_border | border colour of URL popup | red |
  | popup_font | URL popup font, specified as ('family', size) | Code New Roman, 13 |
  | show_url | True or False. If False, no popup will be shown, the URL will not be seen | True |
