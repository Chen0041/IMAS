<template>
  <div class="nav-center">
    <ul>
      <li v-for="(list) in headerList" :key="list.id">
        <router-link :to="{path: list.path}" onmouseover="this.style.color = '#409EFF'" onmouseout="this.style.color = 'rgb(140, 197, 255)'">
          {{list.title}}
        </router-link>
      </li>
    </ul>
  </div>
  <div class="nav-right">
    <span>{{'Hi, ' + store1.state.user.username}}</span>&nbsp;|&nbsp;<el-button type="text" @click="logOut">Log Out</el-button>
  </div>
</template>

<script>
import { useStore } from "vuex"
const store1 = useStore();
export default {
  name: "NavigationBar",
  computed: {
    store1() {
      // TODO store userInfo
      // return store1
      return {"state":{"user":{"username":"Test"}}}}
  },
  data() {
    return {
      headerList: [
        // {id: '1', path: '/deepLearning', title: 'Deep Learning'},
        // {id: '2', path: '/medicalArchivePreprocess', title: 'Medical Archive Preprocess'},
        // {id: '4', path: '/knowledgeGraph', title: 'Knowledge Graph'},
        // {id: '5', path: '/medicalCaseDeepSearch', title: 'Medical Case Deep Search'},
        // {id: '6', path: '/autoDiagnosis', title: 'Automatic Diagnosis'},
        // {id: '7', path: '/QA', title: 'Q&A'},
        // {id: '8', path: '/consult', title: 'Consult'},
        {id: '9', path: '/my', title: 'UserInfo'}
      ],
      isShow: false
    };
  },
  methods: {
    logOut() {
      this.$confirm('Log Out? ', 'Notification', {
        confirmButtonText: 'Confirm',
        cancelButtonText: 'Cancel',
        type: 'warning'
      }).then(() => {
        window.location.reload();
        store1.commit('clearUserInfo');
        this.$router.push('/');
        this.$notify({
          title: 'Success',
          message: 'Log out successfully! ',
          type: 'success'
        });
      }).catch(() => {
      });
    }
  }
}
</script>

<style scoped>
ul {
  line-height: 75px;
  margin: 0;
  padding-left: 0;
}

li {
  list-style: none;
  float: left;
  margin-left: 40px;
}

a {
  text-decoration: none;
  display: block;
  color: rgb(140, 197, 255);
}

.nav-center {
  float: left;
}

.nav-center ul li a.is-active {
  color: #409EFF;
  border-bottom: 4px solid rgb(140, 197, 255);
}

.nav-right {
  float: right;
  line-height: 80px;
}
</style>
