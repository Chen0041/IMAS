<template>
  <el-main>
    <div class="top-bar">
      <div class="option-bar">
        <div class="header-bar">
          <span>All Dataset</span>
        </div>
        <div class="operation-btn-bar">
          <el-button type="primary" @click="newDatasetDialog">Generate Dataset</el-button>
        </div>
      </div>
    </div>
    <el-dialog
      title="Generate Dataset"
      :visible.sync="addDatasetFormVisible"
      width="750px"
      append-to-body
      :close-on-click-modal="false"
      :close-on-press-escape="false"
      :show-close="false"
    >
      <el-steps :active="stepsActive" finish-status="success" align-center>
        <el-step title="Upload your data" icon="el-icon-upload" description="Create dataset"></el-step>
      </el-steps>
      <el-form
        ref="addDatasetForm"
        :model="addDatasetForm"
        :rules="rules"
        label-position="left"
        label-width="130px"
      >
        <el-form-item label="Name" prop="name">
          <el-input v-model="addDatasetForm.name"></el-input>
        </el-form-item>
        <el-form-item label="Description" prop="description">
          <el-input
            type="textarea"
            :rows="5"
            v-model="addDatasetForm.description"
          ></el-input>
        </el-form-item>
        <el-form-item v-if="!this.addDatasetForm.is_single_case" label="Train/Valid/Test" prop="test">
          <template>
            <div class="block">
              <el-slider
                  v-model="addDatasetForm.ratio"
                  range
                  show-stops
                  :max="10">
              </el-slider>
            </div>
          </template>
        </el-form-item>
        <el-form-item>
          <el-upload class="upload-demo"
                     ref="upload"
                     multiple
                     accept=".zip"
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
            <div class="el-upload__tip" slot="tip">please upload zip files</div>
          </el-upload>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-checkbox v-model="addDatasetForm.is_labeled">is_labeled</el-checkbox>
        <el-checkbox v-model="addDatasetForm.is_single_case" style="margin-right: 20px">is_single_case</el-checkbox>
        <el-checkbox v-if="addDatasetForm.is_labeled" v-model="addDatasetForm.need_OCR" disabled style="margin-right: 20px">need_OCR</el-checkbox>
        <el-checkbox v-else v-model="addDatasetForm.need_OCR" style="margin-right: 20px">need_OCR</el-checkbox>
        <el-button type="text" @click="open" style="margin-right: 20px">Readme</el-button>
        <el-button type="primary" @click="upload">Submit</el-button>
        <el-button @click="cancelAddDataset">Cancel</el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="Upload Dataset"
      :visible.sync="uploadDatasetFormVisible"
      width="640px"
      append-to-body
      :close-on-click-modal="false"
      :close-on-press-escape="false"
      :show-close="false"
    >
      <el-steps :active="stepsActive" finish-status="success" align-center>
        <el-step title="Step 1" description="Create dataset"></el-step>
        <el-step title="Step 2" description="Go labeling"></el-step>
      </el-steps>

      <div slot="footer" class="dialog-footer">
        <el-button @click="goNextStep">Finish</el-button>
      </div>
    </el-dialog>

    <div class="content-div scrollable-div">
      <el-scrollbar>
        <div class="content-parent">
          <div class="content">
            <div class="item-list">
              <el-table
                ref="datasetTable"
                :row-class-name=datasetStatus
                :data="datasetTableData"
                :max-height="datasetTableHeight"
              >
                <template slot="empty">
                  <span>{{ datasetTableEmptyText }}</span>
                </template>
                <el-table-column
                  prop="name"
                  label="Name"
                  min-width="20%"
                  align="center"
                  :show-overflow-tooltip="true"
                ></el-table-column>
                <el-table-column
                  prop="description"
                  label="Description"
                  min-width="30%"
                  align="center"
                  :show-overflow-tooltip="true"
                ></el-table-column>
                <el-table-column
                  prop="status"
                  label="Status"
                  min-width="15%"
                  align="center"
                >
                </el-table-column>
                <el-table-column
                  prop="operations"
                  label="Operations"
                  min-width="35%"
                  align="center"
                >
                  <template slot-scope="scope">
                    <div v-if="scope.row.status=='success'">
                      <el-button
                        type="primary"
                        plain
                        size="small"
                        @click="goDownload(scope.row.name)"
                        >Download
                      </el-button>
                      <el-button
                        type="danger"
                        plain
                        size="small"
                        @click="goDelete(scope.row.name)"
                        >Delete
                      </el-button>
                    </div>
                    <div v-else>
                      <el-button
                          type="primary"
                          plain
                          size="small"
                          @click="goDownload(scope.row.name)"
                          disabled
                      >Download</el-button>
                      <el-button
                          type="danger"
                          plain
                          size="small"
                          @click="goDelete(scope.row.name)"
                      >Delete
                      </el-button>
                    </div>
                  </template>
                </el-table-column>ratio
              </el-table>
            </div>
          </div>
        </div>
      </el-scrollbar>
    </div>
  </el-main>
</template>

<script>
export default {
  name: "dataset",
  data() {
    return {
      fileList: [],
      datasetTableHeight: 200,
      datasetTableData: [
        {},
      ],
      datasetTableEmptyText: "Loading...",
      stepsActive: 0,
      addDatasetFormVisible: false,

      addDatasetForm: {
        name: "",
        description: "",
        ratio:[4,8],
        is_single_case: false,
        is_labeled: false,
        need_OCR: false,
      },
      rules: {
        name: [
          { required: true, message: "Please input name", trigger: "blur" },
          // {min: 1, max: 10, message: 'Name length is between 1 and 10', trigger: 'blur'}
        ],
        description: [
          {
            required: true,
            message: "Please input description",
            trigger: "blur",
          },

        ],
        train: [
          {
            required: true,
            message: "Please input description",
            trigger: "blur",
          },

        ],
        valid: [
          {
            required: true,
            message: "Please input description",
            trigger: "blur",
          },

        ],
        test: [
          {
            required: true,
            message: "Please input description",
            trigger: "blur",
          },

        ],
      },
      uploadDatasetFormVisible: false,
      uploadDatasetForm: {
        datasetId: 0,
        type: "",
      },

      trainSetExist: false,
      testSetExist: false,
      devSetExist: false,
      trainSetFileList: [],
      testSetFileList: [],
      devSetFileList: [],
    };
  },
  methods: {
    datasetStatus({row}, rowIndex) {
      if (row.status == 'success'){
        return 'success-row';
      }
      else if (row.status == 'processing'){
        return 'warning-row';
      }
      else{
        return 'danger-row'
      }
    },
    handleRemove(file,fileList) {
      console.log(file,fileList);
    },
    // 文件上传成功时的函数
    handleFilUploadSuccess (res,file,fileList) {
      console.log(res,file,fileList)
      this.$message.success("上传成功")
    },
    handleUpdate () {
      this.dialogVisible = true;
    },

    download(url){
      const ele = document.createElement('a');
      ele.setAttribute('href', this.$options.filters['filterUrl'](url));
      //this.$options.filters['filterUrl']是调用全局过滤器,filterUrl是你自己项目main.js里面定义的过滤器
      ele.setAttribute('download',name);
      ele.style.display = 'none';
      document.body.appendChild(ele);
      ele.click();
      document.body.removeChild(ele);
    },

    goDownload(dataset){
      this.$axios({
        method: 'get',
        url: '/dataset/download/' + dataset,
      }).then(res => {
        console.log(res.data);
        const content=res.data;
        const blob=new Blob([content]);
        const fileName='Preprocessed_data.csv';
        if('download' in document.createElement('a')){
          const link=document.createElement('a')
          link.download=fileName
          link.style.display='none'
          link.href=URL.createObjectURL(blob)
          document.body.appendChild(link)
          link.click()
          URL.revokeObjectURL(link.href)
          document.body.removeChild(link)
        }else{
          navigator.msSaveBlob(blob,fileName)
        }
      }).catch(error => {
        console.log(error);
        alert("ERROR! Download Preprocessed Data Failed! ");
      });
    },
    goDelete(dataset){
      this.$axios({
        method: 'delete',
        url: '/dataset/delete/' + dataset,
        data: {
          login_name: this.$store.state.user.username,
        },
      }).then(res => {
        this.$notify({
          message: 'Successfully delete! ',
          type: 'success',
          showClose: true
        });
        location.reload();
      }).catch(error => {
        console.log(error);
        alert("Delete error! ");
      });
    },
    loadDataset() {
      this.$axios({
        method: "get",
        url: "/datasets",
      })
        .then((res) => {
          console.log(res.data);
          this.datasetTableData = res.data;
          if (this.datasetTableData.length === 0) {
            this.datasetTableEmptyText = "No Dataset";
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    open() {
      this.$notify({
        title: 'File format',
        dangerouslyUseHTMLString: true,
        message: "1. zip文件中包含医学图像和对应病例描述，分别用图片（*.jpg, *.jpeg, *.png）和文本（*.txt, *.csv等）表示。 <br/> " +
            "2. 用relationship.csv文件标示图片和文本的对应。 <br/> " +
            "3. 若选中is_labeled，relationship.csv文件每列分别为：图片文件名、病例名、图片描述、疾病、药物，不再上传文本。反之，每列分别为：图片文件名、文本文件名。含扩展名，不含表头。 <br/> " +
            "4. 若选中is_single_case，则图片、文本（如有需要）、对应关系三个文件均置于根目录下。否则创建两个文件夹，分别命名为img和txt，存放图片和文本文件。 <br/> " +
            "5. 若选中need_OCR，则文本描述可以用图片形式表示。",
        type: 'info',
        showClose: true
      });
    },
    newDatasetDialog() {
      this.stepsActive = 0;
      this.addDatasetFormVisible = true;
    },
    upload() {
      this.uploadFormVisible = false;
      this.$refs.upload.submit();
    },
    uploadDataset(content) {
      let params = new FormData();
      params.append("login_name", this.$store.state.user.username);
      params.append("name", this.addDatasetForm.name);
      params.append("description", this.addDatasetForm.description);
      params.append("is_single_case", this.addDatasetForm.is_single_case);
      params.append("is_labeled", this.addDatasetForm.is_labeled);
      params.append("need_OCR", this.addDatasetForm.need_OCR);
      params.append("train", this.addDatasetForm.ratio[0]);
      params.append("valid", this.addDatasetForm.ratio[1]-this.addDatasetForm.ratio[0]);
      params.append("test", 10-this.addDatasetForm.ratio[1]);
      params.append("file", content.file);
      console.log(params)
      this.$axios({
        method: "post",
        url: "/dataset/upload",
        data:params,
      })
        .then((res) => {
          console.log(res.data);
          this.addDatasetFormVisible = false;
          this.loadDataset();
          this.$notify({
            title: "Success",
            message: "Successfully create dataset! ",
            type: "success",
          });
          this.openUploadDatasetForm(res.data, "", "", "");
        })
        .catch((error) => {
          console.log(error);
          this.$notify({
            message: "Upload dataset error, please check console for detail! ",
            type: "error",
          });
        });
    },
    cancelAddDataset() {
      this.closeAddDatasetForm();
    },
    closeAddDatasetForm() {
      this.addDatasetFormVisible = false;
      this.$refs["addDatasetForm"].resetFields();
    },
    goNextStep() {
      this.$router.push('/dataset/preprocessed');
      this.uploadDatasetFormVisible = false;
    },
    openUploadDatasetForm(datasetId, trainSet, testSet, devSet) {
      this.stepsActive = 1;
      this.uploadDatasetForm.datasetId = datasetId;
      this.trainSetExist = trainSet !== "";
      this.testSetExist = testSet !== "";
      this.devSetExist = devSet !== "";
      this.uploadDatasetFormVisible = true;
    },
  },
  created() {
    this.loadDataset();
  },
  mounted() {
    this.$nextTick(function () {
      this.datasetTableHeight =
        window.innerHeight - this.$refs.datasetTable.$el.offsetTop - 190;
      let self = this;
      window.onresize = function () {
        self.datasetTableHeight =
          window.innerHeight - self.$refs.datasetTable.$el.offsetTop - 190;
      };
    });
  },
};
</script>

<style>
.el-table .warning-row {
  background: oldlace;
}
.el-table .success-row {
  background: #f0f9eb;
}
.el-table .danger-row {
  background: #FF00000D;
}
</style>

<style scoped>
.el-main {
  position: fixed;
  top: 80px;
  left: 260px;
  right: 30px;
  bottom: 0;
  margin: 20px;
  padding: 10px;
}

.option-bar {
  display: inline-block;
  position: fixed;
  left: 280px;
  right: 40px;
}

.header-bar {
  float: left;
  margin: 0 20px;
}

.header-bar span {
  font-size: 20px;
  font-weight: bold;
  float: left;
}

.operation-btn-bar {
  float: right;
  margin: 0 20px;
  overflow: hidden;
}

.el-form {
  padding: 0 10px;
}

/*.el-upload {*/
/*  display: inline-block;*/
/*}*/

.content-div {
  position: fixed;
  top: 130px;
  left: 280px;
  right: 40px;
  bottom: 20px;
  z-index: -100;
}

.content {
  margin: 10px;
  padding: 30px;
}

.dataset-btn {
  margin: 0 auto;
}

.browse-btn {
  width: 70px;
  height: 30px;
  margin: 5px;
  vertical-align: top;
}

.el-tag {
  width: 95px;
  text-align: center;
}

.el-steps {
  margin-bottom: 40px;
}
</style>
