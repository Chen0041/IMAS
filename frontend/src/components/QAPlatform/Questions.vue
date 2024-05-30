<template>
  <el-container>
    <NavigationBar/>
    <el-main>
      <div class="option-bar-div">
        <div class="option-bar">
          <div class="selector-bar">
            <span>Select: </span>
            <el-select class="select-bar" placeholder="Question Status" v-model="statusValue" @change="selectQuestionStatus">
              <el-option v-for="item in statusOptions" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>
            <el-select class="select-bar" placeholder="Question Department" v-model="departmentValue" @change="selectQuestionDepartmentId">
              <el-option v-for="item in departmentOptions" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>
          </div>
          <div class="search-bar">
            <el-input placeholder="Search" v-model="searchContent" clearable>
              <el-button slot="append" icon="el-icon-search" disabled></el-button>
            </el-input>
          </div>
          <div class="btn-bar">
            <el-button type="primary" @click="loadQuestions">Select</el-button>
            <el-button type="primary" @click="dialogFormVisible = true" style="margin-left: 20px">New Question</el-button>
          </div>
        </div>
      </div>

      <el-dialog title="New Question" :visible.sync="dialogFormVisible" append-to-body width="560px">
        <el-form ref="addQuestionForm" :model="newQuestionForm" :rules="rules" label-position="left" label-width="120px">
          <el-form-item label="Department" prop="hospitalDepartmentId">
            <el-select v-model="newQuestionForm.hospitalDepartmentId" placeholder="Choose a department">
              <el-option v-for="item in newQuestionForm.departmentOptions" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Description" prop="questionDesc">
            <el-input type="textarea" :rows="5" v-model="newQuestionForm.questionDesc"></el-input>
          </el-form-item>
          <el-form-item label="Image" prop="questionPic">
            <el-upload class="upload-demo"
                       ref="upload"
                       multiple
                       accept=".png, .jpg, .jpeg"
                       :http-request="uploadNewQuestion"
                       :file-list="fileList"
                       :show-file-list="true"
                       :auto-upload="false"
                       :limit="5"
                       :on-success="handleFilUploadSuccess"
                       :on-remove="handleRemove"
                       action=""
            >
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">drop files here,or <em>click here to upload files</em></div>
              <div class="el-upload__tip" slot="tip">please upload image files</div>
            </el-upload>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button type="primary" @click="uploadQuestion">Submit</el-button>
          <el-button @click="dialogFormVisible = false">Cancel</el-button>
        </div>
      </el-dialog>

      <el-dialog title="Answer Question" :visible.sync="answerFormVisible" append-to-body width="560px">
        <el-form :rules="rules" label-position="left" label-width="120px">
          <el-form-item label="Answer" prop="questionAnswer">
            <el-input type="textarea" :rows="5" v-model="questionAnswer"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button type="primary" @click="answerQuestion">Submit</el-button>
          <el-button @click="answerFormVisible = false">Cancel</el-button>
        </div>
      </el-dialog>

      <el-card>
        <el-table
            :data="questionList"
            style="width: 100%"
            :row-class-name=tableRowClassName
            :default-sort="{prop: 'date', order: 'descending'}"
        >
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">-->
                <el-form-item label="Answer" style="width: 300px">
                  <span>{{props.row.answer}} </span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>

          <el-table-column
              prop="department"
              label="Department"
              width="140"
              sortable
          ></el-table-column>

          <el-table-column
              prop="content"
              label="Content"
              width="500"
              sortable
          ></el-table-column>

          <el-table-column
              prop="date"
              label="Date"
              width="120"
              sortable
          ></el-table-column>
          <el-table-column
              prop="status"
              label="Status"
              width="120"
              sortable
          ></el-table-column>
          <el-table-column label="Show Images" width="120">
            <template slot-scope="scope">
              <el-popover
                  placement="bottom"
                  title="Show Image"
                  width="1000"
                  trigger="click"
                  content="">
                <el-button type="text" slot="reference" @click="getPhoto(scope.row.id)">Show Images</el-button>
                <div>
                  <el-scrollbar style="height:500px">
                    <img :src="imgSrc" width="500px" height="400px" alt=""/>
                  </el-scrollbar>
                </div>
              </el-popover>
            </template>
          </el-table-column>

          <el-table-column
              label="Operations"
              width="180"
          >
            <template slot-scope="scope">
              <el-button type="danger" size="mini" @click="deleteQuestion(scope.row.id)">Delete</el-button>
              <el-button type="primary" size="mini" @click="beforeAnswerQuestion(scope.row.id)" :style="{ display: allowAnswer}">Answer</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-main>
  </el-container>

</template>

<script>
import NavigationBar from "../NavigationBar.vue";
export default {
  name: "Questions",
  components: {
    NavigationBar
  },
  data() {
    return {
      allowAnswer: this.$store.state.user.type === 0?'none':'',
      imgSrc: require('../../assets/medical_pic.jpg'),
      fileList:[],
      questionList: [],
      statusOptions: [
        {
          value: 0,
          label: 'Not Answered'
        }, {
          value: 1,
          label: 'Answered'
        },{
          value: 2,
          label: 'All'
        }
      ],
      statusValue: 2,
      departmentOptions:[],
      departmentValue: 0,
      searchContent: '',
      dialogFormVisible: false,
      answerFormVisible: false,
      answerQuestionId: 0,
      questionAnswer: '',
      newQuestionForm: {
        departmentOptions: [],
        hospitalDepartmentId: '',
        questionDesc: '',
      },
      rules: {
        hospitalDepartmentId: [
          {required: true, message: 'Please choose a department', trigger: 'blur'}
        ],
        questionDesc: [
          {required: true, message: 'Please input question description', trigger: 'blur'}
        ],
        questionPic: [
          {required: true, message: 'Please upload file', trigger: 'blur'}
        ],
        questionAnswer: [
          {required: true, message: 'Please input answer', trigger: 'blur'}
        ]
      },
      questionStatus: 2,
      questionDepartmentId: 0,
    };
  },
  methods: {
    uploadQuestion() {
      this.dialogFormVisible = false;
      this.$refs.upload.submit();
    },
    uploadNewQuestion(content) {
      let params = new FormData();
      params.append("login_name", this.$store.state.user.username);
      params.append("content", this.newQuestionForm.questionDesc);
      params.append("department_id", this.newQuestionForm.hospitalDepartmentId);
      params.append("file", content.file);
      console.log(params)
      this.$axios({
        method: "post",
        url: "/QAPlatform/question/new",
        data:params,
      })
          .then((res) => {
            console.log(res.data);
            this.dialogFormVisible = false;
            this.loadQuestions();
            this.$notify({
              title: "Success",
              message: "Successfully upload question! ",
              type: "success",
            });
          })
          .catch((error) => {
            console.log(error);
            this.$notify({
              message: "Upload error, please check console for detail! ",
              type: "error",
            });
          });
    },
    handleFilUploadSuccess (res,file,fileList) {
      console.log(res,file,fileList)
      this.$message.success("上传成功")
    },
    handleRemove(file,fileList) {
      console.log(file,fileList);
    },
    tableRowClassName({row}, rowIndex) {
      if (row.status == 'answered'){
        return 'success-row';
      }
      else{
        return 'warning-row';
      }
    },
    beforeAnswerQuestion(id){
      this.answerFormVisible = true
      this.answerQuestionId = id
    },
    answerQuestion(){
      let params = new FormData();
      params.append("login_name", this.$store.state.user.username);
      params.append("answer", this.questionAnswer);
      this.$axios({
        method: "post",
        url: "/QAPlatform/question/answer/"+this.answerQuestionId,
        data:params,
      })
          .then((res) => {
            this.answerFormVisible = false;
            this.loadQuestions();
            this.$notify({
              title: "Success",
              message: "Successfully answer question! ",
              type: "success",
            });
          })
          .catch((error) => {
            console.log(error);
            this.$notify({
              message: "Answer error, please check console for detail! ",
              type: "error",
            });
          });
    },
    deleteQuestion(id){
      let params = new FormData();
      params.append("login_name", this.$store.state.user.username);
      this.$axios({
        method: "post",
        url: "/QAPlatform/question/delete/"+id,
        data:params,
      })
          .then((res) => {
            this.loadQuestions();
            this.$notify({
              title: "Success",
              message: "Successfully delete question! ",
              type: "success",
            });
          })
          .catch((error) => {
            console.log(error);
            this.$notify({
              title: 'ERROR',
              message: "Dekete error, please check console for detail! ",
              type: "error",
            });
          });
    },
    selectQuestionStatus(value) {
      this.questionStatus = value
    },
    selectQuestionDepartmentId(value) {
      this.questionDepartmentId = value
    },
    loadDepartments() {
      this.$axios({
        method: 'get',
        url: '/QAPlatform/departments',
      }).then(res => {
        for (let department in res.data) {
          if (res.data.hasOwnProperty(department)) {
            this.newQuestionForm.departmentOptions.push({
              value: res.data[department].id,
              label: res.data[department].department
            });
            this.departmentOptions.push({
              value: res.data[department].id,
              label: res.data[department].department
            });
          }
        }
        this.departmentOptions.push({value: 0, label: "全部"})
      }).catch(error => {
        console.log(error);
        this.$notify({
          title: 'ERROR',
          message: 'ERROR when load departments, check console for detail! ',
          type: 'error'
        });
      });
    },
    getPhoto(id){
      this.$axios({
        method: 'get',
        url: '/loadPicture/'+id,
        responseType:'blob'
      }).then(res => {
        let blob = new Blob([res.data], {
          type: "image/png",
        });
        this.imgSrc=window.URL.createObjectURL(blob)
      }).catch(error => {
        console.log(error);
      });
    },
    loadQuestions() {
      let params = new FormData();
      params.append('status',this.questionStatus)
      params.append('department_id',this.questionDepartmentId)
      params.append('search_content',this.searchContent)
      this.$axios({
        method: 'post',
        url: 'QAPlatform/questions',
        data: params
      }).then(res => {
        this.questionList=res.data
      }).catch(error => {
        console.log(error);
      });
    },
  },
  created() {
    this.loadDepartments();
    this.loadQuestions();
    sessionStorage.setItem("addsCurrentQuestionStatusIsChanged", JSON.stringify({
      isChanged: false
    }));
  },
}
</script>

<style>
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>

<style scoped>
.el-main {
  position: fixed;
  top: 80px;
  left: 30px;
  right: 30px;
  bottom: 0;
  margin: 20px;
  padding: 10px;
}

.option-bar-div {
  text-align: center;
}

.option-bar-div .option-bar {
  display: inline-block;
}

.selector-bar {
  float: left;
  margin: 0 20px;
}

.selector-bar span {
  margin-right: 20px;
}

.select-bar{
  width: 150px
}

.search-bar {
  float: left;
  margin: 0 20px;
  width: 280px;
}

.btn-bar {
  float: left;
  margin: 0 20px;
}

.demo-table-expand {
  font-size: 0;
}

.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}

.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 20%;
}

.content-div {
  position: fixed;
  top: 180px;
  left: 30px;
  right: 30px;
  bottom: 0;
}

.question-list-div {
  overflow-y: hidden;
}

.el-card:hover {
  box-shadow: 6px 6px 8px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

.question-div {
  width: 75%;
  margin: 0 auto 30px auto;
  padding: 20px 40px;
  border: 1px solid rgb(180, 216, 255);
  border-radius: 5px;
  overflow: hidden;
}

.question-div .el-button {
  float: right;
  padding: 0;
}

.loading-info {
  height: 40px;
  text-align: center;
}

.back-top {
  height: 50px;
  width: 50px;
  line-height: 50px;
  background-color: rgb(238, 241, 246);
  box-shadow: 0 0 6px rgba(0, 0, 0, .12);
  font-weight: bold;
  color: #1989fa;
  text-align: center;
  border-radius: 3px;
  position: fixed;
  bottom: 75px;
  right: 75px;
  cursor: pointer;
}
</style>
