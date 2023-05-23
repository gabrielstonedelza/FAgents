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
    path("delete_report/<int:id>/",views.delete_report),
    path("get_user_reports/<str:username>/",views.get_user_reports),
    path("get_all_reports/",views.get_all_reports),
    path("get_reports_today/",views.get_reports_today),
    path("get_my_reports/",views.get_my_reports),


    path("add_to_blocked_lists/",views.add_to_blocked_lists),
    path("get_all_blocked/",views.get_all_blocked),
    path("remove_from_blocked/<int:id>/",views.remove_from_blocked),


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

    # rebalancing
    path("request_for_re_balancing/",views.request_for_re_balancing),
    path("re_balancing_details/<int:id>/",views.re_balancing_details),
    path("delete_agent_rebalancing/<int:id>/",views.delete_agent_rebalancing),
    path("update_agent_rebalancing/<int:pk>/",views.update_agent_rebalancing),
    path("get_user_re_balancing_requests/<str:username>/",views.get_user_re_balancing_requests),
    path("get_unapproved_re_balancing_requests/",views.get_unapproved_re_balancing_requests),
    path("get_all_re_balancing/",views.get_all_re_balancing),
    path("get_my_re_balancing_requests/",views.get_my_re_balancing_requests),


    path("register_agents_accounts/",views.register_agents_accounts),
    path("agent_accounts_details/<int:pk>/",views.agent_accounts_details),
    path("agent_accounts_details_by_account_number/<str:account_number>/",views.agent_accounts_details_by_account_number),
    path("agent_account_details_by_account_name/<str:account_name>/",views.agent_account_details_by_account_name),
    path("update_agents_accounts/<int:pk>/",views.update_agents_accounts),
    path("agent_account_delete/<int:pk>/",views.agent_account_delete),
    path("get_my_accounts/",views.get_my_accounts),
    path("get_all_my_agents_accounts/",views.get_all_my_agents_accounts),


    path("get_my_notifications/",views.get_my_notifications),
    path("get_my_unread_notifications/",views.get_my_unread_notifications),
    path("read_notification/",views.read_notification),
    path("un_trigger_notification/<int:id>/",views.un_trigger_notification),
    path("get_triggered_notifications/",views.get_triggered_notifications),


    path("request_float/",views.request_float),
    path("float_details/<int:pk>/",views.float_details),
    path("get_user_float_requests/<str:username>/",views.get_user_float_requests),
    path("get_all_floats/",views.get_all_floats),
    path("get_my_float_requests/",views.get_my_float_requests),

    path("get_all_my_agents/<str:owner>/", views.get_all_my_agents),

# private and group messages
    path("private_message_detail/<str:private_chat_id>/", views.private_message_detail),
    path("get_private_message/<int:user1>/<int:user2>/", views.get_private_message),
    path("send_private_message/", views.send_private_message),
    path("get_all_group_message/", views.get_all_group_message),
    path("send_group_message/", views.send_group_message),

#     agent pre registration
    path("add_agent_pre_reg/",views.add_agent_pre_reg),
    path("get_agents_pre_registrations/",views.get_agents_pre_registrations),


#     new customer accounts urls
    path("get_customer_account/<str:customer>/", views.get_customer_account),
    path("get_customer_accounts_by_bank/<str:customer_phone>/<str:bank>/", views.get_customer_accounts_by_bank),
    path("get_customer_by_phone/<str:customer>/", views.get_customer_by_phone),

#     requests to join float
    path("request_to_join_float/",views.request_to_join_float),
    path("get_request_to_join_float/",views.get_request_to_join_float),
    path("get_my_request_to_join_float/",views.get_my_request_to_join_float),

#     agent account started and closed
    path("add_balance_to_start/",views.add_balance_to_start),
    path("update_balance_to_start/<int:pk>/",views.update_balance_to_start),
    path("get_my_account_balance_started/",views.get_my_account_balance_started),
    path("get_my_account_balance_started_today/",views.get_my_account_balance_started_today),
    path("close_balance/",views.close_balance),
    path("get_my_account_balance_closed/",views.get_my_account_balance_closed),
    path("get_my_account_balance_closed_today/",views.get_my_account_balance_closed_today),

#     authenticate phone
    path("authenticate_agent_phone/",views.authenticate_agent_phone),
    path("get_all_auth_phones/",views.get_all_auth_phones),
    path("get_all_auth_phone_agent_username/<str:username>/",views.get_all_auth_phone_agent_username),
    path("delete_auth_phone/<int:id>/",views.delete_auth_phone),

    # free trial and monthly payments
    path("update_free_trial/<int:pk>/",views.update_free_trial),
    path("start_free_trial/",views.start_free_trial),
    path("get_my_free_trial/",views.get_my_free_trial),
    path("get_all_free_trials/",views.get_all_free_trials),
    path("make_monthly_payment/",views.make_monthly_payment),
    path("get_my_monthly_payment_status/",views.get_my_monthly_payment_status),
    path("get_all_monthly_payment_status/",views.get_all_monthly_payment_status),
    path("end_trial/",views.end_trial),
    path("end_monthly_payment/",views.end_monthly_payment),

#     mtn pay to
    path("add_pay_to/", views.add_pay_to),
    path("get_all_pay_to/", views.get_all_pay_to),
    path("get_all_my_pay_to/", views.get_all_my_pay_to),

#     agents detail transactions
    path("get_agents_customers/<str:username>/", views.get_agents_customers),
    path("get_agents_bank_deposits/<str:username>/", views.get_agents_bank_deposits),
    path("get_agents_bank_withdrawals/<str:username>/", views.get_agents_bank_withdrawals),
    path("get_agents_momo_deposits/<str:username>/", views.get_agents_momo_deposits),
    path("get_agents_momo_withdrawals/<str:username>/", views.get_agents_momo_withdrawals),
    path("get_agents_momo_pay_to/<str:username>/", views.get_agents_momo_pay_to),
    path("get_agents_request_username/<str:username>/", views.get_agents_request_username),
    path("get_agents_reports/<str:username>/", views.get_agents_reports),
    # agent requests
    path("agent_request_from_owner/",views.agent_request_from_owner),
    path("get_all_my_agents_requests/",views.get_all_my_agents_requests),
    path("get_all_my_requests/",views.get_all_my_requests),
    path("get_unapproved_requests/",views.get_unapproved_requests),
    path("get_unpaid_requests/",views.get_unpaid_requests),
    path("get_all_my_requests_today/",views.get_all_my_requests_today),
    path("update_agent_request/<int:pk>/",views.update_agent_request),
    path("delete_agent_request/<int:id>/",views.delete_agent_request),
    path("request_detail/<int:pk>/",views.request_detail),

# agent request limit
    path("add_agent_request_limit/",views.add_agent_request_limit),
    path("get_all_my_agents_request_limits/",views.get_all_my_agents_request_limits),
    path("get_all_my_request_limit/",views.get_all_my_request_limit),
    path("update_agent_request_limit/<int:pk>/",views.update_agent_request_limit),

#     meetings
    path("admin_set_up_meeting/",views.admin_set_up_meeting),
    path("get_all_meetings/",views.get_all_meetings),

#    complains
    path("add_complain/",views.add_complain),
    path("get_all_complains/",views.get_all_complains),
    path("get_all_my_complains/",views.get_all_my_complains),
#     request to hold accounts

    path("request_to_hold_account/",views.request_to_hold_account),
    path("get_all_request_to_hold_account/",views.get_all_request_to_hold_account),
    path("get_all_my_request_to_hold_account/",views.get_all_my_request_to_hold_account),

#     request payments
    path("make_request_payment/",views.make_request_payment),
    path("get_all_my_agents_payment_requests/",views.get_all_my_agents_payment_requests),
    path("get_all_my_payment_requests/",views.get_all_my_payment_requests),
    path("get_unapproved_payment_requests/",views.get_unapproved_payment_requests),
    path("get_all_my_payment_requests_today/",views.get_all_my_payment_requests_today),
    path("update_agent_payment_request/<int:pk>/",views.update_agent_payment_request),
    path("delete_agent_payment_request/<int:id>/",views.delete_agent_payment_request),
    path("get_agents_payment_request_username/<str:username>/",views.get_agents_payment_request_username),
    path("payment_request_detail/<int:pk>/",views.payment_request_detail),

#     approvals
    path("add_to_approve_request_payment/",views.add_to_approve_request_payment),
    path("add_to_approve_request/",views.add_to_approve_request_payment),
    path("add_to_approve_request_rebalancing/",views.add_to_approve_request_rebalancing),

#     owners and agents messages
    path("send_owners_group_message/",views.send_owners_group_message),
    path("get_owners_group_messages/",views.get_owners_group_messages),
    path("send_agents_group_message/",views.send_agents_group_message),
    path("get_agents_group_messages/<str:owner>/",views.get_agents_group_messages),
]