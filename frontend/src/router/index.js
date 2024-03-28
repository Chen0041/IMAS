import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/userInfo/Login.vue'
import SignUp from '../components/userInfo/SignUp.vue'
import My from '../components/userInfo/My.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
    }
    // {
    //   path: '/signUp',
    //   name: 'signUp',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../components/userInfo/My.vue')
    // }
  ]
})

export default router
