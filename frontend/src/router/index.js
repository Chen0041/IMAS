import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/userInfo/Login.vue'
import SignUp from '../components/userInfo/SignUp.vue'
import My from '../components/userInfo/My.vue'

import Datasets from '../components/dataPreprocessing/Datasets.vue'
import Preprocessing from '../components/dataPreprocessing/Preprocessing.vue'

import Train from '../components/modelTrain/Train.vue'
import Reports from '../components/modelTrain/Reports.vue'

import AutoQA from '../components/autoQA/AutoQA.vue'

import KnowledgeGraph from '../components/similarSearch/KnowledgeGraph.vue'
import SimilarGraphSearch from '../components/similarSearch/SimilarGraphSearch.vue'

import QAPlatform from "../components/QAPlatform/QAPlatform.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      // UserInfo
    {
      path: '/',
      redirect: '/login'
    }, {
      path: '/login',
      name: 'login',
      component: Login
    }, {
      path: '/signUp',
      name: 'signUp',
      component: SignUp
    }, {
      path: '/my',
      name: 'my',
      component: My
    },
    // DataPreprocessing
    {
      path: '/datasets',
      name: 'datasets',
      component: Datasets
    }, {
      path: '/preprocessing',
      name: 'preprocessing',
      component: Preprocessing
    },
    // ModelTrain
    {
      path: '/train',
      name: 'train',
      component: Train
    }, {
      path: '/reports',
      name: 'reports',
      component: Reports
    },
    // AutoQA
    {
      path: '/autoQA',
      name: 'autoQA',
      component: AutoQA
    },
    // SimilarSearch
    {
      path: '/knowledgeGraph',
      name: 'knowledgeGraph',
      component: KnowledgeGraph
    }, {
      path: '/similarGraphSearch',
      name: 'similarGraphSearch',
      component: SimilarGraphSearch
    },
    // QAPlatform
    {
      path: '/QAPlatform',
      name: 'QAPlatform',
      component: QAPlatform
    }]
})

export default router
