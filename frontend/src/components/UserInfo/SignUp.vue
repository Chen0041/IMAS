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
        <el-form-item label="Name" prop="name">
          <el-input v-model="signUpForm.name" name="name" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Gender" prop="gender">
          <el-input v-model="signUpForm.gender" name="gender" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Age" prop="age">
          <el-input v-model="signUpForm.age" name="age" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Marriage" prop="marriage">
          <el-input v-model="signUpForm.marriage" name="marriage" auto-complete="on"></el-input>
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
      </el-form>
    </div>
  </div>
</template>

<script>
    export default {
        name: "SignUp",
        data() {
            return {
                signUpForm: {
                    loginName: '',
                    password: '',
                    name: '',
                    gender: '',
                    age: 0,
                    marriage: '',
                    phone: '',
                    email: '',
                    type: 0,
                    state: 0
                },
                rules: {
                    loginName: [
                        {required: true, message: 'Please input login name', trigger: 'blur'},
                        {min: 1, max: 10, message: 'Login name length is between 1 and 10', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: 'Please input password', trigger: 'blur'}
                    ],
                    // name: [
                    //     {required: true, message: 'Please input your name', trigger: 'blur'}
                    // ],
                    // gender: [
                    //     {required: true, message: 'Please input your name', trigger: 'blur'}
                    // ],
                    // age: [
                    //     {required: true, message: 'Please input your name', trigger: 'blur'}
                    // ],
                    // marriage: [
                    //     {required: true, message: 'Please input your name', trigger: 'blur'}
                    // ],
                    // phone: [
                    //     {required: true, message: 'Please input your name', trigger: 'blur'}
                    // ],
                    // email: [
                    //     {required: true, message: 'Please input your name', trigger: 'blur'}
                    // ],
                }
            };
        },
        methods: {
            signUp() {
                this.$axios({
                    method: 'post',
                    url: '/user/register',
                    data: {
                        login_name: this.signUpForm.loginName,
                        password: this.signUpForm.password,
                        username: this.signUpForm.name,
                        gender: this.signUpForm.gender,
                        age: this.signUpForm.age,
                        marriage: this.signUpForm.marriage,
                        phone: this.signUpForm.phone,
                        email: this.signUpForm.email,
                        type: this.signUpForm.type,
                        state: this.signUpForm.state
                    }
                }).then(res => {
                    console.log(res.data);
                    alert("Sign up successfully! Now go to LOG IN! ");
                    this.$router.push('/login');
                }).catch(error => {
                    console.log(error);
                    alert("Sign up ERROR! ");
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

#info-div {
  width: 300px;
  height: 280px;
  text-align: center;
  display: inline-block;
  vertical-align: middle;
  border: 1px solid #dddddd;
  border-radius: 5px;
}

#info-head {
  font-size: 32px;
  font-weight: bolder;
  margin-top: 20px;
}

#info-content {
  font-size: 26px;
}

#sign-up-div {
  width: 450px;
  margin: 50px auto;
  text-align: center;
  border: 1px solid #cccccc;
  border-radius: 5px;
  display: inline-block;
  vertical-align: middle;
}

#form-head {
  font-size: 24px;
  font-weight: bolder;
  color: #409EFF;
}

.el-form {
  padding: 30px 20px;
}

.el-form-item {
  margin-top: 20px;
  margin-bottom: 20px;
}

.el-input {
  width: 300px;
}
</style>