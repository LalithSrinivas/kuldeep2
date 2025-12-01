Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    map = Task(
        task_id = "map", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "map", "sourceType" : "Seed", "alias" : ""}
    )
    amk__Reformat_1 = Task(task_id = "amk__Reformat_1", component = "Model", modelName = "amk__Reformat_1")
    map.out >> amk__Reformat_1.in_0
