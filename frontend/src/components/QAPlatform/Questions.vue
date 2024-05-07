<template>
  <el-container>
    <NavigationBar/>
    <el-main>
      <div class="option-bar-div">
        <div class="option-bar">
          <div class="selector-bar">
            <span>Select: </span>
            <el-select class="select-bar" placeholder="Question Status" v-model="value1" @change="selectQuestionStatus">
              <!--            clearable @clear="clearQuestionStatus" @clear="clearQuestionType"-->
              <el-option v-for="item in options1" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>
            <el-select class="select-bar" placeholder="Question Department" v-model="value3" @change="selectQuestionType">
              <el-option v-for="item in options3" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>
          </div>
          <div class="search-bar">
            <el-input placeholder="Search" v-model="searchContent" clearable>
              <el-button slot="append" icon="el-icon-search" @click="searchQuestions"></el-button>
            </el-input>
          </div>
          <div class="btn-bar">
            <el-button type="primary" @click="dialogFormVisible = true">New Question</el-button>
            <el-button type="primary" @click="loadMyQuestions">My Questions</el-button>
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
                       accept=".pdf"
                       :http-request="uploadDataset"
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
            </el-upload>
          </el-form-item>
          <!--        <el-form-item label="Type" prop="questionType">-->
          <!--          <el-radio-group v-model="newQuestionForm.questionType">-->
          <!--            <el-radio label="1">Simple choice</el-radio>-->
          <!--            <el-radio label="2">Detailed answer</el-radio>-->
          <!--          </el-radio-group>-->
          <!--        </el-form-item>-->
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button type="primary" @click="addNewQuestion">Submit</el-button>
          <el-button @click="dialogFormVisible = false">Cancel</el-button>
        </div>
      </el-dialog>

      <el-dialog title="Answer Question" :visible.sync="answerFormVisible" append-to-body width="560px">
        <el-form ref="addQuestionForm" :model="newQuestionForm" :rules="rules" label-position="left" label-width="120px">
          <el-form-item label="Answer" prop="questionDesc">
            <el-input type="textarea" :rows="5" v-model="newQuestionForm.questionDesc"></el-input>
          </el-form-item>
          <el-form-item label="Picture" prop="questionPic">
            <el-upload class="upload-demo"
                       ref="upload"
                       multiple
                       accept=".pdf"
                       :http-request="uploadDataset"
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
            </el-upload>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button type="primary" @click="addNewQuestion">Submit</el-button>
          <el-button @click="answerFormVisible = false">Cancel</el-button>
        </div>
      </el-dialog>

      <el-card>
        <el-table
            :data="tableData1"
            style="width: 100%"
            :row-class-name=tableRowClassName
            :default-sort="{prop: 'date', order: 'descending'}"
        >
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">-->
                <el-form-item label="Answer">
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
                <el-button type="text" slot="reference">Show Images</el-button>
                <div>
                  <el-scrollbar style="height:500px">
                    <el-row>
                      <p style="font-size:15px">Question Image:</p>
                    </el-row>
                    <img :src="imgSrc1" width="500px" height="400px" alt=""/>
                    <el-row>
                      <p style="font-size:15px">Answer Image:</p>
                    </el-row>
                    <img :src="imgSrc2" width="500px" height="400px" alt=""/>
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
              <el-button type="primary" size="mini" @click="answerFormVisible = true">Answer</el-button>
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
              imgSrc1: require('../../assets/medical_pic.jpg'),
              imgSrc2: require('../../assets/medical_pic2.jpg'),
              fileList:[],
                tableData1: [{
                  id: 1,
                  date: '2024-4-25',
                  content: 'Test Question1',
                  department: '儿科',
                  status: 'answered',
                  answer: 'Test Answer1'
                },{
                  id: 2,
                  date: '2024-4-27',
                  content: 'Test Question2',
                  department: '外科',
                  status: 'not answered',
                  answer: ''
                }
                ],
                options1: [
                    {
                        value: '1',
                        label: 'All'
                    }, {
                        value: '2',
                        label: 'Not Answered'
                    }, {
                        value: '3',
                        label: 'Answered'
                    }
                ],
                value1: '1',
                options2: [
                    {
                        value: '1',
                        label: 'All'
                    }, {
                        value: '2',
                        label: 'Detailed answer'
                    }, {
                        value: '3',
                        label: 'Simple choice'
                    }
                ],
                value2: '1',
                options3:[
                  {
                    value:'1',
                    label:'全部'
                  },{
                    value:'2',
                    label:'内科'
                  },{
                    value:'3',
                    label:'外科'
                  },{
                    value:'4',
                    label:'儿科'
                  },{
                    value:'5',
                    label:'妇科'
                  },{
                    value:'6',
                    label:'不明'
                  }
                ],
                value3: '1',
                searchContent: '',
                dialogFormVisible: false,
                answerFormVisible: false,
                newQuestionForm: {
                    departmentOptions: [],
                    hospitalDepartmentId: '',
                    questionDesc: '',
                    questionType: ''
                },
                rules: {
                    hospitalDepartmentId: [
                        {required: true, message: 'Please choose a department', trigger: 'blur'}
                    ],
                    questionDesc: [
                        {required: true, message: 'Please input question description', trigger: 'blur'}
                    ],
                    questionType: [
                        {required: true, message: 'Please choose question type', trigger: 'blur'}
                    ],
                    questionPic: [
                        {required: false, message: 'Please choose question type', trigger: 'blur'}
                    ]
                },

                // questionList: [],
                questionList: [{
                  id: 1,
                  desc: 'Test Question Simple Choice'
                }],
                page: 1,
                limit: 10,
                loadedQuestionCount: 999,
                // scroll: 0,

                questionStatus: 1,
                questionType: 1,
            };
        },
        computed: {
            stopLoading() {
                return this.loadedQuestionCount < this.limit;
            }
        },
        methods: {
          uploadDataset(content) {
            let params = new FormData();
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
          answerQuestion(id){

          },
          deleteQuestion(id){

          },
            selectQuestionStatus(value) {
                if (value === '1') {
                    this.questionStatus = 1;
                    this.selectQuestions();
                } else if (value === '2') {
                    this.questionStatus = 2;
                    this.selectQuestions();
                }
            },
            selectQuestionType(value) {
                if (value === '1') {
                    this.questionType = 1;
                    this.selectQuestions();
                } else if (value === '2') {
                    this.questionType = 2;
                    this.selectQuestions();
                }
            },
            // clearQuestionStatus() {
            //     this.questionStatus = 0;
            //     this.selectQuestions();
            // },
            // clearQuestionType() {
            //     this.questionType = 0;
            //     this.selectQuestions();
            // },
            initPage() {
                this.questionList.length = 0;
                this.page = 1;
                this.loadedQuestionCount = 999;
            },
            selectQuestions() {
                this.initPage();
                this.loadQuestions();
            },
            loadQuestions() {
                this.$axios({
                    method: 'post',
                    url: '/doctor/' + this.$store.state.user.id + '/question',
                    data: {
                        answeredOrNot: this.questionStatus,
                        questionType: this.questionType,
                        start: this.page,
                        limit: this.limit
                    }
                }).then(res => {
                    console.log(res.data);
                    this.loadedQuestionCount = res.data.length;
                    for (let question in res.data) {
                        if (res.data.hasOwnProperty(question)) {
                            this.questionList.push({
                                id: res.data[question].qid,
                                desc: res.data[question].content,
                                type: res.data[question].type,
                                status: this.questionStatus
                                // departmentId: res.data[i].hospitalDepartmentId
                            });
                        }
                    }
                    this.questionList.sort((a, b) => (a.id > b.id) ? -1 : 1)
                }).catch(error => {
                    console.log(error);
                    // alert("ERROR! Check Console plz! ");
                    this.loadedQuestionCount = 0;
                });

                this.page++;
            },
            load() {
                setTimeout(() => {
                    this.loadQuestions();
                }, 500);
            },
            searchQuestions() {
                this.$axios({
                    method: 'post',
                    url: '/user/similarityQuestion',
                    data: {
                        question: this.searchContent
                    }
                }).then(res => {
                    console.log(res.data);
                    this.loadedQuestionCount = 0;
                    this.initPage();
                    for (let question in res.data) {
                        if (res.data.hasOwnProperty(question)) {
                            let answered = res.data[question].answered === 1;
                            this.questionList.push({
                                id: res.data[question].qid,
                                desc: res.data[question].content,
                                isAnswered: answered
                                // departmentId: res.data[i].hospitalDepartmentId
                            });
                        }
                    }
                }).catch(error => {
                    console.log(error);
                    // alert("ERROR! Check Console plz! ");
                });
            },
            loadDepartments() {
                this.$axios({
                    method: 'get',
                    url: '/QAPlatform/department',
                }).then(res => {
                    // console.log(res.data);
                    for (let department in res.data) {
                        if (res.data.hasOwnProperty(department)) {
                            this.newQuestionForm.departmentOptions.push({
                                value: res.data[department].id,
                                label: res.data[department].name
                            });
                        }
                    }
                }).catch(error => {
                    console.log(error);
                    // alert("ERROR  in function \"loadDepartments( )\"! Check Console plz! ");
                });
            },
            addNewQuestion() {
                // console.log(
                //     'Department ID: ' + this.newQuestionForm.hospitalDepartmentId + '\n' +
                //     'Question Desc: ' + this.newQuestionForm.questionDesc + '\n' +
                //     'Question Type: ' + this.newQuestionForm.questionType
                // );

                this.$axios({
                    method: 'put',
                    url: '/patient',
                    data: {
                        content: this.newQuestionForm.questionDesc,
                        hospitalDepartmentId: this.newQuestionForm.hospitalDepartmentId,
                        type: this.newQuestionForm.questionType,
                        userid: this.$store.state.user.id,
                        // userid: 2,
                        remark: ''
                    }
                }).then(res => {
                    // console.log(res.data);
                    this.$message({
                        type: 'success',
                        message: 'Add Question successfully! '
                    });
                    this.dialogFormVisible = false;
                    this.selectQuestions();
                    this.$refs['addQuestionForm'].resetFields();
                }).catch(error => {
                    console.log(error);
                    // alert("ERROR! Check Console plz! ");
                });
            },
            loadMyQuestions() {
                this.$axios({
                    method: 'get',
                    url: '/patient/' + this.$store.state.user.id + '/question',
                }).then(res => {
                    // console.log(res.data);

                    this.loadedQuestionCount = 0;
                    this.initPage();
                    for (let question in res.data) {
                        if (res.data.hasOwnProperty(question)) {
                            this.questionList.push({
                                id: res.data[question].qid,
                                desc: res.data[question].content,
                                type: res.data[question].type
                            });
                        }
                    }
                    this.loadedQuestionCount = 0;
                    this.questionList.sort((a, b) => (a.id > b.id) ? -1 : 1)
                }).catch(error => {
                    console.log(error);
                    // alert("ERROR  in function \"loadMyQuestions( )\" [Questions]! Check Console plz! ");
                });
            },
            scrollTo() {
                let currentQuestion = JSON.parse(sessionStorage.getItem("addsCurrentQuestionStatusIsChanged"));
                if (currentQuestion.isChanged) {
                    this.selectQuestions();
                } else {
                    // this.$refs.questionListDiv.parentElement.parentElement.scrollTop = this.scroll;
                    // this.$refs.questionListDiv.scrollTop = null;
                }
            },
            showDetails(question) {
                sessionStorage.setItem("addsCurrentQuestion", JSON.stringify(question));
                this.$router.push('/QA/questionDetail/' + question.id);

                // if (question.type === 1) {
                //     this.$router.push('/QA/simpleChoice/' + question.id);
                // } else if (question.type === 2) {
                //     sessionStorage.setItem("addsCurrentQuestion", question.desc);
                //     this.$router.push('/QA/detailedAnswer/' + question.id);
                // }
            }
        },
        created() {
            this.loadMyQuestions();
            this.loadDepartments();
            sessionStorage.setItem("addsCurrentQuestionStatusIsChanged", JSON.stringify({
                isChanged: false
            }));
        },
        watch: {
            '$route': {
              handler(route) {
                this.loadMyQuestions();
              }
            }
        }
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
