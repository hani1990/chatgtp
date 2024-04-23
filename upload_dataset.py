# -*- coding: utf-8 -*-
from common import get_openai_client

client = get_openai_client()

ret = client.files.create(
    file=open("./data/fine_tuning.jsonl", "rb"),
    purpose="fine-tune"
)
# file.id要复制下来，下一步开始微调要用  file-ykHHL7SAjEaoVM81tEGXyg2x
print(ret.id)
print(client.with_raw_response)