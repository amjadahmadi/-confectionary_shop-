from .models import Order_Item
from customer.models import User


def back_money(order: Order_Item, user: User):
    money = list(map(lambda val: (val.total_price, str(val.stock_id)) if val.order_status == 'CA' else (0, 0), order))
    sum_back_money = sum(_ for _, i in money)
    if sum_back_money:
        user = User.objects.select_related('bank_account').get(id=user)
        bank_account = user.bank_account
        bank_account.balance += sum_back_money
        bank_account.save()
        return money
    return False
