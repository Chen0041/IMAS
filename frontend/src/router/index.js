import Vue from 'vue'
import Router from 'vue-router'

import Login from "../components/UserInfo/Login";
import SignUp from "../components/UserInfo/SignUp";
import UserInfo from "../components/UserInfo/UserInfo";

import DataPreprocessing from "../components/dataPreprocessing/DataPreprocessing";
import DatasetUpload from "../components/dataPreprocessing/DatasetUpload";
import PreprocessedData from "../components/dataPreprocessing/PreprocessedData";

import modelTrain from "../components/ModelTrain/ModelTrain.vue";
import ModelTrainTask from "../components/ModelTrain/ModelTrainTask.vue";
import Report from "../components/ModelTrain/Report.vue";

import AutoQA from "../components/AutoQA/AutoQA"

import Questions from "../components/QAPlatform/Questions";

Vue.use(Router);

const router = new Router({
  // 使用 history 模式消除 URL 中的 # 号
  mode: "history",
  linkActiveClass: 'is-active',
  routes: [
    {
      path: '/',
      redirect: '/login'
    }, {
      path: '/login',
      component: Login
    }, {
      path: '/signUp',
      component: SignUp
    }, {
      path: '/userInfo',
      name: 'UserInfo',
      component: UserInfo,
      meta: {
        keepAlive: true
      }
    }, {
      path: '/dataset',
      component: DataPreprocessing,
      children: [
        {
          path: '',
          redirect: '/dataset/upload'
        }, {
          path: '/dataset/upload',
          component: DatasetUpload,
          meta: {
            keepAlive: true
          }
        }, {
          path: '/dataset/preprocessed',
          component: PreprocessedData,
          meta: {
            keepAlive: true
          }
        }
      ]
    },{
      path: '/modelTrain',
      component: modelTrain,
      children: [
        {
          path: '',
          redirect: '/modelTrain/new'
        }, {
          path: '/modelTrain/new',
          component: ModelTrainTask,
        }, {
          path: '/modelTrain/report',
          component: Report,
        }
      ]
    },
    {
      path: '/autoQA',
      component: AutoQA
    },{
      path: '/QA',
      component: Questions
    }
  ]
});

// 导航守卫
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
router.beforeEach((to, from, next) => {
  if (to.path === '/login') {
    next();
  } else if (to.path === '/signUp') {
    next();
  } else {
    let userInfo = JSON.parse(sessionStorage.getItem("addsCurrentUserInfo"));
    let token = sessionStorage.getItem("addsCurrentUserToken");
    if (token === 'null' || token === '' || userInfo === null || userInfo === '') {
      next('/login');
    } else {
      next();
    }
  }
});

export default router;
