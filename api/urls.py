from django.urls import path

from . import views

urlpatterns = [
    path("register_customer/",views.register_customer),
    path("search_customer/",views.SearchCustomers.as_view()),
    path("customer_details/<int:pk>/",views.customer_details),
    path("customer_details_by_phone/<str:phone>/",views.customer_details_by_phone),
    path("customer_details_by_name/<str:name>/",views.customer_details_by_name),
    path("get_user_customers/",views.get_user_customers),
    path("get_my_customers/",views.get_my_customers),
    path("get_all_customers/",views.get_all_customers),
    path("update_customer/<int:pk>/",views.update_customer),
    path("customer_delete/<int:pk>/",views.customer_delete),
    #
    path("register_customer_accounts/",views.register_customer_accounts),
    path("search_customer_accounts/",views.SearchCustomersAccounts.as_view()),
    path("customer_accounts_details/<int:pk>/",views.customer_accounts_details),
    path("customer_accounts_details_by_account_number/<str:account_number>/",views.customer_accounts_details_by_account_number),
    path("customer_account_details_by_account_name/<str:account_name>/",views.customer_account_details_by_account_name),
    path("update_customer_accounts/<int:pk>/",views.update_customer_accounts),
    path("customer_account_delete/<int:pk>/",views.customer_account_delete),
    #
    path("post_bank_deposit/",views.post_bank_deposit),
    path("search_bank_deposit/",views.SearchBankDeposit.as_view()),
    path("bank_details/<int:pk>/",views.bank_details),
    path("get_user_bank_deposits/<str:username>/",views.get_user_bank_deposits),
    path("get_all_bank_deposits/",views.get_all_bank_deposits),
    path("get_my_bank_deposits/",views.get_my_bank_deposits),
    path("get_customer_bank_deposits/<int:pk>/",views.get_customer_bank_deposits),


    path("post_momo_deposit/",views.post_momo_deposit),
    path("search_momo_deposit/",views.SearchMomoDeposit.as_view()),
    path("momo_deposit_details/<int:pk>/",views.momo_deposit_details),
    path("get_user_momo_deposits/<str:username>/",views.get_user_momo_deposits),
    path("get_all_momo_deposits/",views.get_all_momo_deposits),
    path("get_my_momo_deposits/",views.get_my_momo_deposits),
    path("get_customer_momo_deposits/<int:pk>/",views.get_customer_momo_deposits),


    path("post_momo_withdrawal/",views.post_momo_withdrawal),
    path("search_momo_withdrawal/",views.SearchMomoWithdrawal.as_view()),
    path("momo_withdrawal_details/<int:pk>/",views.momo_withdrawal_details),
    path("get_user_momo_withdrawals/<str:username>/",views.get_user_momo_withdrawals),
    path("get_all_momo_withdraws/",views.get_all_momo_withdraws),
    path("get_my_momo_withdraws/",views.get_my_momo_withdraws),
    path("get_customer_momo_withdrawals/<int:pk>/",views.get_customer_momo_withdrawals),


    path("post_bank_withdrawal/",views.post_bank_withdrawal),
    path("search_bank_withdrawal/",views.SearchBankWithdrawal.as_view()),
    path("bank_withdrawal_details/<int:pk>/",views.bank_withdrawal_details),
    path("get_user_bank_withdrawals/<str:username>/",views.get_user_bank_withdrawals),
    path("get_all_bank_withdrawals/",views.get_all_bank_withdrawals),
    path("get_my_bank_withdrawals/",views.get_my_bank_withdrawals),
    path("get_customer_bank_withdrawals/<int:pk>/",views.get_customer_bank_withdrawals),


    path("post_report/",views.post_report),
    path("report_detail/<int:id>/",views.report_detail),
    path("get_user_reports/<str:username>/",views.get_user_reports),
    path("get_all_reports/",views.get_all_reports),
    path("get_my_reports/",views.get_my_reports),


    path("add_to_blocked_lists/",views.add_to_blocked_lists),
    path("get_all_blocked/",views.get_all_blocked),


    path("add_to_fraud_lists/",views.add_to_fraud_lists),
    path("fraud_detail/<int:pk>/",views.fraud_detail),
    path("get_all_fraudsters/",views.get_all_fraudsters),
    path("get_my_fraud_lists/",views.get_my_fraud_lists),
    path("search_fraudsters/",views.SearchFraudsters.as_view()),


    path("post_payment_for_re_balancing/",views.post_payment_for_re_balancing),
    path("search_payment/",views.SearchPaymentForReBalancing.as_view()),
    path("payment_details/<int:pk>/",views.payment_details),
    path("get_user_payments/<str:username>/",views.get_user_payments),
    path("get_all_payments/",views.get_all_payments),
    path("get_my_payments/",views.get_my_payments),


    path("request_for_re_balancing/",views.request_for_re_balancing),
    path("re_balancing_details/<int:id>/",views.re_balancing_details),
    path("get_user_re_balancing_requests/<str:username>/",views.get_user_re_balancing_requests),
    path("get_all_re_balancing/",views.get_all_re_balancing),
    path("get_my_re_balancing_requests/",views.get_my_re_balancing_requests),


    path("authenticate_phone/",views.authenticate_phone),
    path("authenticated_phone_details/<int:pk>/",views.authenticated_phone_details),
    path("get_all_authenticated_phones/",views.get_all_authenticated_phones),
    path("get_my_authenticated_phone_details/",views.get_my_authenticated_phone_details),


    path("register_agents_accounts/",views.register_agents_accounts),
    path("agent_accounts_details/<int:pk>/",views.agent_accounts_details),
    path("agent_accounts_details_by_account_number/<str:account_number>/",views.agent_accounts_details_by_account_number),
    path("agent_account_details_by_account_name/<str:account_name>/",views.agent_account_details_by_account_name),
    path("update_agents_accounts/<int:pk>/",views.update_agents_accounts),
    path("agent_account_delete/<int:pk>/",views.agent_account_delete),
    path("get_my_accounts/",views.get_my_accounts),


    path("get_my_notifications/",views.get_my_notifications),
    path("get_my_unread_notifications/",views.get_my_unread_notifications),
    path("read_notification/",views.read_notification),


    path("request_float/",views.request_float),
    path("float_details/<int:pk>/",views.float_details),
    path("get_user_float_requests/<str:username>/",views.get_user_float_requests),
    path("get_all_floats/",views.get_all_floats),
    path("get_my_float_requests/",views.get_my_float_requests),

    path("get_all_my_agents/", views.get_all_my_agents)
]