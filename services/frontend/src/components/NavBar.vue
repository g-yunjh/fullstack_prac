<template>
    <header>
      <nav class="bg-gray-800">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
          <a class="text-white text-lg font-bold" href="/">FastAPI + Vue</a>
          <button class="text-white md:hidden" @click="toggleNavbar">
            <span class="material-icons">menu</span>
          </button>
          <div :class="{'hidden': !navbarOpen, 'flex': navbarOpen}" class="md:flex md:items-center">
            <ul v-if="isLoggedIn" class="flex space-x-4">
              <li>
                <router-link class="text-white hover:bg-gray-700 px-3 py-2 rounded" to="/">Home</router-link>
              </li>
              <li>
                <router-link class="text-white hover:bg-gray-700 px-3 py-2 rounded" to="/dashboard">Dashboard</router-link>
              </li>
              <li>
                <router-link class="text-white hover:bg-gray-700 px-3 py-2 rounded" to="/profile">My Profile</router-link>
              </li>
              <li>
                <a class="text-white hover:bg-gray-700 px-3 py-2 rounded" @click="logout">Log Out</a>
              </li>
            </ul>
            <ul v-else class="flex space-x-4">
              <li>
                <router-link class="text-white hover:bg-gray-700 px-3 py-2 rounded" to="/">Home</router-link>
              </li>
              <li>
                <router-link class="text-white hover:bg-gray-700 px-3 py-2 rounded" to="/register">Register</router-link>
              </li>
              <li>
                <router-link class="text-white hover:bg-gray-700 px-3 py-2 rounded" to="/login">Log In</router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'NavBar',
    data() {
      return {
        navbarOpen: false,
      };
    },
    computed: {
      isLoggedIn() {
        return this.$store.getters.isAuthenticated;
      },
    },
    methods: {
      async logout() {
        await this.$store.dispatch('logOut');
        this.$router.push('/login');
      },
      toggleNavbar() {
        this.navbarOpen = !this.navbarOpen;
      },
    },
  });
  </script>
  
  <style scoped>
  a {
    cursor: pointer;
  }
  </style>
  