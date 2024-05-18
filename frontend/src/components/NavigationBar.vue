<template>
  <el-header height="80px">
    <div>
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
        <span>{{'Hi, ' + this.$store.state.user.username}}</span>&nbsp;|&nbsp;<el-button type="text" @click="logOut">Log Out</el-button>
      </div>
    </div>
  </el-header>
</template>

<script>
    export default {
        name: "NavigationBar",
        data() {
            return {
                headerList: [
                  {id: '1', path: '/dataset', title: 'Data Preprocess \t'},
                  {id: '2', path: '/modelTrain', title: 'Model Train \t'},
                  {id: '3', path: '/autoQA', title: 'Auto QA \t'},
                  {id: '4', path: '/QA', title: 'QA Platform \t'},
                  {id: '5', path: '/userInfo', title: 'User Info'}
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
                    this.$store.commit('clearUserInfo');
                    this.$router.push('/login');
                    location.reload();
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
  .el-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;

    border-bottom: 1px solid #dcdfe6;
    padding-left: 0;
    font-size: 16px;
    background-color: white;
    z-index: 999;
  }

  ul {
    line-height: 76px;
    margin: 0;
    padding-left: 0;
    /*padding-left: 20px;*/
  }

  li {
    list-style: none;
    float: left;
    margin-left: 20px;
    /*height: 80px;*/
  }

  a {
    text-decoration: none;
    display: block;
    /* padding: 0 10px; */
    color: rgb(140, 197, 255);
    /*font-weight: bolder;*/
  }

  .nav-left {
    height: 80px;
    float: left;
    cursor: pointer;
  }

  .nav-center {
    float: left;
    /*margin-left: 50px;*/
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
