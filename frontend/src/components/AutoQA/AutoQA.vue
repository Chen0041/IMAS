<template>
  <div>
    <el-dialog
        title="UPLOAD"
        :visible.sync="uploadFormVisible"
        width="640px"
        append-to-body
        :close-on-click-modal="false"
        :close-on-press-escape="false"
        :show-close="false"
    >
      <el-form
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
        <el-form-item label="Picture" prop="uploadFile">
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
            <el-button slot="trigger" type="primary">BROWSE</el-button>
          </el-upload>
        </el-form-item>
      </el-form>
      <div slot="footer">
        <el-button type="primary" @click="upload">SUBMIT</el-button>
        <el-button @click="cancelUpload">CANCEL</el-button>
      </div>
    </el-dialog>

    <el-container>
      <NavigationBar/>
      <el-container id="consult-div">
        <el-container id="chat-div">
          <el-main>
            <div class="option-block">
              <el-select v-model="characterChosen" placeholder="Please select model"
                         @change="chooseCharacter">
                <el-option
                    v-for="item in characterList"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
              </el-select>
            </div>
            <div id="chat-history-box">
              <div id="chat-history" ref="chat"></div>
            </div>
          </el-main>
          <el-footer>
            <el-container>
              <div id="input">

                <template>
                  <el-input
                      placeholder="Please input through UPDATE button"
                      v-model="input"
                      @keyup.enter.native="send"
                      style="width: 100%; float: left"
                      :disabled="true"
                  >
                    <el-button slot="prepend" @click="openUploadDialog">UPDATE</el-button>
                  </el-input>
                </template>

              </div>
            </el-container>
          </el-footer>
        </el-container>
        <el-container id="info-div">
          <el-main id="intro">
            <div>
              <el-avatar>
                <img v-bind:src="require('../../assets/' + characterImgPath)"/>
              </el-avatar>
            </div>
            <div id="name-box">
              <div>{{characterName}}</div>
            </div>
            <div id="name-box1">
              <div style="font-size: 12px;">{{characterIntro}}</div>
            </div>
          </el-main>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
    import NavigationBar from "../NavigationBar.vue";
    export default {
      name: "AutoQA",
      components: {
          NavigationBar
      },
      data() {
        return {
          blue:true,
          blue_color: 255,
          input: "",
          characterList: [],
          characterChosen: "",
          final_transcript: "",
          recognizing: false,
          ignore_onend: "",
          start_timestamp: "",
          current_style: "",
          create_email: false,
          recognization: "",
          first_char: /\S/,
          two_line: /\n\n/g,
          one_line: /\n/g,
          uploadFormVisible: false,
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
          characterImgPath: 'robot.jpg',
          characterName: 'AI robot',
          characterIntro: 'AI robot automatically replies your questions.'
        }
      },
      methods: {
        getAllModels() {
          this.$axios({
            method: 'get',
            url: '/autuQA/models',
          }).then(res => {
            for (let i = 0; i < res.data.length; i++) {
              console.log(res.data[i])
              const temp = {"value": i + 1, "label": res.data[i]};
              // console.log(temp)
              this.characterList.push(temp)
            }
            console.log(this.characterList)
          }).catch(error => {
            console.log(error);
            this.$notify({
              title: 'Error',
              message: "ERROR! Load Models Failed! ",
              type: 'error'
            });
          });
        },
        showInfo: function (s) {
          if (s) {
            for (let child = document.getElementById("info").firstChild; child; child = child.nextSibling) {
              if (child.style) {
                child.style.display = child.id == s ? 'inline' : 'none';
              }
            }
            document.getElementById("info").setAttribute("style", "visibility:'visible'");
          } else {
            document.getElementById("info").setAttribute("style", "visibility:'hidden'");
          }
        },

        chooseCharacter(value) {
          this.characterChosen = value;
          this.blue=!this.blue
          if(this.blue){
            this.blue_color=255;
          }else {
            this.blue_color=120;
          }
        },
        linebreak: function (s) {
          return s.replace(this.two_line, "<p></p>").replace(this.one_line, "<br>");
        },
        upgrade: function () {
          document
              .getElementById("start_button")
              .setAttribute("style", "visibility :'hidden'");
          this.showInfo("info_upgrade");
        },
        upload() {
          this.uploadFormVisible = false;
          this.$refs.upload.submit();
        },
        openUploadDialog() {
          this.uploadFormVisible = true;
        },
        cancelUpload() {
          this.$refs["uploadForm"].resetFields();
          this.uploadFormVisible = false;
        },
        uploadMedicalArchive(content) {
          let imgurl = URL.createObjectURL(content.file);
          window.console.log(imgurl);
          console.log(this.uploadForm.desc);
          window.console.log("this.uploadForm.desc");
          let ques = this.uploadForm.desc;
          let params = new FormData();
          // params.append("title", this.uploadForm.title);
          params.append("desc", this.uploadForm.desc);
          params.append("file", content.file);
          console.log(params)
          // this.loadArchiveList();
          let image = document.createElement("img");
          image.src = URL.createObjectURL(content.file);
          image.style =
              "border: 1px rgb(31, 142, 255) solid; border-radius: 5px; background-color: rgb(31, 142, 255); color: white; float: right; width: 150px; padding: 6px 10px; margin: 5px; margin-left: 30px;"; // document.getElementById("images").appendChild(image);
          let outer_div = document.createElement("div");
          outer_div.style = "width: 100%; overflow: auto;";
          let div = document.createElement("div");
          div.innerHTML = ques;
          div.style =
              "border: 1px rgb(31, 142, 255) solid; border-radius: 5px; background-color: rgb(31, 142, 255); color: white; float: right; width: fit-content; padding: 6px 10px; margin: 5px; margin-left: 30px;";
          outer_div.append(div);
          let outer_div2 = document.createElement("div");
          outer_div.style = "width: 100%; overflow: auto;";
          outer_div2.append(image);
          // document.createElement("chat-history")

          document.getElementById("chat-history").append(outer_div);
          document.getElementById(
              "chat-history-box"
          ).scrollTop = document.getElementById("chat-history").scrollHeight;

          document.getElementById("chat-history").append(outer_div2);
          document.getElementById(
              "chat-history-box"
          ).scrollTop = document.getElementById("chat-history").scrollHeight;

          let taskName = ''
          for(let i=0;i<this.characterList.length;i++){
            if(this.characterChosen==this.characterList[i].value){
              taskName=this.characterList[i].label;
              break;
            }
          }
          this.$axios({
            method: "post",
            url: "/autuQA/"+ taskName,
            data: params,
          }).then((res) => {
            window.console.log(res);
            this.$refs["uploadForm"].resetFields();
            outer_div = document.createElement("div");
            outer_div.style = "width: 100%; overflow: auto;";
            div = document.createElement("div");
            div.innerHTML = res.data;
            div.style =
                "border: 1px rgb(235, 237, 240) solid; border-radius: 5px; background-color: rgb(235, 237, 240); float: left; width: fit-content; padding: 6px 10px; margin: 5px; margin-right: 30px;";
            outer_div.append(div);
            document.getElementById("chat-history").append(outer_div);
            setTimeout(function(){
              console.log("Time out! ");
            },"2000");
            document.getElementById(
                "chat-history-box"
            ).scrollTop = document.getElementById("chat-history").scrollHeight;
          });
        },
        capitalize: function (s) {
          return s.replace(this.first_char, function (m) {
            return m.toUpperCase();
          });
        },
      },
      mounted() {
        this.getAllModels()

        if (!("webkitSpeechRecognition" in window)) {
          this.upgrade();
        } else {
          // document.getElementById("start_button").setAttribute("style","display: 'inline-block'") ;
          this.recognition = new webkitSpeechRecognition();
          this.recognition.continuous = true;
          this.recognition.interimResults = true;
          let that = this;
          this.recognition.onstart = function () {
            that.recognizing = true;
            that.showInfo("info_speak_now");
            that.micImgPath = "mic-animate.gif";
            // document.getElementById("start_img").src = '../image/mic-animate.gif';
          };

          this.recognition.onerror = function (event) {
            if (event.error == "no-speech") {
              that.micImgPath = "mic.gif";
              // document.getElementById("start_img").setAttribute("src", '../image/mic.gif');
              that.showInfo("info_no_speech");
              that.ignore_onend = true;
            }
            if (event.error == "audio-capture") {
              that.micImgPath = "mic.gif";
              // document.getElementById("start_img").setAttribute("src",'../image/mic.gif');
              that.showInfo("info_no_microphone");
              that.ignore_onend = true;
            }
            if (event.error == "not-allowed") {
              if (event.timeStamp - this.start_timestamp < 100) {
                that.showInfo("info_blocked");
              } else {
                that.showInfo("info_denied");
              }
              that.ignore_onend = true;
            }
          };

          this.recognition.onend = function () {
            console.log("endof recog");
            that.recognizing = false;
            if (that.ignore_onend) {
              return;
            }
            that.micImgPath = "mic.gif";
            // document.getElementById("start_img").setAttribute("src", '../image/mic.gif');
            if (!that.final_transcript) {
              that.showInfo("info_start");
              return;
            }
            that.showInfo("");
          };

          this.recognition.onresult = function (event) {
            let interim_transcript = "";
            for (let i = event.resultIndex; i < event.results.length; ++i) {
              if (event.results[i].isFinal) {
                that.final_transcript += event.results[i][0].transcript;
              } else {
                interim_transcript += event.results[i][0].transcript;
              }
            }
            that.final_transcript = that.capitalize(that.final_transcript);
            // document.getElementById('final_span').setAttribute("innerHTML",this.linebreak(this.final_transcript))  ;
            // document.getElementById('interim_span').setAttribute("innerHTML", this.linebreak(interim_transcript);
            that.input = that.linebreak(that.final_transcript);
            // if (final_transcript || interim_transcript) {
            //   showButtons('inline-block');
            // }
          };
        }
      },
    }
</script>

<style scoped>
  #consult-div {
    position: fixed;
    top: 25%;
    left: 25%;
    right: 25%;
    bottom: 10%;
    border: 1px rgb(180, 180, 180) solid;
    border-radius: 5px;
  }

  #chat-div {
    width: 100%;
    height: 100%;
    margin-right: 0;
  }

  #chat-history-box {
    height: 99%;
    background-color: #fff;
    border: 1px rgb(180, 180, 180) solid;
    border-radius: 5px;
    overflow: auto;
  }

  #chat-history {
    margin: 15px;
    white-space: pre-line;
  }

  #input {
    width: 100%;
    height: 80%;
    margin-bottom: 0;
  }

  .el-input {
    width: 100%;
  }

  #info-div {
    width: 100%;
    height: 100%;
    padding-top: 50px;
    text-align: center;
    border-left: 1px rgb(180, 180, 180) solid;
    border-radius: 5px;
    background-color: rgb(245, 247, 250);
  }

  #name-box {
    margin-top: 20px;
  }
  #name-box1 {
    margin-top: 10px;
    text-align: left;
    margin-left: 5%;
  }

  .intro {
    padding-top: 50px;
  }
  .option-block {
    display: inline-block;
    position: fixed;
    top: 15%;
    /*margin-right: 40px;*/
  }

  .option-block .el-select {
    width: 400px;
  }
  #consult-div {
    position: fixed;
    top: 25%;
    left: 25%;
    right: 25%;
    bottom: 10%;
    border: 1px rgb(180, 180, 180) solid;
    border-radius: 5px;
  }

  #chat-div {
    width: 80%;
    height: 100%;
    margin-right: 0;
  }

  #chat-history-box {
    height: 100%;
    background-color: #fff;
    border: 1px rgb(180, 180, 180) solid;
    border-radius: 5px;
    overflow: auto;
  }

  #chat-history {
    margin: 15px;
    white-space: pre-line;
  }

  #input {
    width: 100%;
    height: 150%;
    margin-bottom: 0;
  }

  .el-input {
    width: 100%;
  }

  #info-div {
    width: 32%;
    height: 100%;
    padding-top: 50px;
    text-align: center;
    border-left: 1px rgb(180, 180, 180) solid;
    border-radius: 5px;
    background-color: rgb(245, 247, 250);
  }

  #name-box {
    margin-top: 20px;
  }

  #name-box1 {
    margin-top: 10px;
    text-align: left;
    margin-left: 5%;
  }

  .intro {
    padding-top: 50px;
  }

  .option-block {
    display: inline-block;
    position: fixed;
    top: 15%;
    /*margin-right: 40px;*/
  }

  .option-block .el-select {
    width: 400px;
  }

  #start_button {
    border: 0;
    background-color: transparent;
    padding: 0;
  }
</style>
