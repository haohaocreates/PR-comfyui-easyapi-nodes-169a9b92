import torch

from .util import tensor_to_pil, hex_to_rgba


class GetImageBatchSize:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {
            "image": ('IMAGE', {}),
        },
        }

    RETURN_TYPES = ("NUMBER", "INT", "FLOAT",)
    RETURN_NAMES = ("number", "int", "float",)

    FUNCTION = "batch_size"

    OUTPUT_NODE = False
    CATEGORY = "EasyApi/Image"

    # INPUT_IS_LIST = False
    # OUTPUT_IS_LIST = (False, False)

    def batch_size(self, image):
        size = image.shape[0]
        return (size, size, float(size),)


class JoinList:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {
            "lst": ('LIST', {}),
            "delimiter": ('STRING', {"default": ','},),
        },
        }

    RETURN_TYPES = ("STRING",)
    # RETURN_NAMES = ("STRING", )

    FUNCTION = "join"

    OUTPUT_NODE = False
    CATEGORY = "EasyApi/List"

    # INPUT_IS_LIST = False
    # OUTPUT_IS_LIST = (False, False)

    def join(self, lst, delimiter=','):
        lst = delimiter.join(list(map(str, lst)))
        return (lst,)


class IntToNumber:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {
            "INT": ('INT', {"forceInput": True}),
        },
        }

    RETURN_TYPES = ("NUMBER",)

    FUNCTION = "convert"

    OUTPUT_NODE = False
    CATEGORY = "EasyApi/Integer"

    def convert(self, INT):
        return (INT,)


class IntToList:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "int_a": ('INT', {"forceInput": True}),
            },
            "optional": {
                "int_b": ('INT', {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("LIST",)

    FUNCTION = "convert"

    OUTPUT_NODE = False
    CATEGORY = "EasyApi/Integer"

    def convert(self, int_a, int_b=None):
        list = [int_a]
        if int_b:
            list.append(int_b)
        return (list,)


class StringToList:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "str_a": ('STRING', {"forceInput": True}),
            },
            "optional": {
                "str_b": ('STRING', {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("LIST",)

    FUNCTION = "convert"

    OUTPUT_NODE = False
    CATEGORY = "EasyApi/String"

    def convert(self, str_a, str_b=None):
        list = [str_a]
        if str_b:
            list.append(str_b)
        return (list,)


class ListMerge:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "list_a": ('LIST', {"forceInput": True}),
            },
            "optional": {
                "list_b": ('LIST', {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("LIST",)

    FUNCTION = "convert"

    OUTPUT_NODE = False
    CATEGORY = "EasyApi/String"

    def convert(self, list_a, list_b=None):
        list = [] + list_a
        if list_b:
            list = list + list_b
        return (list,)


class ShowString:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "str": ("STRING", {"forceInput": True}),
                "key": ('STRING', {"default": "text"}),
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "show"

    CATEGORY = "EasyApi/String"
    # 作为输出节点，返回数据格式是{"ui": {output_name:value}, "result": (value,)}
    # ui中是websocket返回给前端的内容，result是py执行传给下个节点用的
    OUTPUT_NODE = True

    def show(self, str, key):
        return {"ui": {key: (str,)}, "result": (str,)}


class ShowInt:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "INT": ("INT", {"forceInput": True}),
                "key": ('STRING', {"default": "text"}),
            }
        }

    RETURN_TYPES = ("INT",)

    FUNCTION = "show"

    CATEGORY = "EasyApi/Integer"
    # 作为输出节点，返回数据格式是{"ui": {output_name:value}, "result": (value,)}
    # ui中是websocket返回给前端的内容，result是py执行传给下个节点用的
    OUTPUT_NODE = True

    def show(self, INT, key):
        return {"ui": {key: (INT,)}, "result": (INT,)}


class ShowFloat:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "FLOAT": ("FLOAT", {"forceInput": True}),
                "key": ('STRING', {"default": "text"}),
            }
        }

    RETURN_TYPES = ("FLOAT",)

    FUNCTION = "show"

    CATEGORY = "EasyApi/Float"
    # 作为输出节点，返回数据格式是{"ui": {output_name:value}, "result": (value,)}
    # ui中是websocket返回给前端的内容，result是py执行传给下个节点用的
    OUTPUT_NODE = True

    def show(self, FLOAT, key):
        return {"ui": {key: (FLOAT,)}, "result": (FLOAT,)}


class ShowNumber:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "number": ("NUMBER", {"forceInput": True}),
                "key": ('STRING', {"default": "text"}),
            }
        }

    RETURN_TYPES = ("NUMBER",)

    FUNCTION = "show"

    CATEGORY = "EasyApi/Number"
    # 作为输出节点，返回数据格式是{"ui": {output_name:value}, "result": (value,)}
    # ui中是websocket返回给前端的内容，result是py执行传给下个节点用的
    OUTPUT_NODE = True

    def show(self, number, key):
        return {"ui": {key: (number,)}, "result": (number,)}


class ColorPicker:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {
                "color": ("SINGLECOLORPICKER",),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "INT",)
    RETURN_NAMES = ("HEX", "RGBA", "RGB", "A",)

    FUNCTION = "picker"

    CATEGORY = "EasyApi/Color"

    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, False, False, False, )

    def picker(self, color):
        r, g, b, a = hex_to_rgba(color)
        h = color
        rgba = f"#{r:02X}{g:02X}{b:02X}{a:02X}"
        rgb = f"#{r:02X}{g:02X}{b:02X}"
        return h, rgba, rgb, a,


class ImageEqual:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {
                "a": ("IMAGE",),
                "b": ('IMAGE',),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("is_b",)

    FUNCTION = "compare"

    CATEGORY = "EasyApi/Image"

    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False, )

    def compare(self, a, b):
        return torch.all(a == b),


NODE_CLASS_MAPPINGS = {
    "GetImageBatchSize": GetImageBatchSize,
    "JoinList": JoinList,
    "IntToNumber": IntToNumber,
    "StringToList": StringToList,
    "IntToList": IntToList,
    "ListMerge": ListMerge,
    "ShowString": ShowString,
    "ShowInt": ShowInt,
    "ShowNumber": ShowNumber,
    "ShowFloat": ShowFloat,
    "ColorPicker": ColorPicker,
    "ImageEqual": ImageEqual,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "GetImageBatchSize": "GetImageBatchSize",
    "JoinList": "Join List",
    "IntToNumber": "Int To Number",
    "StringToList": "String To List",
    "IntToList": "Int To List",
    "ListMerge": "Merge List",
    "ShowString": "Show String",
    "ShowInt": "Show Int",
    "ShowNumber": "Show Number",
    "ShowFloat": "Show Float",
    "ColorPicker": "Color Picker",
    "ImageEqual": "Image Equal Judgment",
}
