import { createRouter, createWebHistory } from 'vue-router'
import RegisterView from '@/views/RegisterView.vue';
import LoginView from '@/views/LoginView.vue';
import DashboardView from '@/views/DashboardView.vue';
import ProfileView from '@/views/ProfileView.vue';
import PostView from '@/views/PostView.vue';
import EditPostView from '@/views/EditPostView.vue';
import store from '@/store';
import SearchView from '@/views/SearchView.vue';


const routes = [
  {
    path: '/',
    name: "Login",
    component: LoginView,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchView,
    meta: { requiresAuth: true },
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: '/post/:id',
    name: 'Post',
    component: PostView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/editpost/:id',
    name: 'EditPost',
    component: EditPostView,
    meta: { requiresAuth: true },
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/');
  } else {
    next();
  }
});

export default router