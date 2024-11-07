from src.sheet import Bonus


def bonus_template(bonus: Bonus) -> str:
    temp: str = (
        f"✅\t<i>{bonus.username}</i>\n"
        f"<b>KPI</b>: {bonus.kpi}\n"
        f"<b>Всего</b>: <code>{bonus.amount}</code>\n\n"
    )
    if bonus.bonuses:
        # max_len: int = max(len(bonus.name) for bonus in bonus.bonuses) + 8  # tags
        temp += "\n".join(
            f"<b>{bonus.name + '</b>:'}\t\t\t{bonus.bonus}" for bonus in bonus.bonuses
        )
    return temp
