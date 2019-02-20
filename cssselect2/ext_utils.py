def textstring(el):
    """Return a text string of all text for subtree of el."""
    strval = u''
    strval += (el.etree_element.text or u'')
    for elem in el.iter_children():
        strval += textstring(elem)
    strval += (el.etree_element.tail or u'')
    return strval
