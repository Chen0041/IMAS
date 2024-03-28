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
    <span>{{'Hi, ' + store1.state.user.username}}</span>&nbsp;|&nbsp;<el-button link type="primary" @click="logOut">Log Out</el-button>
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
        {id: '1', path: '/datasets', title: 'Data Preprocessing'},
        {id: '2', path: '/train', title: 'Model Train'},
        {id: '3', path: '/autoQA', title: 'Auto QA'},
        {id: '4', path: '/knowledgeGraph', title: 'Similar Search'},
        {id: '5', path: '/QAPlatform', title: 'QA Platform'},
        {id: '6', path: '/my', title: 'User Info'}
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
        this.$router.push('/login');
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
