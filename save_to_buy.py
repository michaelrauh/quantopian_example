def initialize(context):
    context.stocks = (sid(8554))
    context.current_time = 0
    context.spent = 0

    schedule_function(
    func=rebalance,
    date_rule=date_rules.every_day(),
    time_rule=time_rules.market_open(),
  )

def rebalance(context, data):
    all_money = 1000000
    all_time = 1500
    context.current_time += 1
    allotment = (all_money/(all_time) * context.current_time) - context.spent

    low_history = data.history(sid(8554),'price',252,'1d')
    low = min(low_history[:-1])
    price = low_history[0]

    if price <= low:
        log.info("BUYING: " + str(allotment))
        order_value(sid(8554), allotment)
        context.spent += allotment


def handle_data(context, data):
    pass
