# django imports
from django.forms import ModelForm

# muecke imports
from muecke.core.widgets.image import LFSImageInput
from muecke.shipping.models import ShippingMethod


class ShippingMethodAddForm(ModelForm):
    """Form to add a shipping method.
    """
    class Meta:
        model = ShippingMethod
        fields = ["name"]


class ShippingMethodForm(ModelForm):
    """
    """
    def __init__(self, *args, **kwargs):
        super(ShippingMethodForm, self).__init__(*args, **kwargs)
        self.fields["image"].widget = LFSImageInput()

    class Meta:
        model = ShippingMethod
        exclude = ("priority", )
