import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
// import AddTodoView from '@/views/AddTodoView.vue'
// import ViewTodoView from '@/views/ViewTodoView.vue'

const routes: Array<RouteRecordRaw> = [
  {path: '/', component: HomeView},
  {path: '', component: HomeView},
  {path: '/login', component: LoginView},
  {path: '/register', component: RegisterView},
  // {path: '/add-todo', component: AddTodoView},
  {path: '/add-todo', name: 'add', component: () => import('../views/AddTodoView.vue')},
  // {path: '/view', component: ViewTodoView},
  {path: '/todo/:id/view', name: 'TodoViewSingle', component: () => import('../views/TodoViewView.vue')},
  {path: '/todo/:id/edit', name: 'TodoEditSingle', component: () => import('../views/TodoEditView.vue')},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
