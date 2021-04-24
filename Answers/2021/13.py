def get_table(lines):
  return [input().split(",") for _ in range(lines)]

def get_table_ids(table):
  return [col[0] for col in table]

for _ in range(int(input())):
  w, t, p = map(int, input().split())
  work_order_table = get_table(w)
  work_task_table = get_table(t)
  part_table = get_table(p)

  work_order_ids = get_table_ids(work_order_table)
  part_ids = get_table_ids(part_table)

  for id, work_order_id, part_id, assigned_to in work_task_table:
    data = [str(id)]

    if work_order_id not in work_order_ids:
      data.append(f"MISSING WORK_ORDER {work_order_id}")
    if part_id not in part_ids:
      data.append(f"MISSING PART {part_id}")

    if len(data) > 1:
      print(" ".join(data))