from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import RedirectView

from example import views


urlpatterns = [
    path("", RedirectView.as_view(url="/categories/"), name="home"),
    path("admin/", admin.site.urls),
    # TODO: Do not show login for authenticated user.
    path("login/", LoginView.as_view(), name="login"),
    path(
        "logout/",
        login_required(LogoutView.as_view(template_name="registration/logout.html")),
        name="logout",
    ),
    # TODO: Do not show sign up for authenticated user.
    path("sign_up/", views.SignUpView.as_view(), name="sign-up"),
    path("profile/", login_required(views.ProfileView.as_view()), name="profile"),
    path(
        "notifications/",
        login_required(views.NotificationListView.as_view()),
        name="notification-list",
    ),
    path(
        "categories/",
        login_required(views.CategoryListView.as_view()),
        name="category-list",
    ),
    path(
        "categories/<int:id>/",
        login_required(views.CategoryDetailView.as_view()),
        name="category-detail",
    ),
    path(
        "shop/", login_required(views.CategoryShopView.as_view()), name="category-shop"
    ),
    path(
        "subscribe/<int:id>/",
        login_required(views.BuySubscriptionView.as_view()),
        name="buy-subscription",
    ),
    path("put_money/", login_required(views.PutMoneyView.as_view()), name="put-money"),
]