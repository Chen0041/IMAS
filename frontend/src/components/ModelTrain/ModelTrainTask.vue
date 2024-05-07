<template>
  <el-main>
    <div class="top-bar">
      <div class="option-bar">
        <div class="selector-bar">
          <p>Deep Model: </p>
          <el-cascader
              style="width: 400px"
              ref="selectedDeepModelOptions"
              v-model="selectedDeepModel"
              :options="deepModelsOptions"
              :props="{ expandTrigger: 'hover'}"
              @change="selectModel"
              placeholder="Select a model">
          </el-cascader>
        </div>
      </div>
    </div>
    <div>
      <p>Dataset</p>
      <div>
        <template>
          <el-select v-model="characterChosen"
                     @change="chooseDataset">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </template>
      </div>
      <p>Epoch</p>
      <div>
        <template>
          <div class="block">
            <el-slider
                v-model="epoch"
                :step="10"
                show-stops
                show-input>
            </el-slider>
          </div>
        </template>
      </div>
      <p>Batch size</p>
      <div>
        <template>
          <el-select v-model="choosenBatchsize" placeholder="Please"
                     @change="chooseBatchsize"
          >
            <el-option
                v-for="item in batchsize"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </template>
      </div>
      <p>Rnn Cell</p>
      <div>
        <template>
          <el-select v-model="choosenRnncell" placeholder="Please"
                     @change="chooseRnncell">
            <el-option
                v-for="item in rnn"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </template>
      </div>
      <p>Embedding</p>
      <div>
        <template>
          <el-select v-model="choosenEmbedding" placeholder="Please"
                     @change="chooseEmbedding">
            <el-option
                v-for="item in embedding"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </template>
      </div>
      <p>Attention</p>
      <div>
        <template>
          <el-select v-model="choosenAttention" placeholder="Please"
                     @change="chooseAttention">
            <el-option
                v-for="item in attention"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </template>
      </div>
      <p>Construct Module</p>
      <div>
        <template>
          <el-select v-model="choosenConstruct" placeholder="Please"
                     @change="chooseConstruct"
                     >
            <el-option
                v-for="item in construct"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </template>
      </div>

      <p>TrainName</p>
      <div>
        <el-col :span="12">
          <el-input placeholder="Please input model name"
                    v-model="input" size="medium">
          </el-input>
        </el-col>

      </div>
      <div class="operation-btn-bar">
        <el-button type="primary" @click="trainModel()">Train</el-button>
      </div>
    </div>
  </el-main>
</template>

<script>
export default {
  methods: {
    loadDeepModels() {
      this.deepModelsOptions.push({
        value: 0,
        label: 'Joint Embedding Models',
        children: [{
            value: 0,
            label: 'ODL'
        }]
      });
      this.deepModelsOptions.push({
        value: 1,
        label: 'Encoder-Decoder Models',
        children: [
          {value: 0, label:'NLM'},
          {value: 1, label:'VGG-Seq2Seq'}
        ]
      });
      this.deepModelsOptions.push({
        value: 2,
        label: 'Knowledge Embedding Models',
        children: [{
          value: 0,
          label: 'ArticleNet'
        }]
      });
      this.deepModelsOptions.push({
        value: 3,
        label: 'Attention-based Models',
        children: [{
          value: 0,
          label: 'MMBERT'
        }]
      });
      // this.$axios({
      //   method: 'get',
      //   url: '/model/category',
      // }).then(res => {
      //   // console.log(res.data);
      //   for (let category in res.data) {
      //     if (res.data.hasOwnProperty(category)) {
      //       let childModels = [];
      //       let models = res.data[category].models;
      //       for (let model in models) {
      //         if (models.hasOwnProperty(model)) {
      //           childModels.push({
      //             value: models[model].id,
      //             label: models[model].name
      //           });
      //         }
      //       }
      //       this.deepModelsOptions.push({
      //         value: res.data[category].id,
      //         label: res.data[category].name,
      //         children: childModels
      //       });
      //     }
      //   }
      // }).catch(error => {
      //   console.log(error);
      // });
    },
    selectModel(value) {
      console.log(value);
      this.selectedModel=value.label
      // value[value.length-1] modelId

      // console.log(value[value.length-1]);
      // this.getModelInfo(value[value.length-1]);
      // this.modelInfoFormVisible = true;
    },
    getAllDatasets(){
      // options: [
      //   { value: 1, label: "VQA-Med-2019" },
      //   { value: 2, label: "VQA-RAD" },
      //   { value: 3, label: "MVQA(Our)" },
      // ],
      this.$axios({
        method: 'get',
        url: '/model/datasetsLabeled',
      }).then(res => {
        console.log("all datasets: ")
        console.log(res.data)
        for(let i=0;i<res.data.length;i++){
          // console.log(res.data[i])
          let temp={"value":i+1,"label":res.data[i]}

          // console.log(temp)
          this.options.push(temp)
        }
        console.log(this.options)
        // this.characterChosen=this.characterList[0].label;

      }).catch(error => {
        console.log(error);
        // alert("ERROR! Load Models Failed! ");
      });
    },
    chooseEmbedding(value){
      this.choosenEmbedding=value;
    },
    chooseAttention(value){
      this.choosenAttention=value;
    },
    chooseConstruct(value){
      this.choosenConstruct=value;
    },
    chooseRnncell(value){
      this.choosenRnncell=value;
    },
    chooseBatchsize(value){
      this.choosenBatchsize=value;
    },
    chooseDataset(value) {
      // console.log(label);
      this.characterChosen=value;
    },
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex === 1) {
        return "warning-row";
      } else if (rowIndex === 3) {
        return "success-row";
      }
      return "";
    },
    trainModel(){
      this.$notify({
        title: 'Success',
        // message: 'Begin training '+this.selectedModel+' model. ',
        message: 'Start Train! ',
        type: 'success'
      });
      // console.log(item)
      // alert("Begin training "+this.selectedModel+" model.");
      let dataset='';
      let batchsize="";
      let rnn="";
      let embedding="";
      let attention="";
      let construct="";
      //getDataset
      for(let i=0;i<this.options.length;i++){
        if(this.characterChosen==this.options[i].value){
          // console.log(this.options[i])
          dataset=this.options[i].label;
          break;
        }
      }
      //getBatchsize
      for(let i=0;i<this.batchsize.length;i++){
        if(this.choosenBatchsize==this.batchsize[i].value){
          // console.log(this.options[i])
          batchsize=this.batchsize[i].label;
          break;
        }
      }
      //rnn
      for(let i=0;i<this.rnn.length;i++){
        if(this.choosenRnncell==this.rnn[i].value){
          // console.log(this.options[i])
          rnn=this.rnn[i].label;
          break;
        }
      }
      //embedding
      for(let i=0;i<this.embedding.length;i++){
        if(this.choosenEmbedding==this.embedding[i].value){
          // console.log(this.options[i])
          embedding=this.embedding[i].label;
          break;
        }
      }
      //attention
      for(let i=0;i<this.attention.length;i++){
        if(this.choosenAttention==this.attention[i].value){
          // console.log(this.options[i])
          attention=this.attention[i].label;
          break;
        }
      }
      //constructor
      for(let i=0;i<this.construct.length;i++){
        if(this.choosenConstruct==this.construct[i].value){
          // console.log(this.options[i])
          construct=this.construct[i].label;
          break;
        }
      }
      // console.log(dataset)
      // console.log(attention)
      // console.log(construct)
      // this.$axios({
      //   method: 'post',
      //   url: '/train/'+item.name,
      //   data: {
      //     name: this.input,
      //     data: dataset,
      //     batchsize:batchsize,
      //     epoch:this.epoch,
      //     rnn_cell:rnn,
      //     embedding:embedding,
      //     attention:attention,
      //     constructor:construct
      //   }
      // }
      // ).then(res => {
      //   if (res.data=="name_existed"){
      //     alert("ERROR! This name has existed! ");
      //     console.log("name_existed checking.");
      //     console.log(res.data);
      //   }
      //   // else {
      //   //   alert("Success!Begin training "+item.name+" model.");
      //   // }
      //   console.log(this.characterList)
      //   console.log(res.data);
      // }).catch(error => {
      //   console.log(error);
      //   alert("TRAIN ERROR! Check Console plz! ");
      //   this.$axios({
      //         method: 'post',
      //         url: '/error/'+item.name,
      //       }
      //   ).then(res => {
      //     console.log(this.characterList)
      //     console.log(res.data);
      //   }).catch(error => {
      //     console.log(error);});
      // });
    },
  },
  mounted() {
    this.getAllDatasets()
    this.loadDeepModels()

  },
  data() {

    return {
      selectedModel:'',
      selectedDeepModel: [],
      deepModelsOptions: [],
      choosenBatchsize:32,
      characterChosen:1,
      epoch:20,
      choosenRnncell:1,
      choosenEmbedding:3,
      choosenAttention:1,
      choosenConstruct:3,
      input:'',
      options: [
        // { value: 1, label: "VQA-Med-2019" },
        // { value: 2, label: "VQA-RAD" },
        // { value: 3, label: "MVQA(Our)" },
      ],
      rnn:[
        // { value: 1, label: "RNN" },
        { value: 1, label: "GRU" },
        { value: 2, label: "LSTM" },
      ],
      embedding:[
        { value: 1, label: "w2v" },
        { value: 2, label: "glove" },
        { value: 3, label: "none" },
      ],
      attention:[
        { value: 1, label: "SAN" },
        { value: 2, label: "BAN" }
      ],
      construct:[
        { value: 1, label: "maml" },
        { value: 2, label: "autoencoder" },
        { value: 3, label: "both" },
        // { value: 4, label: "none" },
      ],
      batchsize:[
        { value: 1, label: "1" },
        { value: 2, label: "4" },
        { value: 3, label: "8" },
        { value: 4, label: "16" },
        { value: 5, label: "32" },
        { value: 6, label: "64" },
        { value: 7, label: "128" },
      ],
      modelType:[

        {name:'Joint Embedding  Models',
          model:[
            {name:'--->  ODL',
              paper:'Overcoming Data Limitation in Medical Visual Question Answering. ',
              type:"joint embedding",
              link:'https://arxiv.org/abs/1909.11867',
              embedding_vis:false,
              rnn_cell_vis:true,
              attention_vis:true,
              construct_vis:true
            },
          ]},
        {name:'Encoder-Decoder Models',
          model:[
            {name:'--->  NLM',
              paper:'NLM at VQA-Med 2020: Visual Question Answering and Generation in the Medical Domain',
              link:'http://ceur-ws.org/Vol-2696/paper_98.pdf',
              type:"Seq2Seq",
              embedding_vis:true,
              rnn_cell_vis:true,
              attention_vis:false,
              construct_vis:false
            },
            {name:'--->  VGG-Seq2Seq',
              paper:'JUST at VQA-Med: A VGG-Seq2Seq Model',
              link:'http://ceur-ws.org/Vol-2125/paper_171.pdf',
              type:"Seq2Seq",
              embedding_vis:false,
              rnn_cell_vis:false,
              attention_vis:false,
              construct_vis:false
            },
          ]},
        {name:'Attention-based  Models',
          model:[
            {name:'--->  MMBERT',
              paper:'MMBERT: Multimodal BERT Pretraining for Improved Medical VQA',
              link:'https://arxiv.org/abs/2104.01394',
              type:"attention",
              embedding_vis:false,
              rnn_cell_vis:false,
              attention_vis:false,
              construct_vis:false
            },
          ]},
        {name:'Knowledge Embedding  Models',
          model:[
            {name:'--->  ArticleNet',
              paper:'OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge',
              link:'https://openaccess.thecvf.com/content_CVPR_2019/papers/Marino_OK-VQA_A_Visual_Question_Answering_Benchmark_Requiring_External_Knowledge_CVPR_2019_paper.pdf',
              type:"knowledge embedding",
              embedding_vis:false,
              rnn_cell_vis:false,
              attention_vis:false,
              construct_vis:false
            },
          ]},
      ],
    };
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

.el-header {
  background-color: #ffffff;
  color: #333;
  line-height: 60px;
}

.ms {
  text-align: right;
}
</style>

