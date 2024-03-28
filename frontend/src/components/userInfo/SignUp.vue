<template>
  <div id="sign-up">
    <div id="sign-up-div">
      <el-form :model="signUpForm" :rules="rules" label-position="left" label-width="100px">
        <p id="form-head">Sign Up</p>
        <el-form-item label="Login Name" prop="loginName">
          <el-input v-model="signUpForm.loginName" name="loginName" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input v-model="signUpForm.password" name="password"></el-input>
        </el-form-item>
        <el-form-item label="Gender" prop="gender">
          <el-input v-model="signUpForm.gender" name="gender" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Age" prop="age">
          <el-input v-model="signUpForm.age" name="age" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Name" prop="name">
          <el-input v-model="signUpForm.name" name="name" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Phone" prop="phone">
          <el-input v-model="signUpForm.phone" name="phone" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Email" prop="email">
          <el-input v-model="signUpForm.email" name="email" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="signUp">Sign up</el-button>
          <el-button type="primary" @click="logIn">Log in</el-button>
        </el-form-item>
        <el-text class="mx-1" type="info">Notes: Doctor accounts can only be registered by doctors.</el-text>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "signUp",
  data() {
    return {
      signUpForm: {
        loginName: '',
        password: '',
        name: '',
        gender: '',
        age: 0,
        phone: '',
        email: ''
      },
      rules: {
        loginName: [
          {required: true, message: 'Please input login name', trigger: 'blur'},
          {min: 1, max: 10, message: 'Login name length is between 1 and 10', trigger: 'blur'}
        ],
        password: [
          {required: true, message: 'Please input password', trigger: 'blur'}
        ],
        name: [
          {required: false, trigger: 'blur'}
        ],
        gender: [
          {required: true, message: 'Please input your gender', trigger: 'blur'},
          {min: 1, max: 1, message: 'only need one character', trigger: 'blur'}
        ],
        age: [
          {required: true, message: 'Please input your age', trigger: 'blur'},
          {min: 1, max: 3, message: 'age is between 1 and 200', trigger: 'blur'}
        ],
        phone: [
          {required: false, trigger: 'blur'}
        ],
        email: [
          {required: false, trigger: 'blur'}
        ]
      }
    };
  },
  methods: {
    signUp() {
      this.$axios({
        method: 'put',
        url: '/user/register',
        data: {
          login_name: this.signUpForm.loginName,
          password: this.signUpForm.password,
          username: this.signUpForm.name,
          gender: this.signUpForm.gender,
          age: this.signUpForm.age,
          phone: this.signUpForm.phone,
          email: this.signUpForm.email
        }
      }).then(res => {
        console.log(res.data);
        this.$notify({
          title: 'Success',
          message: 'Sign up successfully! Now go to LOG IN! ',
          type:'success'
        });
        this.$router.push('/login');
      }).catch(error => {
        console.log(error);
        this.$notify({
          title: 'Warning',
          message: 'Sign up ERROR! ',
          type:'warning'
        });
      });
    },
    logIn() {
      this.$router.push('/login');
    }
  }
}
</script>

<style scoped>
#sign-up {
  text-align: center;
}

#sign-up-div {
  width: 400px;
  margin-left: 400px;
  padding: 20px;
  text-align: center;
  border: 1px solid #cccccc;
  border-radius: 5px;
  display: inline-block;
  vertical-align: middle;
}

#form-head {
  font-size: 24px;
  font-weight: bolder;
  margin-bottom: 20px;
  color: #409EFF;
}
</style>
