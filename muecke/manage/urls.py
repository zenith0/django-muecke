from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# General
urlpatterns = patterns('muecke.manage.views',
    url(r'^$', "dashboard", name="muecke_manage_dashboard"),
)

# Delivery Times
urlpatterns += patterns('muecke.manage.delivery_times.views',
    url(r'^delivery_times$', "manage_delivery_times", name="muecke_manage_delivery_times"),
    url(r'^delivery_time/(?P<id>\d*)$', "manage_delivery_time", name="muecke_manage_delivery_time"),
    url(r'^add-delivery-time$', "add_delivery_time", name="muecke_manage_add_delivery_time"),
    url(r'^delete-delivery-time/(?P<id>\d*)$', "delete_delivery_time", name="muecke_delete_delivery_time"),
    url(r'^no-times$', "no_delivery_times", name="muecke_no_delivery_times"),
)

# Manufacturer
urlpatterns += patterns('muecke.manage.manufacturers.views',
    url(r'^manufacturer-dispatcher$', "manufacturer_dispatcher", name="muecke_manufacturer_dispatcher"),
    url(r'^manufacturer/(?P<manufacturer_id>\d*)$', "manage_manufacturer", name="muecke_manufacturer"),
    url(r'^update-manufacturer-data/(?P<manufacturer_id>\d*)$', "update_data", name="muecke_manufacturer_update_manufacturer_data"),
    url(r'^add-manufacturer$', "add_manufacturer", name="muecke_manufacturer_add_manufacturer"),
    url(r'^delete-manufacturer/(?P<manufacturer_id>\d*)$', "delete_manufacturer", name="muecke_manufacturer_delete_manufacturer"),
    url(r'^edit-category-manufacturer/(?P<manufacturer_id>\d*)/(?P<category_id>\d*)$', "edit_category", name="muecke_manufacturer_edit_category"),
    url(r'^edit-product-manufacturer/(?P<manufacturer_id>\d*)/(?P<product_id>\d*)$', "edit_product", name="muecke_manufacturer_edit_product"),
    url(r'^category-state-manufacturer/(?P<manufacturer_id>\d*)/(?P<category_id>\d*)$', "category_state", name="muecke_manufacturer_category_state"),
    url(r'^manufacturer-inline/(?P<manufacturer_id>\d*)/(?P<category_id>\d*)$', "manufacturer_inline", name="muecke_manufacturer_inline"),
    url(r'^manufacturers-ajax/$', "manufacturers_ajax", name="muecke_manufacturers_ajax"),
    url(r'^no-manufacturers$', "no_manufacturers", name="muecke_manage_no_manufacturers"),
)

# Marketing
urlpatterns += patterns('muecke.manage.views.marketing',
    url(r'^featured$', "marketing.manage_featured_page", name="muecke_manage_featured"),
    url(r'^add-featured$', "featured.add_featured", name="muecke_manage_add_featured"),
    url(r'^update-featured$', "featured.update_featured", name="muecke_manage_update_featured"),
    url(r'^featured-inline$', "featured.manage_featured_inline", name="muecke_manage_featured_inline"),
    url(r'^marketing$', "marketing.manage_marketing", name="muecke_manage_marketing"),
    url(r'^manage-rating-mails$', "rating_mails.manage_rating_mails", name="muecke_manage_rating_mails"),
    url(r'^add-topseller$', "topseller.add_topseller", name="muecke_manage_add_topseller"),
    url(r'^update-topseller$', "topseller.update_topseller", name="muecke_manage_update_topseller"),
    url(r'^topseller-inline$', "topseller.manage_topseller_inline", name="muecke_manage_topseller_inline"),
    url(r'^send-rating-mails$', "rating_mails.send_rating_mails", name="muecke_send_rating_mails"),
)

# # Voucher
# urlpatterns += patterns('muecke.manage.voucher.views',
#     url(r'^vouchers$', "manage_vouchers", name="muecke_manage_vouchers"),
#     url(r'^no-vouchers$', "no_vouchers", name="muecke_no_vouchers"),
#     url(r'^add-voucher-group$', "add_voucher_group", name="muecke_manage_add_voucher_group"),
#     url(r'^voucher-group/(?P<id>\d+)$', "voucher_group", name="muecke_manage_voucher_group"),
#     url(r'^delete-voucher-group/(?P<id>\d+)$', "delete_voucher_group", name="muecke_delete_voucher_group"),
#     url(r'^save-voucher-group-data/(?P<id>\d+)$', "save_voucher_group_data", name="muecke_manage_save_voucher_group_data"),
#     url(r'^save-voucher-options$', "save_voucher_options", name="muecke_manage_save_voucher_options"),
#     url(r'^add-vouchers/(?P<group_id>\d+)$', "add_vouchers", name="muecke_manage_add_vouchers"),
#     url(r'^delete-vouchers/(?P<group_id>\d+)$', "delete_vouchers", name="muecke_manage_delete_vouchers"),
#     url(r'^set-vouchers-page$', "set_vouchers_page", name="muecke_set_vouchers_page"),
# )

# Portlets
urlpatterns += patterns('muecke.manage.views.muecke_portlets',
    url(r'^add-portlet/(?P<object_type_id>\d+)/(?P<object_id>\d+)$', "add_portlet", name="muecke_add_portlet"),
    url(r'^update-portlets/(?P<object_type_id>\d+)/(?P<object_id>\d+)$', "update_portlets", name="muecke_update_portlets"),
    url(r'^delete-portlet/(?P<portletassignment_id>\d+)$', "delete_portlet", name="muecke_delete_portlet"),
    url(r'^edit-portlet/(?P<portletassignment_id>\d+)$', "edit_portlet", name="muecke_edit_portlet"),
    url(r'^move-portlet/(?P<portletassignment_id>\d+)$', "move_portlet", name="muecke_move_portlet"),
)

# Product
urlpatterns += patterns('muecke.manage.product.product',
    url(r'^product-dispatcher$', "product_dispatcher", name="muecke_manage_product_dispatcher"),
    url(r'^product-by-id/(?P<product_id>\d*)$', "product_by_id", name="muecke_manage_product_by_id"),
    url(r'^product/(?P<product_id>\d*)$', "manage_product", name="muecke_manage_product"),
    url(r'^product-data-form/(?P<product_id>\d*)$', "product_data_form"),
    url(r'^add-product$', "add_product", name="muecke_manage_add_product"),
    url(r'^edit-product-data/(?P<product_id>\d*)$', "edit_product_data", name="muecke_manage_edit_product_data"),
    url(r'^delete-product/(?P<product_id>\d*)$', "delete_product", name="muecke_manage_delete_product"),
    url(r'^selectable-products-inline$', "selectable_products_inline", name="muecke_manage_selectable_products_inline"),
    url(r'^save-product-stock/(?P<product_id>\d*)$', "stock", name="muecke_save_product_stock"),
    url(r'^change-product-subtype/(?P<product_id>\d*)$', "change_subtype", name="muecke_change_product_subtype"),
    url(r'^products$', "products", name="muecke_manage_products"),
    url(r'^products-inline$', "products_inline", name="muecke_products_inline"),
    url(r'^save-products$', "save_products", name="muecke_manage_save_products"),
    url(r'^set-product-filters$', "set_filters", name="muecke_set_product_filters"),
    url(r'^set-product-name-filter$', "set_name_filter", name="muecke_set_product_name_filter"),
    url(r'^reset-product-filters$', "reset_filters", name="muecke_reset_product_filters"),
    url(r'^set-products-page$', "set_products_page", name="muecke_set_products_page"),
    url(r'^no-products$', "no_products", name="muecke_manage_no_products"),
)

urlpatterns += patterns('muecke.manage.product',
    url(r'^product-categories-tab/(?P<product_id>\d*)$', "categories.manage_categories", name="muecke_product_categories_tab"),
    url(r'^product-accessories-tab/(?P<product_id>\d*)$', "accessories.load_tab", name="muecke_manage_product_accessories_tab"),
    url(r'^product-relateds-tab/(?P<product_id>\d*)$', "related_products.load_tab", name="muecke_manage_product_related_products_tab"),
    url(r'^product-variants-tab/(?P<product_id>\d*)$', "variants.manage_variants", name="muecke_manage_product_variants_tab"),
)

urlpatterns += patterns('muecke.manage.product.categories',
    url(r'^change-product-categories/(?P<product_id>\d*)$', "change_categories", name="muecke_manage_product_categories"),
)

# Product Images
urlpatterns += patterns('muecke.manage.product.images',
    url(r'^add-image/(?P<product_id>\d*)$', "add_image", name="muecke_manage_add_image"),
    url(r'^update-images/(?P<product_id>\d*)$', "update_images", name="muecke_manage_update_images"),
    url(r'^product-images/(?P<product_id>\d*)$', "manage_images", name="muecke_manage_images"),
    url(r'^update-active-images/(?P<product_id>\d*)$', "update_active_images", name="muecke_manage_update_active_images"),
    url(r'^move-image/(?P<id>\d+)$', "move_image", name="lfc_move_image"),
)

# Product Attachments
urlpatterns += patterns('muecke.manage.product.attachments',
    url(r'^add-attachment/(?P<product_id>\d*)$', "add_attachment", name="muecke_manage_add_attachment"),
    url(r'^update-attachments/(?P<product_id>\d*)$', "update_attachments", name="muecke_manage_update_attachments"),
    url(r'^product-attachments/(?P<product_id>\d*)$', "manage_attachments", name="muecke_manage_attachments"),
    url(r'^move-product-attachments/(?P<id>\d+)$', "move_attachment", name="muecke_move_product_attachment"),
)

# Product SEO
urlpatterns += patterns('muecke.manage.product.seo',
    url(r'^manage-seo/(?P<product_id>\d*)$', "manage_seo", name="muecke_manage_product_seo"),
)

# Product Variants
urlpatterns += patterns('muecke.manage.product.variants',
    url(r'^properties/(?P<product_id>\d*)$', "manage_variants", name="muecke_manage_variants"),
    url(r'^add-property/(?P<product_id>\d*)$', "add_property", name="muecke_manage_add_property"),
    url(r'^add-property-option/(?P<product_id>\d*)$', "add_property_option", name="muecke_manage_add_property_option"),
    url(r'^delete-property/(?P<product_id>\d*)/(?P<property_id>\d*)$', "delete_property", name="muecke_manage_delete_property"),
    url(r'^delete-property-option/(?P<product_id>\d*)/(?P<option_id>\d*)$', "delete_property_option", name="muecke_manage_delete_property_option"),
    url(r'^change-property-position$', "change_property_position", name="muecke_manage_change_property_position"),
    url(r'^update-variants/(?P<product_id>\d*)$', "update_variants", name="muecke_manage_update_variants"),
    url(r'^add-variants/(?P<product_id>\d*)$', "add_variants", name="muecke_manage_add_variants"),
    url(r'^edit-sub-type/(?P<product_id>\d*)$', "edit_sub_type", name="muecke_manage_edit_sub_type"),
    url(r'^update-category-variant/(?P<product_id>\d*)$', "update_category_variant", name="muecke_update_category_variant"),
)

# Global Images
urlpatterns += patterns('muecke.manage.images.views',
    url(r'^imagebrowser$', "imagebrowser", name="muecke_manage_imagebrowser"),
    url(r'^global-images$', "images", name="muecke_manage_global_images"),
    url(r'^delete-global-images$', "delete_images", name="muecke_manage_delete_images"),
    url(r'^add-global-images$', "add_images", name="muecke_manage_add_global_image"),
)

# Property Groups
urlpatterns += patterns('muecke.manage.property_groups.views',
    url(r'^property-groups', "manage_property_groups", name="muecke_manage_property_groups"),
    url(r'^property-group/(?P<id>\d*)', "manage_property_group", name="muecke_manage_property_group"),
    url(r'^add-property-group', "add_property_group", name="muecke_manage_add_property_group"),
    url(r'^delete-property-group/(?P<id>\d*)', "delete_property_group", name="muecke_delete_property_group"),
    url(r'^assign-properties/(?P<group_id>\d*)', "assign_properties", name="muecke_assign_properties"),
    url(r'^update-properties/(?P<group_id>\d*)', "update_properties", name="muecke_update_properties"),
    url(r'^no-property-groups$', "no_property_groups", name="muecke_manage_no_property_groups"),
)

# Property Groups / Products
urlpatterns += patterns('muecke.manage.property_groups.views',
    url(r'^assign-products-to-property-group/(?P<group_id>\d*)', "assign_products", name="muecke_assign_products_to_property_group"),
    url(r'^remove-products-from-property-group/(?P<group_id>\d*)', "remove_products", name="muecke_pg_remove_products"),
    url(r'^pg-products-inline/(?P<product_group_id>\d*)', "products_inline", name="muecke_pg_products_inline"),
)

# Shop Properties
urlpatterns += patterns('muecke.manage.property.views',
    url(r'^shop-properties$', "manage_properties", name="muecke_manage_shop_properties"),
    url(r'^shop-property/(?P<id>\d*)', "manage_property", name="muecke_manage_shop_property"),
    url(r'^update-shop-property-type/(?P<id>\d*)', "update_property_type", name="muecke_update_shop_property_type"),
    url(r'^add-shop-property$', "add_property", name="muecke_add_shop_property"),
    url(r'^delete-shop-property/(?P<id>\d*)', "delete_property", name="muecke_delete_shop_property"),
    url(r'^add-shop-property-option/(?P<property_id>\d*)', "add_option", name="muecke_add_shop_property_option"),
    url(r'^add-shop-property-step/(?P<property_id>\d*)', "add_step", name="muecke_add_shop_property_step"),
    url(r'^save-shop-property-step/(?P<property_id>\d*)', "save_step_range", name="muecke_save_shop_property_step_range"),
    url(r'^save-shop-property-step-type/(?P<property_id>\d*)', "save_step_type", name="muecke_save_shop_property_step_type"),
    url(r'^delete-shop-property-option/(?P<id>\d*)', "delete_option", name="muecke_delete_shop_property_option"),
    url(r'^delete-shop-property-step/(?P<id>\d*)', "delete_step", name="muecke_delete_shop_property_step"),
    url(r'^save-number-field-validators/(?P<property_id>\d*)', "save_number_field_validators", name="muecke_save_number_field_validators"),
    url(r'^save-select-field/(?P<property_id>\d*)', "save_select_field", name="muecke_save_select_field"),
    url(r'^no-properties$', "no_properties", name="muecke_manage_no_shop_properties"),
)

# Product properties
urlpatterns += patterns('muecke.manage.product.properties',
    url(r'^update-product-properties/(?P<product_id>\d*)$', "update_properties", name="muecke_update_product_properties"),
    url(r'^update-product-property-groups/(?P<product_id>\d*)$', "update_property_groups", name="muecke_update_product_property_groups"),
)

# # Accesories
# urlpatterns += patterns('muecke.manage.product.accessories',
#     url(r'^accessories/(?P<product_id>\d*)$', "manage_accessories", name="muecke_manage_accessories"),
#     url(r'^accessories-inline/(?P<product_id>\d*)$', "manage_accessories_inline", name="muecke_manage_accessories_inline"),
#     url(r'^add-accessories/(?P<product_id>\d*)$', "add_accessories", name="muecke_manage_add_accessories"),
#     url(r'^remove-accessories/(?P<product_id>\d*)$', "remove_accessories", name="muecke_manage_remove_accessories"),
#     url(r'^update-accessories/(?P<product_id>\d*)$', "update_accessories", name="muecke_manage_update_accessories"),
# )

# Related Products
urlpatterns += patterns('muecke.manage.product.related_products',
    url(r'^related-products/(?P<product_id>\d*)$', "manage_related_products", name="muecke_manage_related_products"),
    url(r'^related-products-inline/(?P<product_id>\d*)$', "manage_related_products_inline", name="muecke_manage_related_products_inline"),
    url(r'^add-related-products/(?P<product_id>\d*)$', "add_related_products", name="muecke_manage_add_related_products"),
    url(r'^remove-related-products/(?P<product_id>\d*)$', "remove_related_products", name="muecke_manage_remove_related_products"),
    url(r'^manage-related-products/(?P<product_id>\d*)$', "update_related_products", name="muecke_manage_update_related_products"),
)

# Carts
urlpatterns += patterns('muecke.manage.views.carts',
    url(r'^carts$', "carts_view", name="muecke_manage_carts"),
    url(r'^carts-inline$', "carts_inline", name="muecke_carts_inline"),
    url(r'^cart-inline/(?P<cart_id>\d*)$', "cart_inline", name="muecke_cart_inline"),
    url(r'^cart/(?P<cart_id>\d*)$', "cart_view", name="muecke_manage_cart"),
    url(r'^selectable-carts-inline$', "selectable_carts_inline", name="muecke_selectable_carts_inline"),
    url(r'^set-cart-filters$', "set_cart_filters", name="muecke_set_cart_filters"),
    url(r'^set-cart-filters-date$', "set_cart_filters_date", name="muecke_set_cart_filters_date"),
    url(r'^reset-cart-filters$', "reset_cart_filters", name="muecke_reset_cart_filters"),
    url(r'^set-carts-page$', "set_carts_page", name="muecke_set_carts_page"),
    url(r'^set-cart-page$', "set_cart_page", name="muecke_set_cart_page"),
)

# Categories
urlpatterns += patterns('muecke.manage.categories',
    url(r'^categories$', "manage_categories", name="muecke_manage_categories"),
    url(r'^category/(?P<category_id>\d*)$', "manage_category", name="muecke_manage_category"),
    url(r'^category-by-id/(?P<category_id>\d*)$', "category_by_id", name="muecke_category_by_id"),
    url(r'^add-products/(?P<category_id>\d*)$', "add_products", name="muecke_manage_category_add_products"),
    url(r'^remove-products/(?P<category_id>\d*)$', "remove_products", name="muecke_manage_category_remove_products"),
    url(r'^add-top-category$', "add_category", name="muecke_manage_add_top_category"),
    url(r'^add-category/(?P<category_id>\d*)$', "add_category", name="muecke_manage_add_category"),
    url(r'^delete-category/(?P<id>[-\w]*)$', "delete_category", name="muecke_delete_category"),
    url(r'^products-inline/(?P<category_id>\d*)$', "products_inline", name="muecke_manage_category_products_inline"),
    url(r'^edit-category-data/(?P<category_id>\d*)$', "edit_category_data", name="muecke_manage_category_edit_data"),
    url(r'^edit-category-view/(?P<category_id>\d*)$', "category_view", name="muecke_manage_category_view"),
    url(r'^selected-products/(?P<category_id>\d*)$', "selected_products", name="muecke_selected_products"),
    url(r'^load-products-tab/(?P<category_id>\d*)$', "products_tab", name="muecke_load_products_tab"),
    url(r'^sort-categories$', "sort_categories", name="muecke_sort_categories"),
    url(r'^no-categories$', "no_categories", name="muecke_manage_no_categories"),
)

# Categories / SEO
urlpatterns += patterns('muecke.manage.categories.seo',
    url(r'^edit-category-seo/(?P<category_id>\d*)$', "edit_seo", name="muecke_manage_category_seo"),
)

# Customers
urlpatterns += patterns('muecke.manage.views.customer',
    url(r'^customers$', "customers", name="muecke_manage_customers"),
    url(r'^customers-inline$', "customers_inline", name="muecke_customers_inline"),
    url(r'^customer/(?P<customer_id>\d*)$', "customer", name="muecke_manage_customer"),
    url(r'^customer-inline/(?P<customer_id>\d*)$', "customer_inline", name="muecke_customer_inline"),
    url(r'^set-customer-filters$', "set_customer_filters", name="muecke_set_customer_filters"),
    url(r'^reset-customer-filters$', "reset_customer_filters", name="muecke_reset_customer_filters"),
    url(r'^set-customer-ordering/(?P<ordering>\w*)$', "set_ordering", name="muecke_set_customer_ordering"),
    url(r'^selectable-customers-inline$', "selectable_customers_inline", name="muecke_selectable_customers_inline"),
    url(r'^set-selectable-customers-page$', "set_selectable_customers_page", name="muecke_set_selectable_customers_page"),
    url(r'^set-customers-page$', "set_customers_page", name="muecke_set_customers_page"),
)

# # Export
# urlpatterns += patterns('muecke.manage.views.export',
#     url(r'^export-dispatcher$', "export_dispatcher", name="muecke_export_dispatcher"),
#     url(r'^export/(?P<export_id>\d*)$', "manage_export", name="muecke_export"),
#     url(r'^export-inline/(?P<export_id>\d*)/(?P<category_id>\d*)$', "export_inline", name="muecke_export_inline"),
#     url(r'^edit-category/(?P<export_id>\d*)/(?P<category_id>\d*)$', "edit_category", name="muecke_export_edit_category"),
#     url(r'^edit-product/(?P<export_id>\d*)/(?P<product_id>\d*)$', "edit_product", name="muecke_export_edit_product"),
#     url(r'^category-state/(?P<export_id>\d*)/(?P<category_id>\d*)$', "category_state", name="muecke_export_category_state"),
#     url(r'^update-export-data/(?P<export_id>\d*)$', "update_data", name="muecke_export_update_export_data"),
#     url(r'^add-export$', "add_export", name="muecke_export_add_export"),
#     url(r'^delete-export/(?P<export_id>\d*)$', "delete_export", name="muecke_export_delete_export"),
#     url(r'^export-export/(?P<slug>[-\w]*)$', "export", name="muecke_export_export"),
#     url(r'^update-category-variants-option/(?P<export_id>\d*)/(?P<category_id>\d*)$', "update_category_variants_option", name="muecke_export_update_category_variants_option"),
# )

# Shipping Methods
urlpatterns += patterns('muecke.manage.shipping_methods.views',
    url(r'^shipping$', "manage_shipping", name="muecke_manage_shipping"),
    url(r'^shipping-method/(?P<shipping_method_id>\d*)$', "manage_shipping_method", name="muecke_manage_shipping_method"),
    url(r'^add-shipping-method', "add_shipping_method", name="muecke_manage_add_shipping_method"),
    url(r'^save-shipping-data/(?P<shipping_method_id>\d*)$', "save_shipping_method_data", name="muecke_manage_save_shipping_method_data"),
    url(r'^delete-shipping-method/(?P<shipping_method_id>\d*)$', "delete_shipping_method", name="muecke_manage_delete_shipping_method"),
    url(r'^add-shipping-price/(?P<shipping_method_id>\d*)$', "add_shipping_price", name="muecke_manage_add_shipping_price"),
    url(r'^update-shipping-prices/(?P<shipping_method_id>\d*)$', "update_shipping_prices", name="muecke_manage_update_shipping_prices"),
    url(r'^shipping-price-criteria/(?P<shipping_price_id>\d*)$', "shipping_price_criteria", name="muecke_manage_shipping_price_criteria"),
    url(r'^save-shipping-price-criteria/(?P<shipping_price_id>\d*)$', "save_shipping_price_criteria", name="muecke_manage_save_shipping_price_criteria"),
    url(r'^save-shipping-method-criteria/(?P<shipping_method_id>\d*)$', "save_shipping_method_criteria", name="muecke_manage_save_shipping_method_criteria"),
    url(r'^sort-shipping-methods$', "sort_shipping_methods", name="muecke_sort_shipping_methods"),
    url(r'^no-shipping-methods$', "no_shipping_methods", name="muecke_manage_no_shipping_methods"),
)

# Discounts
urlpatterns += patterns('muecke.manage.discounts.views',
    url(r'^discounts$', "manage_discounts", name="muecke_manage_discounts"),
    url(r'^discount/(?P<id>\d*)$', "manage_discount", name="muecke_manage_discount"),
    url(r'^add-discount', "add_discount", name="muecke_manage_add_discount"),
    url(r'^save-discount-data/(?P<id>\d*)$', "save_discount_data", name="muecke_manage_save_discount_data"),
    url(r'^delete-discount/(?P<id>\d*)$', "delete_discount", name="muecke_manage_delete_discount"),
    url(r'^save-discount-criteria/(?P<id>\d*)$', "save_discount_criteria", name="muecke_manage_save_discount_criteria"),
    url(r'^no-discounts$', "no_discounts", name="muecke_manage_no_discounts"),
)

 # Pages
# urlpatterns += patterns('muecke.manage.pages.views',
#     url(r'^add-page$', "add_page", name="muecke_add_page"),
#     url(r'^delete-page/(?P<id>\d*)$', "delete_page", name="muecke_delete_page"),
#     url(r'^manage-pages$', "manage_pages", name="muecke_manage_pages"),
#     url(r'^manage-page/(?P<id>\d*)$', "manage_page", name="muecke_manage_page"),
#     url(r'^page-by-id/(?P<id>\d*)$', "page_view_by_id", name="muecke_page_view_by_id"),
#     url(r'^sort-pages$', "sort_pages", name="muecke_sort_pages"),
#     url(r'^save-page-data-tab/(?P<id>\d*)$', "save_data_tab", name="muecke_save_page_data_tab"),
#     url(r'^save-page-seo-tab/(?P<id>\d*)$', "save_seo_tab", name="muecke_save_page_seo_tab"),
# )

# Payment
urlpatterns += patterns('muecke.manage.views.payment',
    url(r'^payment$', "manage_payment", name="muecke_manage_payment"),
    url(r'^payment-method/(?P<payment_method_id>\d*)$', "manage_payment_method", name="muecke_manage_payment_method"),
    url(r'^add-payment-method', "add_payment_method", name="muecke_add_payment_method"),
    url(r'^save-payment-data/(?P<payment_method_id>\d*)$', "save_payment_method_data", name="muecke_manage_save_payment_method_data"),
    url(r'^delete-payment-method/(?P<payment_method_id>\d*)$', "delete_payment_method", name="muecke_delete_payment_method"),
    url(r'^add-payment-price/(?P<payment_method_id>\d*)$', "add_payment_price", name="muecke_manage_add_payment_price"),
    url(r'^update-payment-prices/(?P<payment_method_id>\d*)$', "update_payment_prices", name="muecke_manage_update_payment_prices"),
    url(r'^payment-price-criteria/(?P<payment_price_id>\d*)$', "payment_price_criteria", name="muecke_manage_payment_price_criteria"),
    url(r'^save-payment-price-criteria/(?P<payment_price_id>\d*)$', "save_payment_price_criteria", name="muecke_manage_save_payment_price_criteria"),
    url(r'^save-payment-method-criteria/(?P<payment_method_id>\d*)$', "save_payment_method_criteria", name="muecke_manage_save_payment_method_criteria"),
    url(r'^sort-payment-methods$', "sort_payment_methods", name="muecke_sort_payment_methods"),
)

# Orders
urlpatterns += patterns('muecke.manage.views.orders',
    url(r'^manage-orders$', "manage_orders", name="muecke_manage_orders"),
    url(r'^orders$', "orders_view", name="muecke_orders"),
    url(r'^orders-inline$', "orders_inline", name="muecke_orders_inline"),
    url(r'^order/(?P<order_id>\d*)$', "order_view", name="muecke_manage_order"),
    url(r'^delete-order/(?P<order_id>\d*)$', "delete_order", name="muecke_delete_order"),
    url(r'^send-order/(?P<order_id>\d*)$', "send_order", name="muecke_send_order"),
    url(r'^set-orders-filter$', "set_order_filters", name="muecke_set_order_filter"),
    url(r'^set-orders-filter-date$', "set_order_filters_date", name="muecke_set_order_filters_date"),
    url(r'^reset-order-filter$', "reset_order_filters", name="muecke_reset_order_filters"),
    url(r'^set-selectable-orders-page$', "set_selectable_orders_page", name="muecke_set_selectable_orders_page"),
    url(r'^set-orders-page$', "set_orders_page", name="muecke_set_orders_page"),
    url(r'^change-order-state$', "change_order_state", name="muecke_change_order_state"),
)

# Order numbers
urlpatterns += patterns('muecke.manage.views.shop',
    url(r'^save-order-numbers-tab$', "save_order_numbers_tab", name="muecke_save_order_numbers_tab"),
)

# Criteria
urlpatterns += patterns('muecke.manage.views.criteria',
    url(r'^add-criterion', "add_criterion", name="muecke_add_criterion"),
    url(r'^change-criterion', "change_criterion_form", name="muecke_manage_criteria_change_criterion_form"),
)

# # Static blocks
# urlpatterns += patterns('muecke.manage.static_blocks.views',
#     url(r'^add-static-block$', "add_static_block", name="muecke_manage_add_static_block"),
#     url(r'^delete-static-block/(?P<id>\d*)$', "delete_static_block", name="muecke_delete_static_block"),
#     url(r'^preview-static-block/(?P<id>\d*)$', "preview_static_block", name="muecke_preview_static_block"),
#     url(r'^static-blocks$', "manage_static_blocks", name="muecke_manage_static_blocks"),
#     url(r'^static-block/(?P<id>\d*)$', "manage_static_block", name="muecke_manage_static_block"),
#     url(r'^add_files/(?P<id>[-\w]*)', "add_files", name="muecke_add_files_to_static_block"),
#     url(r'^update_files/(?P<id>[-\w]*)', "update_files", name="muecke_manage_update_files_sb"),
#     url(r'^reload_files/(?P<id>[-\w]*)', "reload_files", name="muecke_reload_files"),
#     url(r'^sort-static-blocks$', "sort_static_blocks", name="muecke_sort_static_blocks"),
#     url(r'^no-static-blocks$', "no_static_blocks", name="muecke_manage_no_static_blocks"),
# )


# Reviews
urlpatterns += patterns('muecke.manage.views.review',
    url(r'^reviews$', "reviews", name="muecke_manage_reviews"),
    url(r'^review/(?P<review_id>\d*)$', "review", name="muecke_manage_review"),
    url(r'^set-review-filters$', "set_review_filters", name="muecke_set_review_filters"),
    url(r'^reset-review-filters$', "reset_review_filters", name="muecke_reset_review_filters"),
    url(r'^set-review-ordering/(?P<ordering>\w*)$', "set_ordering", name="muecke_set_review_ordering"),
    url(r'^set-review-state/(?P<review_id>\d*)$', "set_review_state", name="muecke_set_review_state"),
    url(r'^delete-review/(?P<review_id>\d*)$', "delete_review", name="muecke_delete_review"),
    url(r'^set-reviews-page$', "set_reviews_page", name="muecke_set_reviews_page"),
    url(r'^set-selectable-reviews-page$', "set_selectable_reviews_page", name="muecke_set_selectable_reviews_page"),
)

# Shop
urlpatterns += patterns('muecke.manage.views.shop',
    url(r'^shop$', "manage_shop", name="muecke_manage_shop"),
    url(r'^save-shop-data-tab$', "save_data_tab", name="muecke_save_shop_data_tab"),
    url(r'^save-shop-default-values-tab$', "save_default_values_tab", name="muecke_save_shop_default_values_tab"),
    url(r'^save-shop-seo-tab$', "save_seo_tab", name="muecke_save_shop_seo_tab"),
)

 # Actions
# urlpatterns += patterns('muecke.manage.actions.views',
#     url(r'^actions$', "manage_actions", name="muecke_manage_actions"),
#     url(r'^action/(?P<id>\d*)$', "manage_action", name="muecke_manage_action"),
#     url(r'^no-actions$', "no_actions", name="muecke_no_actions"),
#     url(r'^add-action$', "add_action", name="muecke_add_action"),
#     url(r'^delete-action/(?P<id>\d*)$', "delete_action", name="muecke_delete_action"),
#     url(r'^save-action/(?P<id>\d*)$', "save_action", name="muecke_save_action"),
#     url(r'^sort-actions$', "sort_actions", name="muecke_sort_actions"),
# )

# Prodcut Taxes
urlpatterns += patterns('muecke.manage.product_taxes.views',
    url(r'^add-product-tax$', "add_tax", name="muecke_manage_add_tax"),
    url(r'^delete-product-tax/(?P<id>\d*)$', "delete_tax", name="muecke_delete_tax"),
    url(r'^product-taxes$', "manage_taxes", name="muecke_manage_taxes"),
    url(r'^product-tax/(?P<id>\d*)$', "manage_tax", name="muecke_manage_tax"),
    url(r'^no-product-taxes$', "no_taxes", name="muecke_manage_no_taxes"),
)

# Customer tax
urlpatterns += patterns('muecke.manage.customer_tax.views',
    url(r'^add-customer-tax$', "add_customer_tax", name="muecke_add_customer_tax"),
    url(r'^delete-customer-tax/(?P<id>\d*)$', "delete_customer_tax", name="muecke_delete_customer_tax"),
    url(r'^customer-taxes$', "manage_customer_taxes", name="muecke_manage_customer_taxes"),
    url(r'^customer-tax/(?P<id>\d*)$', "manage_customer_tax", name="muecke_manage_customer_tax"),
    url(r'^no-customer-taxes$', "no_customer_taxes", name="muecke_manage_no_customer_taxes"),
)

# # Utils
# urlpatterns += patterns('muecke.manage.views.utils',
#     url(r'^utilities$', "utilities", name="muecke_manage_utils"),
#     url(r'^clear-cache$', "clear_cache", name="muecke_clear_cache"),
#     url(r'^set-category-levels$', "set_category_levels", name="muecke_set_category_levels"),
#     url(r'^update-effective-price$', "update_effective_price", name="muecke_update_effective_price"),
#     url(r'^reindex-topseller$', "reindex_topseller", name="muecke_reindex_topseller"),
# )
