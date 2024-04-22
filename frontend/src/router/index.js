import Vue from 'vue'
import Router from 'vue-router'

import Login from "../components/UserInfo/Login";
import SignUp from "../components/UserInfo/SignUp";
import UserInfo from "../components/UserInfo/UserInfo";

import AutoQA from "../components/AutoQA/AutoQA"

import deepLearning from "../pages/deepLearning";
import DeepModels from "../component_ori/DeepLearning/DeepModels";
import UploadDataset from "../component_ori/DeepLearning/UploadDataset";
import UploadKg from "../component_ori/DeepLearning/UploadKg";
import ModelEvaluation from "../component_ori/DeepLearning/ModelEvaluation";
import AutoSelection from "../component_ori/DeepLearning/AutoSelection";
import KnowledgeExploration from "../component_ori/DeepLearning/KnowledgeExploration";

import knowledgeGraph from "../pages/knowledgeGraph";

import medicalArchivePreprocess from "../pages/medicalArchivePreprocess";

import medicalCaseDeepSearch from "../pages/medicalCaseDeepSearch"
import CaseCluster from "../component_ori/MedicalSearch/CaseCluster";
import CaseSearch from "../component_ori/MedicalSearch/CaseSearch";
import DeepSearchSubmitQuestions from "../component_ori/MedicalSearch/SubmitQuestions";
import Uploadmedicalrecords from "../component_ori/MedicalSearch/Uploadmedicalrecords";

import autoDiagnosis from "../pages/autoDiagnosis";
import devPage from "../pages/devPage";
import UploadMedicalRecords from "../component_ori/AutoDiagnosis/Uploadmedicalrecords";
import MachineDiagnosis from "../component_ori/AutoDiagnosis/MachineDiagnosis";
import SubmitQuestions from "../component_ori/AutoDiagnosis/SubmitQuestions";

import QA from "../pages/QA";
import Questions from "../component_ori/QA/Questions";
import QuestionDetail from "../component_ori/QA/QuestionDetail";

import consult from "../pages/consult";

import vqa from "../pages/vqa";
import consult2 from "../component_ori/Vqa/AI";
import dataset from "../component_ori/Vqa/dataset";
import modelVqa from "../component_ori/Vqa/ModelEvaluation";
import report from "../component_ori/Vqa/report";
import label from "../component_ori/Vqa/label";



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
      path: '/autoQA',
      component: AutoQA
    },



    {
      path: '/deepLearning',
      component: deepLearning,
      children: [
        {
          path: '',
          redirect: 'deepModels'
        }, {
          path: 'deepModels',
          name: 'DeepModels',
          component: DeepModels,
          meta: {
            keepAlive: true
          }
        }, {
          path: 'uploadDataset',
          name: 'UploadDataset',
          component: UploadDataset
        }, {
          path: 'uploadKnowledgeGraph',
          name: 'UploadKg',
          component: UploadKg
        }, {
          path: 'modelEvaluation',
          name: 'ModelEvaluation',
          component: ModelEvaluation
        }, {
          path: 'autoSelection',
          name: 'AutoSelection',
          component: AutoSelection
        }, {
          path: 'knowledgeExploration',
          name: 'KnowledgeExploration',
          component: KnowledgeExploration
        }
      ]
    }, {
      path: '/knowledgeGraph',
      name: 'knowledgeGraph',
      component: knowledgeGraph,
    }, {
      path: '/medicalArchivePreprocess',
      name: 'medicalArchivePreprocess',
      component: medicalArchivePreprocess,
      meta: {
        keepAlive: false
      }
    }, {
      path: '/medicalCaseDeepSearch',
      name: 'medicalCaseDeepSearch',
      component: medicalCaseDeepSearch,
      children: [
        {
          path: '',
          redirect: 'Uploadmedicalrecords'
        }, {
          path: 'Uploadmedicalrecords',
          name: 'Uploadmedicalrecords',
          component: Uploadmedicalrecords,
        }, {
          path: 'CaseCluster',
          name: 'CaseCluster',
          component: CaseCluster,
        }, {
          path: 'CaseSearch',
          name: 'CaseSearch',
          component: CaseSearch,
        }, {
          path: 'SubmitQuestions',
          name: 'SubmitQuestions',
          component: DeepSearchSubmitQuestions,
        }
      ]
    }, {
      path: '/autoDiagnosis',
      component: autoDiagnosis,
      children: [
        {
          path: '',
          redirect: 'uploadMedicalRecords'
        }, {
          path: 'uploadMedicalRecords',
          name: 'UploadMedicalRecords',
          component: UploadMedicalRecords,
          meta: {
            keepAlive: true
          }
        }, {
          path: 'machineDiagnosis',
          name: 'MachineDiagnosis',
          component: MachineDiagnosis,
          meta: {
            keepAlive: true
          }
        }, {
          path: 'submitQuestions',
          name: 'SubmitQuestions',
          component: SubmitQuestions
        }
      ]
    }, {
      path: '/QA',
      component: QA,
      children: [
        {
          path: '',
          redirect: 'questions'
        }, {
          path: 'questions',
          name: 'Questions',
          component: Questions,
          meta: {
            keepAlive: true
          }
        }, {
          path: 'questionDetail/:id',
          name: 'QuestionDetail',
          component: QuestionDetail
        }
      ]
    }, {
      path: '/consult',
      name: 'consult',
      component: consult,
      meta: {
        keepAlive: true
      }
    }, {
      path: '/devPage',
      name: 'devPage',
      component: devPage,
    }, {
      path: '/vqa',
      // redirect:'/vqa/dataset',
      component: vqa,
      children: [
        {
          path: '',
          redirect: 'dataset'
        }, {
          path: 'dataset',
          name: 'dataset',
          component: dataset,
          meta: {
            keepAlive: true
          }
        }, {
          path: 'label',
          name: 'label',
          component: label,
          meta: {
            keepAlive: true
          }
        },
        {
          path: 'modelEvaluation',
          name: 'modelVqa',
          component: modelVqa
        }, {
          path: 'report',
          name: 'report',
          component: report
        }, {
          path: 'AI',
          name: 'AI',
          component: consult2
        }
      ]
    }
  ]
});

// 导航守卫
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
router.beforeEach((to, from, next) => {
  if (to.path === '/login') {
    // alert("可添加“路由至登录页”的效果！！记得弄一下！！");
    next();
  } else if (to.path === '/signUp') {
    next();
  } else {
    // Why I write this??
    // let token = localStorage.getItem('Authorization');

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
