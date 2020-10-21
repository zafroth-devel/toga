from toga.handlers import wrapped_handler

from .base import Widget


class Switch(Widget):
    """ Switch widget, a clickable button with two stable states, True (on, checked) and False (off, unchecked)

    Args:
        label (str): Text to be shown next to the switch.
        id (str): AN identifier for this widget.
        style (:obj:`Style`): An optional style object.
            If no style is provided then a new one will be created for the widget.
        on_toggle (``callable``): Function to execute when pressed.
        on_gain_focus (:obj:`callable`): Function to execute when get focused.
        on_lose_focus (:obj:`callable`): Function to execute when lose focus.
        is_on (bool): Current on or off state of the switch.
        enabled (bool): Whether or not interaction with the button is possible, defaults to `True`.
        factory (:obj:`module`): A python module that is capable to return a
            implementation of this class with the same name. (optional & normally not needed)
    """

    def __init__(
            self,
            label,
            id=None,
            style=None,
            on_toggle=None,
            on_gain_focus=None,
            on_lose_focus=None,
            is_on=False,
            enabled=True,
            factory=None,
    ):
        super().__init__(
            id=id,
            style=style,
            on_gain_focus=on_gain_focus,
            on_lose_focus=on_lose_focus,
            factory=factory,
        )

        self._impl = self.factory.Switch(interface=self)

        self.label = label
        self.on_toggle = on_toggle
        self.is_on = is_on
        self.enabled = enabled
        self.on_gain_focus = on_gain_focus
        self.on_lose_focus = on_lose_focus

    @property
    def label(self):
        """ Accompanying text label of the Switch.

        Returns:
            The label text of the widget as a ``str``.
        """
        return self._label

    @label.setter
    def label(self, value):
        if value is None:
            self._label = ''
        else:
            self._label = str(value)
        self._impl.set_label(value)
        self._impl.rehint()

    @property
    def on_toggle(self):
        """ The callable function for when the switch is pressed

        Returns:
            The ``callable`` on_toggle function.
        """
        return self._on_toggle

    @on_toggle.setter
    def on_toggle(self, handler):
        self._on_toggle = wrapped_handler(self, handler)
        self._impl.set_on_toggle(self._on_toggle)

    @property
    def is_on(self):
        """ Button Off/On state.

        Returns:
            ``True`` if on and ``False`` if the switch is off.
        """
        return self._impl.get_is_on()

    @is_on.setter
    def is_on(self, value):
        if not isinstance(value, bool):
            raise ValueError("Switch.is_on can only be set to true or false")
        self._impl.set_is_on(value)

    def toggle(self):
        """Reverse the value of `Slider.is_on` property from true to false and
        vice versa.
        """
        self.is_on = not self.is_on
