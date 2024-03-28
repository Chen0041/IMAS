<template>
  <div style="display: flex; justify-content: center;">
    <el-col :span="8"></el-col>
    <el-col :span="8">
      <el-form style="width: 450px; border: 1px solid #cccccc; border-radius: 5px; padding: 20px" ref="loginForm" :model="loginForm">
        <p style="font-size: 22px; font-weight: bolder; color: #409EFF; margin: 20px;">Intelligent Medical Analysis System</p>
        <el-form-item prop="username">
          <el-input v-model="loginForm.username" name="username" placeholder="Username" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="loginForm.password" name="password" placeholder="Password" auto-complete="on" show-password @keyup.enter.native="login"></el-input>
        </el-form-item>
        <el-form-item>
          <el-col :span="7"></el-col>
          <el-button type="primary" @click="login">Log in</el-button>
          <el-button type="primary" @click="signUp">Sign up</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </div>
</template>

<script>
import { useStore } from "vuex"
const store1 = useStore();
export default {
  name: "login",
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    login() {
      if (this.loginForm.username === '' || this.loginForm.password === '') {
        // alert("Username or password cannot be blank! ");
        this.$notify({
          title: 'Warning',
          message: 'Username or password cannot be blank! ',
          type:'warning'
        });
      } else {
        this.$axios({
          method: 'post',
          url: '/user/login',
          data: {
            login_name: this.loginForm.username,
            password: this.loginForm.password
          },
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(res => {
          // console.log(res.data);
          // console.log("Token: " + res.headers["token"]);
          // Save user's info & token
          store1.commit('saveUserInfo', res.data.info);
          store1.commit('saveToken', res.headers["token"]);
          this.$notify({
            title: 'Success',
            message: 'Welcome! ',
            type: 'success'
          });
          this.$router.push('/my');
        }).catch(error => {
          console.log(error);
          this.$notify({
            title: 'Warning',
            message: 'Username or password is incorrect. ',
            type:'warning'
          });
        });
      }
    },
    signUp() {
      this.$router.push('/signUp');
    },
    clearForm() {
      this.$refs['loginForm'].resetFields();
    }
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.clearForm();
    })
  }
}
</script>

<style scoped>

</style>
