from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout,name='admin_logout'),
    path('dashboard/', views.admin_dashboard,name='admin_dashboard'),
    path('manage_category/', views.manage_category,name='manage_category'),
    path('create_category/', views.create_category,name='create_category'),
    path('edit_category/<int:id>/',views.edit_category,name='edit_category'),
    path('delete_category/<int:id>/', views.delete_category,name='delete_category'),
    path('manage_products/',views.manage_products,name='manage_products'),
    path('view_products/',views.view_products,name='view_product'),
    path('create_product/',views.create_product,name='create_product'),
    path('edit_product/<int:id>/',views.edit_product,name='edit_product'),
    path('delete_product/<int:id>/', views.delete_product,name='delete_product'),
    path('manage_customers/',views.manage_customers,name='manage_customer'),
    path('create_customer/', views.create_customer,name='create_customer'),
    path('view_customer/<int:id>/',views.view_customers,name='view_customer'),
    path('update_customer/<int:id>/', views.update_customers,name='update_customer'),
    path('delete_customer/<int:id>/', views.delete_customer,name='delete_customer'),
    path('activate_customer/<int:id>/',views.activate_customer,name='activate_customer'),
    path('block_customer/<int:id>/', views.block_customer,name='block_customer'),
    path('manage_orders/',views.manage_orders,name='manage_orders'),
    path('manage_refund/',views.manage_refund,name='manage_refund'),
    path('manage_order_items/<int:id>/',views.manage_order_items,name='manage_order_items'),
    path('pending_order/<int:id>/<str:value>/', views.pending_order,name='pending_order'),
    path('complete_order/<int:id>/<str:value>/', views.complete_order,name='complete_order'),
    path('canceled_order/<int:id>/<str:value>/', views.cancel_order,name='canceled_order'),
    path('reports/', views.report,name='report'),
    path('sales_report/', views.sales_report,name='sales_report'),
    path('cancel_report/', views.cancel_report,name='cancel_report'),
    path('product_return_report/',views.product_return_report,name='product_return_report'),
    path('manage_offer/', views.manage_offer,name='manage_offer'),
    path('create_offer/', views.create_offer, name='create_offer'),
    path('delete_offer/<int:id>/',views.delete_offer,name='delete_offer'),
    path('manage_coupens/',views.manage_coupens,name='manage_coupens'),
    path('create_coupen/',views.create_coupen,name='create_coupen'),
    path('edit_coupen/<int:id>/',views.edit_coupen,name='edit_coupen'),
    path('delete_coupen/<int:id>/', views.delete_coupen,name='delete_coupen'),
    path('refunds/<int:id>/<str:value>/',views.manage_refund_options,name='refund_options'),
    ]