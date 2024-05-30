<template>
  <div>
    <el-dialog
        title="New Doctor User"
        :visible.sync="newDoctorVisible"
        width="640px"
        append-to-body
        :close-on-click-modal="false"
        :close-on-press-escape="false"
        :show-close="false"
    >
      <el-form
          :model="newInfoForm"
          :rules="rules"
          label-position="left"
          label-width="130px"
      >
        <el-form-item label="Login Name" prop="loginName">
          <el-input v-model="newInfoForm.loginName" name="loginName" auto-complete="on"></el-input>
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input v-model="newInfoForm.password" name="password"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer">
        <el-button type="primary" @click="signUp">Sign up</el-button>
        <el-button @click="newDoctorVisible=false">Cancel</el-button>
      </div>
    </el-dialog>

    <el-container>
      <NavigationBar/>
      <el-container>
        <el-main>
          <div id="my-info-div">
            <el-form ref="myInfoForm" :model="myInfoForm" :rules="rules" label-position="left" label-width="90px">
              <div id="my-info-div-1">
                <div id="my-info-div-1-1">
                  <el-form-item label="LoginName" prop="loginName">
                    <el-input v-model="myInfoForm.loginName"></el-input>
                  </el-form-item>
                  <el-form-item label="password" prop="password">
                    <el-input v-model="myInfoForm.password" show-password></el-input>
                  </el-form-item>
                  <el-form-item label="Name" prop="name">
                    <el-input v-model="myInfoForm.name"></el-input>
                  </el-form-item>
                  <el-form-item label="Gender" prop="gender">
                    <el-input v-model="myInfoForm.gender"></el-input>
                  </el-form-item>
                  <el-form-item label="Age" prop="age">
                    <el-input v-model="myInfoForm.age"></el-input>
                  </el-form-item>
                  <el-form-item label="Marriage" prop="marriage">
                    <el-input v-model="myInfoForm.marriage"></el-input>
                  </el-form-item>
                  <el-form-item label="Phone" prop="phone">
                  <el-input v-model="myInfoForm.phone"></el-input>
                  </el-form-item>
                  <el-form-item label="Email" prop="email">
                    <el-input v-model="myInfoForm.email"></el-input>
                  </el-form-item>
                </div>
              </div>
              <el-form-item style="text-align: center;margin: 40px auto;">
                <el-button type="primary" @click="modifyMyInfo">Modify</el-button>
                <el-button @click="resetMyInfo">Reset</el-button>
                <el-button type="primary" @click="newDoctorVisible = true" :style="{ display: allowNewVisible }">New Doctor</el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import NavigationBar from "../NavigationBar";
export default {
  name: "UserInfo",
  components: {
    NavigationBar
  },
  data() {
    return {
      newDoctorVisible: false,
      myInfoForm: {
        name: this.$store.state.user.name?this.$store.state.user.name:'',
        age: this.$store.state.user.age?this.$store.state.user.age:0,
        gender: this.$store.state.user.gender?this.$store.state.user.gender:'',
        phone: this.$store.state.user.phone?this.$store.state.user.phone:'',
        email: this.$store.state.user.email?this.$store.state.user.email:'',
        marriage: this.$store.state.user.marriage?this.$store.state.user.marriage:'',
        loginName: this.$store.state.user.username,
        password: this.$store.state.user.password,
        type: this.$store.state.user.type,
        state: ''
      },
      allowNewVisible: this.$store.state.user.type === 0?'none':'',
      newInfoForm: {
        loginName: '',
        password: '',
      },
      rules: {
        loginName: [
          {required: true, message: 'Please input login name', trigger: 'blur'}
        ],
        password: [
          {required: true, message: 'Please input password', trigger: 'blur'}
        ]
      }
    };
  },
  methods: {
    signUp() {
      this.$axios({
        method: 'post',
        url: '/user/register',
        data: {
          login_name: this.newInfoForm.loginName,
          password: this.newInfoForm.password,
          username: '',
          age: 0,
          gender: '',
          phone: '',
          email: '',
          marriage: '',
          type: 1
        }
      }).then(res => {
        console.log(res.data);
        this.$notify({
          title: "Success",
          message: "Sign up successfully! ",
          type: "success",
        });
      }).catch(error => {
        console.log(error);
        alert("Sign up ERROR! ");
      });
    },
    modifyMyInfo() {
      if (this.myInfoForm.loginName === '') {
        alert("Username cannot be blank! ");
      } else {
        this.$axios({
          method: 'post',
          url: '/user/modify',
          data: {
            login_name: this.myInfoForm.loginName,
            password: this.myInfoForm.password,
            age: this.myInfoForm.age?this.myInfoForm.age:0,
            name: this.myInfoForm.name,
            gender: this.myInfoForm.gender,
            phone: this.myInfoForm.phone,
            email: this.myInfoForm.email,
            marriage: this.myInfoForm.marriage,
          },
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(() => {
          this.$message({
            type: 'success',
            message: 'Modify successfully! ',
            showClose: true
          });
        }).catch(error => {
          this.$message({
            type: 'error',
            message: 'Fail to modify user information! ',
            showClose: true
          });
          console.log(error);
        });
      }
    },
    resetMyInfo() {
      this.$refs['myInfoForm'].resetFields();
      this.$message({
        type: 'success',
        message: 'Reset successfully! '
      });
    }
  }
}
</script>

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

  #my-info-div {
    margin: 40px 80px;
  }

  #my-info-div-1 {
    width: 900px;
    margin: 0 auto;
    padding-left: 300px;
    overflow: hidden;
  }

  #my-info-div-1-1 {
    float: left;
  }

  .el-input {
    width: 300px;
  }
</style>
