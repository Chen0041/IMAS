<template>
  <el-container>
    <el-header style="height: 80px; width: 95vw">
      <NavigationBar/>
    </el-header>

    <el-main style="height: calc(100vh - 80px); width: 95vw">
      <div style="display: flex; justify-content: center;">
          <el-form style="width: 450px; border: 1px solid #cccccc; border-radius: 5px; margin: 50px; padding: 30px" ref="myInfoForm" :model="myInfoForm" :rules="rules" label-position="left" label-width="90px">
            <el-form-item label="loginName" prop="loginName">
              <el-input v-model="myInfoForm.loginName"></el-input>
            </el-form-item>
            <el-form-item label="password" prop="password">
              <el-input v-model="myInfoForm.password"></el-input>
            </el-form-item>
            <el-form-item label="Gender" prop="gender">
              <el-input v-model="myInfoForm.gender"></el-input>
            </el-form-item>
            <el-form-item label="Age" prop="age">
              <el-input v-model="myInfoForm.age"></el-input>
            </el-form-item>
            <el-form-item label="Name" prop="name">
              <el-input v-model="myInfoForm.name"></el-input>
            </el-form-item>
            <el-form-item label="Phone" prop="phone">
              <el-input v-model="myInfoForm.phone"></el-input>
            </el-form-item>
            <el-form-item label="Email" prop="email">
              <el-input v-model="myInfoForm.email"></el-input>
            </el-form-item>

            <el-form-item>
              <el-button type="primary" @click="modifyMyInfo">Modify</el-button>
              <el-button @click="resetMyInfo">Reset</el-button>
              <!--TODO 仅医生角色可见 style="display: none"-->
              <el-button type="primary" @click="doctorRegister">Doctor SignUp</el-button>
            </el-form-item>
          </el-form>
<!--        </el-col>-->
      </div>
    </el-main>
  </el-container>
</template>

<script>
import NavigationBar from "@/components/NavigationBar.vue";
import { useStore } from "vuex"
const store1 = useStore();

export default {
  name: "my",
  components: {
    NavigationBar
  },
  data() {
    return {
      myInfoForm: {
        // TODO 和后端一起测
        // name: store1.state.user.username,
        // age: store1.state.user.age,
        // gender: store1.state.user.gender,
        // phone: store1.state.user.phone,
        // email: store1.state.user.email,
        // loginName: store1.state.user.loginName,
        // password: '',
        name: "",
        age: 0,
        gender: "",
        phone: "",
        email: "",
        loginName: "",
        password: "",
      },
      rules: {
        loginName: [
          {required: true, message: 'Please input loginName', trigger: 'blur'}
        ],
        password: [
          {required: true, message: 'Please input password', trigger: 'blur'}
        ],
        gender: [
          {required: true, message: 'Please input gender', trigger: 'blur'},
          {min: 1, max: 1, message: 'only need one character', trigger: 'blur'}
        ],
        age: [
          {required: true, message: 'Please input age', trigger: 'blur'},
          {min: 1, max: 3, message: 'age is between 1 and 200', trigger: 'blur'}
        ]
      }
    };
  },
  methods: {
    modifyMyInfo() {
      // TODO 新增后端API
      this.$message.error('修改个人信息的功能暂未开放哦！');
    },
    doctorRegister(){
      this.$axios({
        method: 'put',
        url: '/user/register',
        data: {
          login_name: this.myInfoForm.loginName,
          password: this.myInfoForm.password,
          username: this.myInfoForm.name,
          gender: this.myInfoForm.gender,
          age: this.myInfoForm.age,
          phone: this.myInfoForm.phone,
          email: this.myInfoForm.email
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

</style>
