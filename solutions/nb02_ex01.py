order_totals = (
    orders.join(items, "item")
    .group_by("id")
    .agg(total=(_["price"] * _["count"]).sum())
)

order_totals
