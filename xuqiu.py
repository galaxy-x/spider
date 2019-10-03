#登录
login_template = {
    "action":"login",
    "user":"bobby1"
}
#给某个用户发送消息
send_data_template = {
    "action":"send_msg",
    "to":"user",
    "from":"user",
    "data":"i am bobby"
}
#历史消息
offline_msg_template = {
    "action":"history_msg",
    "user":"user",
}
#获取在线用户
get_user_template = {
    "action":"list_user"
}

#退出
exit_template = {
    "action":"exit",
    "user":""
}