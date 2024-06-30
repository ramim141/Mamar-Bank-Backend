from django.urls import path
from .views import DepositMoneyView,WithdrawMoneyView,TransactionReportView,LoanRequestView,LoanListView,PayLoanView,TransferMoneyView


urlpatterns = [
    path('deposit/',DepositMoneyView.as_view(),name='deposit_money'),
    path('withdraw/',WithdrawMoneyView.as_view(),name='withdraw_money'),
    path('report/',TransactionReportView.as_view(),name='transaction_report'),
    path('loan_request/',LoanRequestView.as_view(),name='loan_request'),
    path('loans/',LoanListView.as_view(),name='loan_list'),
    path('loan/<int:loan_id>',PayLoanView.as_view(),name='pay_loan'),
    path('transfer/',TransferMoneyView.as_view(),name='transfer_money'),
]
