import json


def compare_jsons(json_old, json_new, diff_list):
    result = {}

    def compare_nested(old, new, path):
        for key in old:
            if key in new:
                current_path = path + [key]
                if isinstance(old[key], dict) and isinstance(new[key], dict):
                    compare_nested(old[key], new[key], current_path)
                elif old[key] != new[key]:
                    full_path = ".".join(current_path)
                    if len(current_path) > 2:
                        if current_path[-2] in diff_list:
                            result[full_path] = new[key]
                    else:
                        if current_path[-1] in diff_list:
                            result[full_path] = new[key]

    compare_nested(json_old, json_new, [])
    return result


json_old = {
    "company_id": 111111,
    "resource": "record",
    "resource_id": 406155061,
    "status": "create",
    "data": {
        "id": 11111111,
        "company_id": 111111,
        "services": [
            {
                "id": 9035445,
                "title": "Стрижка",
                "cost": 1500,
                "cost_per_unit": 1500,
                "first_cost": 1500,
                "amount": 1,
            }
        ],
        "goods_transactions": [],
        "staff": {"id": 1819441, "name": "Мастер"},
        "client": {
            "id": 130345867,
            "name": "Клиент",
            "phone": "79111111111",
            "success_visits_count": 2,
            "fail_visits_count": 0,
        },
        "clients_count": 1,
        "datetime": "2022-01-25T11:00:00+03:00",
        "create_date": "2022-01-22T00:54:00+03:00",
        "online": False,
        "attendance": 0,
        "confirmed": 1,
        "seance_length": 3600,
        "length": 3600,
        "master_request": 1,
        "visit_id": 346427049,
        "created_user_id": 10573443,
        "deleted": False,
        "paid_full": 0,
        "last_change_date": "2022-01-22T00:54:00+03:00",
        "record_labels": "",
        "date": "2022-01-22 10:00:00",
    },
}
json_new = {
    "company_id": 111111,
    "resource": "record",
    "resource_id": 406155061,
    "status": "update",
    "data": {
        "id": 11111111,
        "company_id": 111111,
        "services": [
            {
                "id": 22222225,
                "title": "Стрижка",
                "cost": 1500,
                "cost_per_unit": 1500,
                "first_cost": 1500,
                "amount": 1,
            }
        ],
        "goods_transactions": [],
        "staff": {"id": 1819441, "name": "Маргарита"},
        "client": {
            "id": 130345867,
            "name": "Клиент",
            "phone": "79111111111",
            "success_visits_count": 2,
            "fail_visits_count": 0,
        },
        "clients_count": 1,
        "datetime": "2022-01-25T13:00:00+03:00",
        "create_date": "2022-01-22T00:54:00+03:00",
        "online": False,
        "attendance": 2,
        "confirmed": 1,
        "seance_length": 3600,
        "length": 3600,
        "master_request": 1,
        "visit_id": 346427049,
        "created_user_id": 10573443,
        "deleted": False,
        "paid_full": 1,
        "last_change_date": "2022-01-22T00:54:00+03:00",
        "record_labels": "",
        "date": "2022-01-22 10:00:00",
    },
}
diff_list = ["services", "staff", "datetime", "status"]

result = compare_jsons(json_old, json_new, diff_list)
print(json.dumps(result, indent=2, ensure_ascii=False))
