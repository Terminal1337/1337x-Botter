from capmonster_python import ImageToTextTask

capmonster = ImageToTextTask("your_api_key")


def return_string(path):
    task_id = capmonster.create_task(image_path=path)
    result = capmonster.join_task_result(task_id)
    return result.get("text")