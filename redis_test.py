from flask import Flask, request, jsonify
import redis
import json
from datetime import datetime

conn = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

print ('Set Record:', conn.set("hello_redis", "헬로우 Redis"))
print ('Get Record:', conn.get("hello_redis"))

test_dict = {
"APV_CD":"0000",
"APV_MSG":"SUCCESS",
"attachFileInfo":[
    {
        "fileid":"B122",
        "type":"body",
        "extention":"pdf",
        "filename":"IT실 소모품구매.pdf",
        "savedname":"1145.pdf",
        "filepath":"/DATA/UFLOW/gwstorage/e-sign/Approval/FlowBody/20200910/1145.pdf",
        "target_fileid":"B122",
        "target_filepath":"/DATA/FFACT/NACCT/NACCT/attachfile/AM/GW/20200910/1145.pdf"
    },
    {
        "fileid":"F123",
        "type":"file",
        "extention":"xlsx",
        "filename":"인터페이스정의서.xlsx",
        "savedname":"20200910_인터페이스정의서.xlsx",
        "filepath":"/DATA/UFLOW/gwstorage/e-sign/Approval/Attach/20200910/20200910_인터페이스정의서.xlsx",
        "target_fileid":"F123",
        "target_filepath":"/DATA/FFACT/NACCT/NACCT/attachfile/AM/GW/20200910/20200910_인터페이스정의서.xlsx"
    },
    {
        "fileid":"F124",
        "type":"file",
        "extention":"ppt",
        "filename":"테이블정의서.ppt",
        "savedname":"20200910_테이블정의서.ppt",
        "filepath":"/DATA/UFLOW/gwstorage/e-sign/Approval/Attach/20200910/20200910_테이블정의서.ppt",
        "target_fileid":"F124",
        "target_filepath":"/DATA/FFACT/NACCT/NACCT/attachfile/AM/GW/20200910/20200910_테이블정의서.ppt"
    }
    ]
}

# key생성
save_key = "my_sp_list_"+datetime.today().strftime('%Y%m%d')

# set
json_test_dict = json.dumps(test_dict)
conn.set(save_key, json_test_dict)

# get
json_test_dict = conn.get(save_key)
test_dict2 = dict(json.loads(json_test_dict))
print(test_dict2)