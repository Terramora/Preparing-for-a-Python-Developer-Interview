from typing import Optional

from task_4 import get_percent


def deposit(amount: int, months: int, contribution: int) -> Optional[float]:
    def contribution_profit(percent: float, months: int, contribution: int):
        sum_contribution = 0
        percent_for_month = percent / 12
        for i in range(months - 2):
            sum_contribution += contribution
            sum_contribution += sum_contribution / 100 * percent_for_month

        return sum_contribution

    if months not in [6, 12, 24]:
        print(f'The deposit is unavailable for {months} months')
    else:
        percent = get_percent(amount, months)
        if not percent:
            print('rate not detected')

        total = amount
        for month in range(months):
            profit = total * percent / 100 / 12
            total += profit

        return total + contribution_profit(percent, months, contribution)


print(deposit(1000000, 24, 200))

