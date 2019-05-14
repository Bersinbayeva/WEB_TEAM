# from .old_w12 import category_list, category_detail, category_product
# from .fbv import sections_list, sections_detail, product_detail, product_list
from .cbv import CategoryList, CategoryDetail
# from .generic_cbv import BasketList, BasketDetail
from .auth import UserList, login, logout
from .csrf import sections_list, sections_detail, product_list, product_detail