<template>
  <el-dialog
      v-model="visible"
      width="640px"
      title="UPLOAD"
      style="margin-top: 200px"
      :close-on-click-modal="false"
      :close-on-press-escape="false"
      :show-close="false"
  >
    <el-form
        style="margin: 10px"
        ref="uploadForm"
        :model="uploadForm"
        :rules="rules"
        label-position="left"
        label-width="130px"
    >
      <el-form-item label="Question" prop="desc">
        <el-input
            type="textarea"
            v-model="uploadForm.desc"
        ></el-input>
      </el-form-item>
      <el-form-item label="UPDATE" prop="uploadFile">
        <el-upload
            ref="upload"
            action=""
            accept=".png, .jpg, .jpeg"
            :multiple="false"
            :file-list="fileList"
            :show-file-list="true"
            :http-request="uploadMedicalArchive"
            :auto-upload="false"
        >
          <el-button slot="trigger" type="primary"
          >BROWSE
          </el-button
          >
        </el-upload>
      </el-form-item>
    </el-form>
    <div slot="footer">
      <el-button type="primary" @click="visible = false">SUBMIT</el-button>
      <el-button @click="visible = false">CANCEL</el-button>
    </div>
  </el-dialog>
  <el-container>
    <el-header style="height: 80px; width: 95vw">
      <NavigationBar/>
    </el-header>
    <el-main style="height: calc(100vh - 80px); width: 95vw">
      <div style="display: flex; justify-content: center;">
        <div style="width: 800px; height: 550px; border: 1px solid #cccccc; border-radius: 5px;">
          <el-container style="height: 100%;">
            <el-main>
              <el-select style="width: 30%" v-model="characterChosen" placeholder="Please chosen character"
                         @change="chooseCharacter">
                <el-option
                    v-for="item in characterList"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
              </el-select>
              <div style="margin-top:30px; height: 85%; background-color: #fff; border: 1px solid #cccccc; border-radius: 5px; overflow: auto;">
                <div style="margin: 15px; white-space: pre-line;" ref="chat"></div>
              </div>
            </el-main>
            <el-footer>
              <el-input placeholder="please input through Update button" v-model="input" @keyup.enter.native="send" style="width: 80%; float: left" :disabled="true"></el-input>
              <el-button style="margin-left: 40px" type="primary" slot="prepend" @click="visible = true">Update</el-button>
<!--              <el-button slot="append" @click="send" style="float: left"></el-button>-->
            </el-footer>
          </el-container>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script setup>
  const visible = ref(false)
</script>


<script>
import NavigationBar from "@/components/NavigationBar.vue";
import {ref} from "vue";


export default {
  name: "autoQA",
  components: {
    NavigationBar
  },

  data(){
    return{
      blue:true,
      blue_color: 255,
      input: "",
      // TODO ForTest
      // characterList: [],
      characterList: [{"value": 0, "label": "Test"}],
      characterChosen: "",
      final_transcript: "",
      recognizing: false,
      ignore_onend: "",
      start_timestamp: "",
      current_style: "",
      create_email: false,
      recognition: "",
      first_char: /\S/,
      two_line: /\n\n/g,
      one_line: /\n/g,
      fileList: [],
      uploadForm: {
        title: "",
        desc: "",
      },
      rules: {
        uploadFile: [
          {required: true, message: "Please select file", trigger: "change"},
        ],
        desc: [
          {
            required: true,
            message: "Please input description",
            trigger: "blur",
          },
        ],
      },
    }
  },
  
  methods:{
    getAllModels() {
      this.$axios({
        method: 'get',
        url: '/models',
      }).then(res => {
        for (let i = 0; i < res.data.length; i++) {
          console.log(res.data[i])
          let temp = {"value": i + 1, "label": res.data[i]}

          // console.log(temp)
          this.characterList.push(temp)
        }
        console.log(this.characterList)
        // this.characterChosen=this.characterList[0].label;

      }).catch(error => {
        console.log(error);
        alert("ERROR! Load Models Failed! ");
      });
    },
    chooseCharacter(value) {
      console.log(value)
      this.characterChosen = value;
      this.blue=!this.blue
      if(this.blue){
        this.blue_color=255;
      }else {
        this.blue_color=120;
      }
      let chat_history_node=document.getElementById("app").firstChild.firstChild.lastChild.lastChild.firstChild.lastChild.firstChild.firstChild.firstChild.firstChild.lastChild.firstChild;
      let chat_history_children=chat_history_node.childNodes;
      console.log(chat_history_children)
      for(let i=chat_history_children.length; i>=0; i--){
        if(chat_history_node.contains(chat_history_children[i])){
          console.log(chat_history_children[i])
          chat_history_node.removeChild(chat_history_children[i])
        }
      }
      console.log(this.characterList[this.characterChosen-1].label)
    },
    uploadMedicalArchive(content) {
    //   let imgUrl = URL.createObjectURL(content.file);
    //   window.console.log(imgUrl);
    //   console.log(this.uploadForm.desc);
    //   window.console.log("this.uploadForm.desc");
    //   let ques = this.uploadForm.desc;
    //   let params = new FormData();
    //   // params.append("title", this.uploadForm.title);
    //   params.append("desc", this.uploadForm.desc);
    //   params.append("file", content.file);
    //   console.log(params)
    //   // this.loadArchiveList();
    //   let image = document.createElement("img");
    //   image.src = URL.createObjectURL(content.file);
    //   image.style = "border: 1px rgb(31, 142, 255) solid; border-radius: 5px; background-color: rgb(31, 142, 255); color: white; float: right; width: 150px; padding: 6px 10px; margin: 5px; margin-left: 30px;"; // document.getElementById("images").appendChild(image);
    //   let outer_div = document.createElement("div");
    //   outer_div.style = "width: 100%; overflow: auto;";
    //   let div = document.createElement("div");
    //   div.innerHTML = ques;
    //   div.style = "border: 1px rgb(31, 142, 255) solid; border-radius: 5px; background-color: rgb(31, 142, 255); color: white; float: right; width: fit-content; padding: 6px 10px; margin: 5px; margin-left: 30px;";
    //   outer_div.append(div);
    //   let outer_div2 = document.createElement("div");
    //   outer_div.style = "width: 100%; overflow: auto;";
    //   outer_div2.append(image);
    //   document.getElementById("chat-history").append(outer_div);
    //   document.getElementById(
    //       "chat-history-box"
    //   ).scrollTop = document.getElementById("chat-history").scrollHeight;
    //
    //   document.getElementById("chat-history").append(outer_div2);
    //   document.getElementById(
    //       "chat-history-box"
    //   ).scrollTop = document.getElementById("chat-history").scrollHeight;
    //   // console.log(error);
    //   console.log("model name:" + this.characterList[this.characterChosen])
    //   this.$axios({
    //     method: "post",
    //     url: "/archive/user/"+this.characterList[this.characterChosen-1].label,//this.characterChosen,
    //     data: params,
    //   }).then((res) => {
    //     window.console.log(res);
    //     this.$refs["uploadForm"].resetFields();
    //     this.$message({
    //       type: "success",
    //       message: "Successfully uploaded medical archive!",
    //       showClose: true,
    //     });
    //     outer_div = document.createElement("div");
    //     outer_div.style = "width: 100%; overflow: auto;";
    //     div = document.createElement("div");
    //     div.innerHTML = res.data;
    //     div.style =
    //         "border: 1px rgb(235, 237, 240) solid; border-radius: 5px; background-color: rgb(235, 237, 240); float: left; width: fit-content; padding: 6px 10px; margin: 5px; margin-right: 30px;";
    //     outer_div.append(div);
    //     document.getElementById("chat-history").append(outer_div);
    //     setTimeout("testFunction(res)", "2000");
    //     document.getElementById(
    //         "chat-history-box"
    //     ).scrollTop = document.getElementById("chat-history").scrollHeight;
    //   });
    },
    send() {
      console.log('send msg.')
      // if (this.input != '') {
      //   let outer_div = document.createElement('div');
      //   outer_div.style = 'width: 100%; overflow: auto;';
      //   let div = document.createElement('div');
      //   div.innerHTML = this.input;
      //   div.style = 'border: 1px rgb(31, 142, 255) solid; border-radius: 5px; background-color: rgb(31, 142, 255); color: white; float: right; width: fit-content; padding: 6px 10px; margin: 5px; margin-left: 30px;';
      //   outer_div.append(div);
      //   document.getElementById("chat-history").append(outer_div);
      //   document.getElementById("chat-history-box").scrollTop = document.getElementById("chat-history").scrollHeight;
      //
      //   let params = new FormData();
      //   params.append("msg", this.input);
      //   this.input = '';
      //
      //   this.$axios({
      //     method: 'post',
      //     url: '/consult/online',
      //     data: params
      //   }).then(res => {
      //     // window.console.log(res.data);
      //     outer_div = document.createElement('div');
      //     outer_div.style = 'width: 100%; overflow: auto;';
      //     div = document.createElement('div');
      //     div.innerHTML = res.data;
      //     div.style = 'border: 1px rgb(235, 237, 240) solid; border-radius: 5px; background-color: rgb(235, 237, 240); float: left; width: fit-content; padding: 6px 10px; margin: 5px; margin-right: 30px;';
      //     outer_div.append(div);
      //     document.getElementById("chat-history").append(outer_div);
      //     setTimeout("testFunction(res)", "2000");
      //     document.getElementById("chat-history-box").scrollTop = document.getElementById("chat-history").scrollHeight;
      //   }).catch(error => {
      //     console.log(error);
      //   });
      // }
    },
  },

  mounted() {
    // this.getAllModels()
    // if (!("webkitSpeechRecognition" in window)) {
    //   this.upgrade();
    // } else {
    //   // document.getElementById("start_button").setAttribute("style","display: 'inline-block'") ;
    //   this.recognition = new webkitSpeechRecognition();
    //   this.recognition.continuous = true;
    //   this.recognition.interimResults = true;
    //   let that = this;
    //   this.recognition.onstart = function () {
    //     that.recognizing = true;
    //     that.showInfo("info_speak_now");
    //     that.micImgPath = "mic-animate.gif";
    //   };
    //
    //   this.recognition.onerror = function (event) {
    //     if (event.error === "no-speech") {
    //       that.micImgPath = "mic.gif";
    //       that.showInfo("info_no_speech");
    //       that.ignore_onend = true;
    //     }
    //     if (event.error === "audio-capture") {
    //       that.micImgPath = "mic.gif";
    //       that.showInfo("info_no_microphone");
    //       that.ignore_onend = true;
    //     }
    //     if (event.error === "not-allowed") {
    //       if (event.timeStamp - start_timestamp < 100) {
    //         that.showInfo("info_blocked");
    //       } else {
    //         that.showInfo("info_denied");
    //       }
    //       that.ignore_onend = true;
    //     }
    //   };
    //
    //   this.recognition.onend = function () {
    //     console.log("endof recog");
    //     that.recognizing = false;
    //     if (that.ignore_onend) {
    //       return;
    //     }
    //     that.micImgPath = "mic.gif";
    //     if (!that.final_transcript) {
    //       that.showInfo("info_start");
    //       return;
    //     }
    //     that.showInfo("");
    //   };
    //
    //   this.recognition.onresult = function (event) {
    //     let interim_transcript = "";
    //     for (let i = event.resultIndex; i < event.results.length; ++i) {
    //       if (event.results[i].isFinal) {
    //         that.final_transcript += event.results[i][0].transcript;
    //       } else {
    //         interim_transcript += event.results[i][0].transcript;
    //       }
    //     }
    //     that.final_transcript = that.capitalize(that.final_transcript);
    //     that.input = that.linebreak(that.final_transcript);
    //   };
    // }
  },
}
</script>


<style scoped>

</style>