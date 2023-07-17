<template>
  <el-container id="app">
    <el-header
      style="
        background: linear-gradient(135deg, #8f75da 0, #727cf5 60%);
        height: 12vw;
        font-size: 3vw;
      "
      ><h1 @click="toIndex" style="color: white">桌游发牌官</h1>
    </el-header>
    <el-main>
      <el-row :gutter="40">
        <el-col :span="6" v-for="i of playerCount" :key="i">
          <el-card :style="i == number ? 'background:pink' : ''">
            <h1 @click="setDown(i)">座位号：{{ i }}</h1>
            <!--                        <h1>姓名：{{ players[i] ? players[i].name : "" }}</h1>-->
          </el-card>
        </el-col>
      </el-row>
    </el-main>
    <el-row :gutter="40" style="margin-top: 5%" v-if="number == 1">
      <el-col :span="8">
        <el-button type="info" round @click="enterNight">进入黑夜</el-button>
      </el-col>
      <el-col :span="8">
        <el-button type="info" round @click="getResult">昨夜信息</el-button>
      </el-col>

      <!-- <el-col :span="8">
        <el-button type="info" round @click="reSit">换个座位</el-button>
      </el-col> -->
    </el-row>

    <el-row style="margin-top: 20px">
      <el-col :span="12">
        <el-button type="info" round @click="startGame">重新发牌 </el-button>
      </el-col>
      <el-col :span="12">
        <el-button type="info" round @click="checkSit">空闲座位 </el-button>
      </el-col>
    </el-row>
    <el-row :gutter="40" style="margin-top: 5%">
      <el-col :span="6">
        <el-button type="danger" round @click="werewolfAction"
          >狼人杀人</el-button
        >
      </el-col>
      <el-col :span="6">
        <el-button type="warning" round @click="witchAction"
          >女巫用药</el-button
        >
      </el-col>
      <el-col :span="6">
        <el-button type="success" round @click="seerAction">预言查验</el-button>
      </el-col>
      <el-col :span="6">
        <el-button type="primary" round @click="saviorAction"
          >守卫守人</el-button
        >
      </el-col>
    </el-row>
  </el-container>
</template>

<script>
import axios from "axios";

export default {
  created() {
    this.player_count().then((res) => {
      console.log(res);
      this.playerCount = res.data;
    });
  },
  methods: {
    checkSit() {
      this.get_role_players().then((res) => {
        console.log(res);
        this.$msgbox(res.data);
      });
    },
    toIndex() {
      window.location.href = "/";
    },
    get_role_players() {
      return axios.get("http://39.101.182.237:7778/room_players");
    },
    player_count() {
      return axios.get("http://39.101.182.237:7778/player_count");
    },
    action(action_number) {
      return axios.post("http://39.101.182.237:7778/action", {
        number: localStorage.getItem("number"),
        action: action_number,
        role: localStorage.getItem("role"),
      });
    },
    getResult() {
      if (this.number != 1) {
        this.$msgbox("这种事你干不了！", "だめ");
        return;
      }
      this.result().then((res) => {
        this.$msgbox(res.data, "昨夜信息");
      });
    },
    result() {
      return axios.get("http://39.101.182.237:7778/result");
    },
    get_role(number, check) {
      return axios.post("http://39.101.182.237:7778/role", {
        number: number,
        check: check,
      });
    },
    status_url() {
      return axios.get("http://39.101.182.237:7778/status");
    },
    reSit() {
      localStorage.clear();
      window.location.href = "/desktop";
    },
    startGame() {
      if (this.number != 1) {
        this.status_url().then((res) => {
          if (res.data != "init" || res.data != "werewolf") {
            this.$msgbox("这种事你干不了！", "だめ");
            return;
          } else {
            localStorage.clear();
            window.location.href = "/desktop";
            return;
          }
        });
      } else {
        axios.get("http://39.101.182.237:7778/start_game").then((res) => {
          // localStorage.clear();
          localStorage.setItem("role", null);
          window.location.href = "/desktop";
        });
      }
    },

    //狼人杀人
    werewolfAction() {
      if (this.role != "werewolf") {
        this.$msgbox("还没到你呢，别急！", "だめ");
        return;
      }
      //    输入要杀的号码
      this.$prompt("请输入猎杀的号码", "狼人", {
        inputType: "number",
        inputValidator: this.numberValidator,
      }).then((value) => {
        this.action(value.value).then((res) => {
          if (res.data == "error") {
            this.$msgbox("还没轮到你，别着急", "だめ");
            return;
          }
        });
      });
    },
    numberValidator(value) {
      console.log(value);
      if (value) {
        if (
          parseInt(value) < 0 ||
          parseInt(value) > parseInt(this.playerCount)
        ) {
          return "号码超出范围";
        }
      } else {
        return "输入不能为空";
      }
    },
    listenStatusChange() {
      this.status_url().then((res) => {
        if (this.status != res.data) {
          this.status = res.data;
          if (this.status == "witch") {
            new Audio(
              "http://39.101.182.237:7777/langren.mp3"
            ).play();
          } else if (this.status == "seer") {
            new Audio(
              "http://39.101.182.237:7777/nvwu.mp3"
            ).play();
          } else if (this.status == "init") {
            new Audio(
              "http://39.101.182.237:7777/tianliang.mp3"
            ).play();
            clearInterval(this.statusInterval);
          }
        }
      });
    },
    enterNight() {
      if (this.number != 1) {
        this.$msgbox("这种事你干不了！", "だめ");
        return;
      }
      new Audio(
              "http://39.101.182.237:7777/tianhei.mp3"
      ).play();
      console.log( new Audio(
              "http://39.101.182.237:7777/tianhei.mp3"
      ))
      this.status = "werewolf";
      this.statusInterval = setInterval(this.listenStatusChange, 3000);
    },
    witchAction() {
      if (this.role != "witch") {
        this.$msgbox("还没到你呢，别急！", "だめ");
        return;
      }
      this.result().then((res) => {
        this.$confirm("昨天晚上：" + res.data + "。你要使用解药吗", "女巫")
          .then((value) => {
            this.action(666).then((res) => {
              if (res.data == "error") {
                this.$msgbox("还没轮到你，别着急", "だめ");
                return;
              }
            });
          })
          .catch((res) => {
            this.$prompt("输入你使用毒药的座位号，不使用则点击取消", "女巫", {
              inputValidator: this.numberValidator,
              inputType: "number",
            })
              .then((value) => {
                this.action(value.value).then((res) => {});
              })
              .catch((res) => {
                this.action(999).then((res) => {});
              });
          });
      });
    },
    seerAction() {
      if (this.role != "seer") {
        this.$msgbox("还没到你呢，别急！", "だめ");
        return;
      }
      this.$prompt("输入你要查验的玩家座位号", "预言家", {
        inputType: "number",
        inputValidator: this.numberValidator,
        showCancelButton: false,
      }).then((value) => {
        this.action(value.value).then((res) => {
          if (res.data == "error") {
            this.$msgbox("还没轮到你，别着急", "だめ");
            return;
          }
          this.$msgbox(res.data, "结果").then((res) => {});
        });
      });
    },
    saviorAction() {
      // new Audio(
      //     "http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=3&text=预言家请闭眼，守卫请睁眼"
      // ).play();
    },

    setDown(desk_index) {
      this.number = localStorage.getItem("number");
      this.role = localStorage.getItem("role");
      console.log(this.number);
      if (this.number) {
        if (this.number != desk_index) {
          this.$msgbox("不可以查看别人的身份", "だめ");
          return;
        }
        this.get_role(desk_index, "no_check").then((res) => {
          this.$msgbox("你的身份是：" + res.data, "结果");
        });
      } else {
        this.$confirm("确定要坐在：" + desk_index + " 号位置吗", "确认")
          .then((res) => {
            this.get_role(desk_index,"check").then((res) => {
              if (res.data == "haven") {
                this.$msgbox("位置上已经有人了！请换个座位", "だめ");
                return;
              }
              localStorage.setItem("number", desk_index);
              localStorage.setItem("role", res.data);
              this.number = localStorage.getItem("number");
              this.role = localStorage.getItem("role");
              this.$msgbox("你的身份是：" + this.role, "结果");
            });
          })
          .catch((res) => {});
      }
    },
  },
  data() {
    return {
      room_players: [],
      statusInterval: null,
      status: "init",
      number: localStorage.getItem("number"),
      role: localStorage.getItem("role"),
      form: {},
      playerCount: 1,
      players: {
        1: { name: "徐开元", identity: "werewolf" },
        2: { name: "冯翀", identity: "villager" },
      },
    };
  },
};
</script>

<style>
p {
  font-size: 2.5vw;
}
span {
  font-size: 3.5vw;
}
.el-message-box {
  width: 60% !important;
}

.el-input__inner {
  font-size: 5vw;
  height: 8vw;
  text-align: center;
  width: 50%;
}
.bottom-text {
  padding: 5vw;
}

.el-button {
  font-size: 3vw;
}

.el-card {
  /* width:60vw; */
  margin-top: 5vw;
  /* margin-left:15vw; */
}

.image {
  /* width:60vw; */
}

#app {
  font-family: Helvetica, sans-serif;
  text-align: center;
}
</style>
