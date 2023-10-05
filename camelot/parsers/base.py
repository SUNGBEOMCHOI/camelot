import os

from ..utils import get_page_layout
from ..utils import get_text_objects


class BaseParser:
    """Defines a base parser."""

    def _generate_layout(self, filename, layout_kwargs, imagename=None, layout=None, dim=None):
        self.filename = filename
        self.imagename = imagename
        self.layout_kwargs = layout_kwargs
        # self.layout, self.dimensions = get_page_layout(filename, **layout_kwargs) # change
        if layout is None or dim is None:
            self.layout, self.dimensions = get_page_layout(filename, **layout_kwargs)
        else:
            self.layout, self.dimensions = layout, dim        
        self.images = get_text_objects(self.layout, ltype="image")
        self.horizontal_text = get_text_objects(self.layout, ltype="horizontal_text")
        self.vertical_text = get_text_objects(self.layout, ltype="vertical_text")
        self.pdf_width, self.pdf_height = self.dimensions
        if self.imagename is not None:
            self.imagename = imagename
            self.rootname = os.path.basename(imagename).split(".")[0]
        if self.filename is not None:
            self.rootname, __ = os.path.splitext(self.filename)
            self.imagename = "".join([self.rootname, ".png"])
