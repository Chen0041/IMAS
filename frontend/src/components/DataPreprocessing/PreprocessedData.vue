<template>
  <el-main>
    <div class="top-bar">
      <div class="option-bar">
        <div class="header-bar">
          <span>Preprocessed Data</span>
        </div>
        <el-row type="flex" justify="end">
          <el-select v-model="characterChosen" placeholder="Please choose dataset."
                     @change="chooseCharacter">
            <el-option
                v-for="item in characterList_dataset"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </el-row>
      </div>
    </div>
    
    <div>
      <el-table :data="patientIds.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%">
        <el-table-column label="Text Name">
          <template slot-scope="scope">
            <span>{{scope.row.patientName}}</span>

          </template>
        </el-table-column>
        <el-table-column label="Picture Name">
          <template slot-scope="scope">
            <span>{{scope.row.photoName}}</span>
          </template>
        </el-table-column>
        <el-table-column label="Description" width="350">
          <template slot-scope="scope">
            <span>{{scope.row.description}}</span>
          </template>
        </el-table-column>
        <el-table-column label="Disease">
          <template slot-scope="scope">
            <span>{{scope.row.disease}}</span>
          </template>
        </el-table-column>
        <el-table-column label="Medicine">
          <template slot-scope="scope">
            <span>{{scope.row.medicine}}</span>
          </template>
        </el-table-column>

        <el-table-column label="Modify">
          <template slot-scope="scope">
            <el-popover
                placement="bottom"
                title="Modify preprocessed data"
                width="1000"
                trigger="click"
                content="">
              <el-button slot="reference" @click="getPhoto(scope.row.photoName)">Edit</el-button>

              <div>
                <el-scrollbar style="height:500px">
                  <el-row>
                    <p style="font-size:15px">Description:</p>
                    <el-input v-model="scope.row.description" type="textarea" style="width:90%; float:left"></el-input>
                  </el-row>
                  <el-row>
                    <p style="font-size:15px">Disease:</p>
                    <el-input v-model="scope.row.disease"  style="width:90%; float:left"></el-input>
                  </el-row>
                  <el-row>
                    <p style="font-size:15px">Medicine:</p>
                    <el-input v-model="scope.row.medicine"  style="width:90%; float:left"></el-input>
                  </el-row>
                  <el-row>
                    <p style="font-size:15px">Picture:</p>
                  </el-row>
                  <label>
                    <img :src="imgSrc" alt=""/>
                  </label>
                  <p style="text-align:center;">
                    <el-button type="primary" @click="modifyData(scope.row.patientName,scope.row.photoName,scope.row.description,scope.row.disease,scope.row.medicine)">Submit</el-button>
                  </p>
                </el-scrollbar>
              </div>
            </el-popover>
          </template>
        </el-table-column>
      </el-table>
      <!--分页区域-->
      <!--        <div class="block" style="margin-top:15px;">-->
      <!--            <el-pagination align='center' @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage" :page-sizes="[1,5,10,20]" :page-size="pageSize" layout="total, sizes, prev, pager, next, jumper" :total="patientIds.length">-->
      <!--            </el-pagination>-->
      <!--        </div>-->
      <div class="yema">
        <el-pagination background
                       @size-change="handleSizeChange"
                       @current-change="handleCurrentChange"
                       :current-page="currentPage"
                       :page-sizes="[5,10,15]"
                       :page-size=10
                       layout="total,jumper,prev, pager, next,sizes"
                       :total="patientIds.length" >
        </el-pagination>
      </div>
    </div>
  </el-main>
</template>

<script>
export default {
  data() {
    return {
      characterList_dataset: [],
      imgSrc:require('../../assets/medical_pic.jpg'),
      characterChosen:"",
      description:'',
      patientIds:[],
      currentPage: 1, // 当前页码
      total: 20, // 总条数
      pageSize: 100 ,// 每页的数据条数
    }
  },
  methods: {
    chooseCharacter(value) {
      // console.log(value)
      // console.log("dataset name: ")
      // console.log(this.characterList_dataset[0].label)
      this.characterChosen=value;
      this.getAllPatients()
    },
    getAllModels(){
      this.$axios({
        method: 'get',
        url: '/dataset/preprocessed',
      }).then(res => {
        // console.log("all datasets: ")
        // console.log(res.data)
        for(let i=0;i<res.data.length;i++){
          // console.log(res.data[i])
          let temp={"value":i+1,"label":res.data[i]}

          // console.log(temp)
          this.characterList_dataset.push(temp)
        }
        // this.characterChosen=this.characterList[0].label;

      }).catch(error => {
        console.log(error);
        alert("ERROR! Load Models Failed! ");
      });
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      // this.currentPage = 1;
      this.pageSize = val;
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
    },
    modifyData(p1,p2,description,disease,medicine){
      console.log("patientName",p1);
      console.log("photoName",p2);
      console.log("description", description);

      let params = new FormData();
      // params.append("patientName", p1);
      // params.append("photoName", p2);
      params.append("description", description);
      params.append("disease", disease);
      params.append("medicine", medicine);

      this.$axios({
        method: 'post',
        url: '/dataset/'+this.characterList_dataset[this.characterChosen-1].label+'/modify/'+p1,
        data: params
      }).then(res => {
        this.$message({
          message: 'Successfully!',
          type: 'success',
          offset:60,
          showClose: true
        });
        // location.reload();
        // this.message="提交完成";
      }).catch(error => {
        console.log(error);
      });
    },
    getPhoto(photo_name){
      this.$axios({
        method: 'get',
        url: '/loadPicture/'+this.characterList_dataset[this.characterChosen-1].label+'/'+photo_name,
        responseType:'blob'
        // data: params
      }).then(res => {
        // console.log(res.data)
        let blob = new Blob([res.data], {
          type: "image/png",
        });
        this.imgSrc=window.URL.createObjectURL(blob)
      }).catch(error => {
        console.log(error);
      });
    },
    getAllPatients(){
      this.$axios({
        method: 'get',
        url: '/dataset/'+this.characterList_dataset[this.characterChosen-1].label+'/cases',
      }).then(res => {
        console.log("dataset name: "+this.characterList_dataset[this.characterChosen-1].label)
        this.patientIds=[]
        for (let row in res.data) {
          if (res.data.hasOwnProperty(row)) {
            this.patientIds.push({
              patientName: res.data[row].patient_name,
              photoName: res.data[row].picture_name,
              medicine:res.data[row].medicine ,
              disease:res.data[row].disease,
              description:res.data[row].whole_desc

            });
          }
        }
      }).catch(error => {
        console.log(error);
      });
    }
  },mounted(){
    this.getAllModels()
  }
}
</script>
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

.d-radio {
  padding-left: 0;
  padding-bottom: 10px;
  margin-bottom: 5px;
  border-bottom: 1px solid #e2e2e2;
}

.d-radio .col-md-12 {
  padding-left: 0;
}
.el-scrollbar__wrap{
  overflow-x: hidden;
}
.el-message {
  top:350px !important;
  z-index: 99999 !important;
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

</style>