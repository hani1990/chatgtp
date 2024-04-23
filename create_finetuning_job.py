from common import get_openai_client
client = get_openai_client()
#
# ret = client.fine_tuning.jobs.create(
#   training_file="file-ykHHL7SAjEaoVM81tEGXyg2x",
#   model="gpt-3.5-turbo"
# )
# """
# FineTuningJob(id='ftjob-OiE0LTIWObJxkv8sTcUyXFxy', created_at=1713845484, error=Error(code=None, message=None, param=None, error=None), fine_tuned_model=None, finished_at=None, hyperparameters=Hyperparameters(n_epochs='auto', batch_size='auto', learning_rate_multiplier='auto'), model='gpt-3.5-turbo-0125', object='fine_tuning.job', organization_id='org-YykWIC6Q2rzbQ2AhDTvBPpzS', result_files=[], seed=340474157, status='validating_files', trained_tokens=None, training_file='file-ykHHL7SAjEaoVM81tEGXyg2x', validation_file=None, integrations=[], user_provided_suffix=None)
#
# """
# print(ret)

# List 10 fine-tuning jobs
# ret_job_list = client.fine_tuning.jobs.list(limit=10)
# print(ret_job_list)
# Retrieve the state of a fine-tune
ret_job = client.fine_tuning.jobs.retrieve("ftjob-OiE0LTIWObJxkv8sTcUyXFxy")
print("模型名称:{} 模型状态:{}".format(ret_job.fine_tuned_model, ret_job.status) )
