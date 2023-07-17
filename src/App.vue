<template>
  <el-container id="app">
    <el-header
      style="
        background: linear-gradient(135deg, #8f75da 0, #727cf5 60%);
        height: 12vw;
        font-size: 3vw;
      "
      ><h1 style="color: white">桌游发牌官</h1></el-header
    >
    <el-main>
      <el-row style="margin-top: 2%" :gutter="40">
        <el-col :span="8">
          <el-button type="success" round @click="enterRoom">进入房间 </el-button>
        </el-col>
        <el-col :span="8">
          <el-button type="danger" round @click="startGame">创建房间 </el-button>
        </el-col>
        <el-col :span="8">
          <el-button type="warning" round @click="awalong">瓦隆语音 </el-button>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/狼人.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>狼人 werewolf</h1>
              <el-input type="number" v-model="form.werewolf"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/村民.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>村民 villager</h1>
              <el-input type="number" v-model="form.villager"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/预言家.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>预言家 seer</h1>
              <el-input type="number" v-model="form.seer"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/女巫.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>女巫 witch</h1>
              <el-input type="number" v-model="form.witch"></el-input>
            </div>
          </el-card>
        </el-col>

        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/猎人.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>猎人 hunter</h1>
              <el-input type="number" v-model="form.hunter"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/白痴.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>白痴 idiot</h1>
              <el-input type="number" v-model="form.idiot"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/炸弹人.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>炸弹人 boomer</h1>
              <el-input type="number" v-model="form.boomer"></el-input>
            </div>
          </el-card>
        </el-col>

        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/守卫.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>守卫 savior</h1>
              <el-input type="number" v-model="form.savior"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/白狼王.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>白狼王 whitewolf</h1>
              <el-input type="number" v-model="form.whitewolf"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/骑士.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>骑士 knightr</h1>
              <el-input type="number" v-model="form.knightr"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              class="image"
              :src="require('./assets/狼狗.jpg')"
            ></el-image>
            <div class="bottom-text">
              <h1>隐狼 hiddenwolf</h1>
              <el-input type="number" v-model="form.hiddenwolf"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/丘比特.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>丘比特 cupid</h1>
              <el-input type="number" v-model="form.cupid"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/城管.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>城管 cityman</h1>
              <el-input type="number" v-model="form.cityman"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              class="image"
              :src="require('./assets/村长.jpg')"
            ></el-image>
            <div class="bottom-text">
              <h1>村长 villagehead</h1>
              <el-input type="number" v-model="form.villagehead"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/大野狼.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>大野狼 bigwolf</h1>
              <el-input type="number" v-model="form.bigwolf"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/盗贼.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>盗贼 thief</h1>
              <el-input type="number" v-model="form.thief"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              class="image"
              :src="require('./assets/狐狸.jpg')"
            ></el-image>
            <div class="bottom-text">
              <h1>狐狸 fox</h1>
              <el-input type="number" v-model="form.fox"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/吉普赛狼.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>吉普赛狼 solitudewolf</h1>
              <el-input type="number" v-model="form.solitudewolf"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/口吃法官.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>口吃法官 shutjudge</h1>
              <el-input type="number" v-model="form.shutjudge"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              class="image"
              :src="require('./assets/苦涩的老爷爷.jpg')"
            ></el-image>
            <div class="bottom-text">
              <h1>苦涩爷爷 hardgrandpa</h1>
              <el-input type="number" v-model="form.hardgrandpa"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/两姐妹.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>两姐妹 sisters</h1>
              <el-input type="number" v-model="form.sisters"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/女仆.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>女仆 maid</h1>
              <el-input type="number" v-model="form.maid"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              class="image"
              :src="require('./assets/三兄弟.jpg')"
            ></el-image>
            <div class="bottom-text">
              <h1>三兄弟 brothers</h1>
              <el-input type="number" v-model="form.brothers"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/替罪羊.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>替罪羊 scapegoat</h1>
              <el-input type="number" v-model="form.scapegoat"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/天使.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>天使 angel</h1>
              <el-input type="number" v-model="form.angel"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              class="image"
              :src="require('./assets/小女孩.jpg')"
            ></el-image>
            <div class="bottom-text">
              <h1>小女孩 girl</h1>
              <el-input type="number" v-model="form.girl"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/驯熊师.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>驯熊师 tamer</h1>
              <el-input type="number" v-model="form.tamer"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/演员.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>演员 actor</h1>
              <el-input type="number" v-model="form.actor"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              class="image"
              :src="require('./assets/野孩子.jpg')"
            ></el-image>
            <div class="bottom-text">
              <h1>野孩子 kids</h1>
              <el-input type="number" v-model="form.kids"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/长老.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>长老 longoldman</h1>
              <el-input type="number" v-model="form.longoldman"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="30">
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              :src="require('./assets/种狼.jpg')"
              class="image"
            ></el-image>
            <div class="bottom-text">
              <h1>种狼 fkwolf</h1>
              <el-input type="number" v-model="form.fkwolf"></el-input>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card :body-style="{ padding: '0px' }">
            <el-image
              fit="cover"
              class="image"
              :src="require('./assets/纵火者.jpg')"
            ></el-image>
            <div class="bottom-text">
              <h1>纵火者 fireman</h1>
              <el-input type="number" v-model="form.fireman"></el-input>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    awalong() {
      let day1 = 21000;
      let day2 = 12000;
      new Audio(
        "http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=3&text=天黑请闭眼，除了莫德雷德的坏人请睁眼并举手确认身份。"
      ).play();
      setTimeout(function () {
        new Audio(
          "http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=3&text=坏人请闭眼，梅林请睁眼确认坏人位置。"
        ).play();
      }, day1);
      setTimeout(function () {
        new Audio(
          "http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=3&text=梅林请闭眼，莫甘娜和梅林请举手，派西维尔请睁眼确认位置。"
        ).play();
      }, day1 + day2);
      setTimeout(function () {
        new Audio(
          "http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=3&text=所有人请闭眼，并放下手。"
        ).play();
      }, day1 + day2 * 2);
      setTimeout(function () {
        new Audio(
          "http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&spd=3&text=天亮了。"
        ).play();
      }, day1 + day2 * 2.5);
    },
    enterRoom() {
      localStorage.clear();
      window.location.href = "/desktop";
    },
    startGame() {
      let context = "";
      let count = 0;
      for (var key in this.form) {
        let item = this.form[key];
        context += "<h1>";
        context += key + "：" + item;
        context += "</h1>";
        count += parseInt(item);
      }
      context += "<h1>总人数：" + count + "</h1>";
      this.$confirm(context, "创建房间", {
        confirmButtonText: "确定",
        dangerouslyUseHTMLString: true,
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        axios
          .post("http://39.101.182.237:7778/start_game", this.form)
          .then((res) => {
            console.log(res);
            if (res.data == "error") {
              this.$message("游戏已经开始");
            }
            localStorage.clear();
            window.location.href = "/desktop";
          })
          .catch((res) => {});
      });
      console.log(this.form);
    },
  },
  data() {
    return {
      form: {
        hunter: 1,
        idiot: 1,
        seer: 1,
        villager: 4,
        werewolf: 4,
        witch: 1,
      },
    };
  },
};
</script>

<style>
.el-message-box {
  width: 60% !important;
}
span {
  font-size: 4vw;
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
