from flask import Flask, request, g, Response
from flask_cors import CORS
from flask import Flask
import random

app = Flask(__name__)

CORS(app)

players = []
dead_players = []
status = "init"
room_players = []

# 狼人杀人 werewolf 0


def werewolf_action(kill=1):
    global dead_players
    if kill == -1:
        print("狼人不杀人", players)
        return
    else:
        dead_players.append(kill)
        print("狼人杀人", dead_players)


# 女巫救人 witch 1
def witch_action(to_number):
    global dead_players
    # 999不操作
    if to_number == 999:
        return
    # 救人
    if to_number == 666:
        dead_players = []
        print("女巫救人", dead_players)
        return
    dead_players.append(to_number)
    print("女巫毒人", dead_players)
    return


# 预言家验人 seer 2
def seer_action(to_number):
    identity = "好人"
    if players[to_number - 1] == "werewolf":
        identity = "坏人"
    print("预言家验人", identity)
    return identity


def distribute_roles(roles):
    global players
    global status
    global dead_players
    dead_players = []
    players = []
    #     分配号码和角色
    for key, value in roles.items():
        for i in range(int(value)):
            players.append(key)
            random.shuffle(players)
    shuffle_players()
    print("完成角色分配", players)
    status = "werewolf"


def shuffle_players():
    global players
    global status
    global dead_players
    global room_players
    for i in range(10):
        random.seed(i * i)
        random.shuffle(players)
    status = "werewolf"
    dead_players = []
    room_players = []


@app.route("/start_game", methods=["POST", "GET"])
def start_game():
    if request.method == "GET":
        shuffle_players()
        return Response("ok", status=200)
    distribute_roles(request.get_json())
    return Response("ok", status=200)


@app.route("/status", methods=["POST", "GET"])
def get_status():
    global status
    return Response(status, status=200)


@app.route("/player_count", methods=["POST", "GET"])
def player_count():
    return Response(str(len(players)), status=200)


@app.route("/ohgod", methods=["POST", "GET"])
def ohgod():
    return Response("player："+str(players) + "status："+status + "dead：" + str(dead_players), status=200)


@app.route("/role", methods=["POST", "GET"])
def role():
    # 保存進入房間的玩家
    global room_players
    user_number = int(request.get_json()["number"])
    check = request.get_json().get('check','check')
    print(room_players)
    if user_number in room_players :
        if request.method=='POST' and check=='check': 
            return Response('haven',status=200)
    else:
        room_players.append(user_number)
    return Response(players[user_number - 1], status=200)


@app.route("/room_players", methods=["POST", "GET"])
def room_play():
    global room_players

    return Response(str(set([i for i in range(1,len(players)+1)]).difference(set(room_players))).replace("set", ""))


@app.route("/result", methods=["POST", "GET"])
def get_result():
    result = "平安夜" if len(
        dead_players) == 0 else "死亡的玩家号码是：" + str(dead_players)
    return Response(result, status=200)


@app.route("/action", methods=["POST", "GET"])
def action():
    global status
    data = request.get_json()
    action_to_num = int(data["action"])
    number = int(data["number"])
    if players[number - 1] == status == data["role"] == "werewolf":
        werewolf_action(action_to_num)
        status = "witch"
        return Response("ok", status=200)

    elif players[number - 1] == status == data["role"] == "witch":
        witch_action(action_to_num)
        status = 'seer'
        return Response("ok", status=200)

    elif players[number - 1] == status == data["role"] == "seer":
        identity = seer_action(action_to_num)
        status = "init"
        return Response(str(action_to_num) + "号玩家的身份是：" + identity, status=200)
    return Response("error", status=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
